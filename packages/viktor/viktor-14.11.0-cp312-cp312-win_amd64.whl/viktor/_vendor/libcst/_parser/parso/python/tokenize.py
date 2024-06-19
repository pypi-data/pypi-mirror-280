# Copyright 2004-2005 Elemental Security, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.
#
# Modifications:
# Copyright David Halter and Contributors
# Modifications are dual-licensed: MIT and PSF.
# 99% of the code is different from pgen2, now.
#
# A fork of `parso.python.tokenize`.
# https://github.com/davidhalter/parso/blob/master/parso/python/tokenize.py
#
# The following changes were made:
# - Changes to be compatible with PythonTokenTypes
# - Removed main section
# - Applied type stubs directly
# - Removed Python 2 shims
# - Added support for Python 3.6 ASYNC/AWAIT hacks
#
# -*- coding: utf-8 -*-
# This tokenizer has been copied from the ``tokenize.py`` standard library
# tokenizer. The reason was simple: The standard library tokenizer fails
# if the indentation is not right. To make it possible to do error recovery the
# tokenizer needed to be rewritten.
#
# Basically this is a stripped down version of the standard library module, so
# you can read the documentation there. Additionally we included some speed and
# memory optimizations here.
# pyre-unsafe
from __future__ import absolute_import

import itertools as _itertools
import re
import sys
from codecs import BOM_UTF8
from collections import namedtuple
from dataclasses import dataclass
from typing import Dict, Generator, Iterable, Optional, Pattern, Set, Tuple

from viktor._vendor.libcst._parser.parso.python.token import PythonTokenTypes
from viktor._vendor.libcst._parser.parso.utils import PythonVersionInfo, split_lines

# Maximum code point of Unicode 6.0: 0x10ffff (1,114,111)
MAX_UNICODE = "\U0010ffff"
BOM_UTF8_STRING = BOM_UTF8.decode("utf-8")

STRING = PythonTokenTypes.STRING
NAME = PythonTokenTypes.NAME
NUMBER = PythonTokenTypes.NUMBER
OP = PythonTokenTypes.OP
NEWLINE = PythonTokenTypes.NEWLINE
INDENT = PythonTokenTypes.INDENT
DEDENT = PythonTokenTypes.DEDENT
ASYNC = PythonTokenTypes.ASYNC
AWAIT = PythonTokenTypes.AWAIT
ENDMARKER = PythonTokenTypes.ENDMARKER
ERRORTOKEN = PythonTokenTypes.ERRORTOKEN
ERROR_DEDENT = PythonTokenTypes.ERROR_DEDENT
FSTRING_START = PythonTokenTypes.FSTRING_START
FSTRING_STRING = PythonTokenTypes.FSTRING_STRING
FSTRING_END = PythonTokenTypes.FSTRING_END


@dataclass(frozen=True)
class TokenCollection:
    pseudo_token: Pattern
    single_quoted: Set[str]
    triple_quoted: Set[str]
    endpats: Dict[str, Pattern]
    whitespace: Pattern
    fstring_pattern_map: Dict[str, str]
    always_break_tokens: Set[str]


_token_collection_cache: Dict[PythonVersionInfo, TokenCollection] = {}


def group(*choices: str, **kwargs: object) -> str:
    capture = kwargs.pop("capture", False)  # Python 2, arrghhhhh :(
    assert not kwargs

    start = "("
    if not capture:
        start += "?:"
    return start + "|".join(choices) + ")"


def maybe(*choices: str) -> str:
    return group(*choices) + "?"


# Return the empty string, plus all of the valid string prefixes.
def _all_string_prefixes(
    version_info: PythonVersionInfo,
    include_fstring: bool = False,
    only_fstring: bool = False,
) -> Set[str]:
    def different_case_versions(prefix):
        for s in _itertools.product(*[(c, c.upper()) for c in prefix]):
            yield "".join(s)

    # The valid string prefixes. Only contain the lower case versions,
    #  and don't contain any permuations (include 'fr', but not
    #  'rf'). The various permutations will be generated.
    valid_string_prefixes = ["b", "r"]
    if version_info >= (3, 0):
        valid_string_prefixes.append("br")
    if version_info < (3, 0) or version_info >= (3, 3):
        valid_string_prefixes.append("u")

    result = {""}
    if version_info >= (3, 6) and include_fstring:
        f = ["f", "fr"]
        if only_fstring:
            valid_string_prefixes = f
            result = set()
        else:
            valid_string_prefixes += f
    elif only_fstring:
        return set()

    # if we add binary f-strings, add: ['fb', 'fbr']
    for prefix in valid_string_prefixes:
        for t in _itertools.permutations(prefix):
            # create a list with upper and lower versions of each
            #  character
            result.update(different_case_versions(t))
    if version_info <= (2, 7):
        # In Python 2 the order cannot just be random.
        result.update(different_case_versions("ur"))
        result.update(different_case_versions("br"))
    return result


def _compile(expr: str) -> Pattern:
    return re.compile(expr, re.UNICODE)


def _get_token_collection(version_info: PythonVersionInfo) -> TokenCollection:
    try:
        return _token_collection_cache[version_info]
    except KeyError:
        _token_collection_cache[version_info] = result = _create_token_collection(
            version_info
        )
        return result


fstring_raw_string = _compile(r"(?:[^{}]+|\{\{|\}\})+")

unicode_character_name = r"[A-Za-z0-9\-]+(?: [A-Za-z0-9\-]+)*"
fstring_string_single_line = _compile(
    r"(?:\{\{|\}\}|\\N\{"
    + unicode_character_name
    + r"\}|\\(?:\r\n?|\n)|\\[^\r\nN]|[^{}\r\n\\])+"
)
fstring_string_multi_line = _compile(
    r"(?:\{\{|\}\}|\\N\{" + unicode_character_name + r"\}|\\[^N]|[^{}\\])+"
)

fstring_format_spec_single_line = _compile(r"(?:\\(?:\r\n?|\n)|[^{}\r\n])+")
fstring_format_spec_multi_line = _compile(r"[^{}]+")


def _create_token_collection(  # noqa: C901
    version_info: PythonVersionInfo,
) -> TokenCollection:
    # Note: we use unicode matching for names ("\w") but ascii matching for
    # number literals.
    Whitespace = r"[ \f\t]*"
    Comment = r"#[^\r\n]*"
    # Python 2 is pretty much not working properly anymore, we just ignore
    # parsing unicode properly, which is fine, I guess.
    if version_info.major == 2:
        Name = r"([A-Za-z_0-9]+)"
    elif sys.version_info[0] == 2:
        # Unfortunately the regex engine cannot deal with the regex below, so
        # just use this one.
        Name = r"(\w+)"
    else:
        Name = "([A-Za-z_0-9\u0080-" + MAX_UNICODE + "]+)"

    if version_info >= (3, 6):
        Hexnumber = r"0[xX](?:_?[0-9a-fA-F])+"
        Binnumber = r"0[bB](?:_?[01])+"
        Octnumber = r"0[oO](?:_?[0-7])+"
        Decnumber = r"(?:0(?:_?0)*|[1-9](?:_?[0-9])*)"
        Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
        Exponent = r"[eE][-+]?[0-9](?:_?[0-9])*"
        Pointfloat = group(
            r"[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?", r"\.[0-9](?:_?[0-9])*"
        ) + maybe(Exponent)
        Expfloat = r"[0-9](?:_?[0-9])*" + Exponent
        Floatnumber = group(Pointfloat, Expfloat)
        Imagnumber = group(r"[0-9](?:_?[0-9])*[jJ]", Floatnumber + r"[jJ]")
    else:
        Hexnumber = r"0[xX][0-9a-fA-F]+"
        Binnumber = r"0[bB][01]+"
        if version_info >= (3, 0):
            Octnumber = r"0[oO][0-7]+"
        else:
            Octnumber = "0[oO]?[0-7]+"
        Decnumber = r"(?:0+|[1-9][0-9]*)"
        Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
        if version_info.major < 3:
            Intnumber += "[lL]?"
        Exponent = r"[eE][-+]?[0-9]+"
        Pointfloat = group(r"[0-9]+\.[0-9]*", r"\.[0-9]+") + maybe(Exponent)
        Expfloat = r"[0-9]+" + Exponent
        Floatnumber = group(Pointfloat, Expfloat)
        Imagnumber = group(r"[0-9]+[jJ]", Floatnumber + r"[jJ]")
    Number = group(Imagnumber, Floatnumber, Intnumber)

    # Note that since _all_string_prefixes includes the empty string,
    #  StringPrefix can be the empty string (making it optional).
    possible_prefixes = _all_string_prefixes(version_info)
    StringPrefix = group(*possible_prefixes)
    StringPrefixWithF = group(*_all_string_prefixes(version_info, include_fstring=True))
    fstring_prefixes = _all_string_prefixes(
        version_info, include_fstring=True, only_fstring=True
    )
    FStringStart = group(*fstring_prefixes)

    # Tail end of ' string.
    Single = r"(?:\\.|[^'\\])*'"
    # Tail end of " string.
    Double = r'(?:\\.|[^"\\])*"'
    # Tail end of ''' string.
    Single3 = r"(?:\\.|'(?!'')|[^'\\])*'''"
    # Tail end of """ string.
    Double3 = r'(?:\\.|"(?!"")|[^"\\])*"""'
    Triple = group(StringPrefixWithF + "'''", StringPrefixWithF + '"""')

    # Because of leftmost-then-longest match semantics, be sure to put the
    # longest operators first (e.g., if = came before ==, == would get
    # recognized as two instances of =).
    Operator = group(
        r"\*\*=?", r">>=?", r"<<=?", r"//=?", r"->", r"[+\-*/%&@`|^!=<>]=?", r"~"
    )

    Bracket = "[][(){}]"

    special_args = [r"\r\n?", r"\n", r"[;.,@]"]
    if version_info >= (3, 0):
        special_args.insert(0, r"\.\.\.")
    if version_info >= (3, 8):
        special_args.insert(0, ":=?")
    else:
        special_args.insert(0, ":")
    Special = group(*special_args)

    Funny = group(Operator, Bracket, Special)

    # First (or only) line of ' or " string.
    ContStr = group(
        StringPrefix
        + r"'[^\r\n'\\]*(?:\\.[^\r\n'\\]*)*"
        + group("'", r"\\(?:\r\n?|\n)"),
        StringPrefix
        + r'"[^\r\n"\\]*(?:\\.[^\r\n"\\]*)*'
        + group('"', r"\\(?:\r\n?|\n)"),
    )
    pseudo_extra_pool = [Comment, Triple]
    all_quotes = '"', "'", '"""', "'''"
    if fstring_prefixes:
        pseudo_extra_pool.append(FStringStart + group(*all_quotes))

    PseudoExtras = group(r"\\(?:\r\n?|\n)|\Z", *pseudo_extra_pool)
    PseudoToken = group(Whitespace, capture=True) + group(
        PseudoExtras, Number, Funny, ContStr, Name, capture=True
    )

    # For a given string prefix plus quotes, endpats maps it to a regex
    #  to match the remainder of that string. _prefix can be empty, for
    #  a normal single or triple quoted string (with no prefix).
    endpats = {}
    for _prefix in possible_prefixes:
        endpats[_prefix + "'"] = _compile(Single)
        endpats[_prefix + '"'] = _compile(Double)
        endpats[_prefix + "'''"] = _compile(Single3)
        endpats[_prefix + '"""'] = _compile(Double3)

    # A set of all of the single and triple quoted string prefixes,
    #  including the opening quotes.
    single_quoted = set()
    triple_quoted = set()
    fstring_pattern_map = {}
    for t in possible_prefixes:
        for quote in '"', "'":
            single_quoted.add(t + quote)

        for quote in '"""', "'''":
            triple_quoted.add(t + quote)

    for t in fstring_prefixes:
        for quote in all_quotes:
            fstring_pattern_map[t + quote] = quote

    pseudo_token_compiled = _compile(PseudoToken)
    return TokenCollection(
        pseudo_token_compiled,
        single_quoted,
        triple_quoted,
        endpats,
        _compile(Whitespace),
        fstring_pattern_map,
        {
            ";",
            "import",
            "class",
            "def",
            "try",
            "except",
            "finally",
            "while",
            "with",
            "return",
        },
    )


class Token(namedtuple("Token", ["type", "string", "start_pos", "prefix"])):
    @property
    def end_pos(self):
        lines = split_lines(self.string)
        if len(lines) > 1:
            return self.start_pos[0] + len(lines) - 1, 0
        else:
            return self.start_pos[0], self.start_pos[1] + len(self.string)


class PythonToken(Token):
    def __repr__(self):
        return "TokenInfo(type=%s, string=%r, start_pos=%r, prefix=%r)" % self._replace(
            type=self.type.name
        )


class FStringNode:
    def __init__(self, quote, raw):
        self.quote = quote
        self.raw = raw
        self.parentheses_count = 0
        self.previous_lines = ""
        self.last_string_start_pos = None
        # In the syntax there can be multiple format_spec's nested:
        # {x:{y:3}}
        self.format_spec_count = 0

    def open_parentheses(self, character):
        self.parentheses_count += 1

    def close_parentheses(self, character):
        self.parentheses_count -= 1
        if self.parentheses_count == 0:
            # No parentheses means that the format spec is also finished.
            self.format_spec_count = 0

    def allow_multiline(self):
        return len(self.quote) == 3

    def is_in_expr(self):
        return self.parentheses_count > self.format_spec_count

    def is_in_format_spec(self):
        return not self.is_in_expr() and self.format_spec_count


def _close_fstring_if_necessary(fstring_stack, string, start_pos, additional_prefix):
    for fstring_stack_index, node in enumerate(fstring_stack):
        if string.startswith(node.quote):
            token = PythonToken(
                FSTRING_END, node.quote, start_pos, prefix=additional_prefix
            )
            additional_prefix = ""
            assert not node.previous_lines
            del fstring_stack[fstring_stack_index:]
            return token, "", len(node.quote)
    return None, additional_prefix, 0


def _find_fstring_string(endpats, fstring_stack, line, lnum, pos):
    tos = fstring_stack[-1]
    allow_multiline = tos.allow_multiline()
    if tos.is_in_format_spec():
        if allow_multiline:
            regex = fstring_format_spec_multi_line
        else:
            regex = fstring_format_spec_single_line
    else:
        if tos.raw:
            regex = fstring_raw_string
        elif allow_multiline:
            regex = fstring_string_multi_line
        else:
            regex = fstring_string_single_line

    match = regex.match(line, pos)
    if match is None:
        return tos.previous_lines, pos

    if not tos.previous_lines:
        tos.last_string_start_pos = (lnum, pos)

    string = match.group(0)
    for fstring_stack_node in fstring_stack:
        end_match = endpats[fstring_stack_node.quote].match(string)
        if end_match is not None:
            string = end_match.group(0)[: -len(fstring_stack_node.quote)]

    new_pos = pos
    new_pos += len(string)
    # even if allow_multiline is False, we still need to check for trailing
    # newlines, because a single-line f-string can contain line continuations
    if string.endswith("\n") or string.endswith("\r"):
        tos.previous_lines += string
        string = ""
    else:
        string = tos.previous_lines + string

    return string, new_pos


def tokenize(
    code: str, version_info: PythonVersionInfo, start_pos: Tuple[int, int] = (1, 0)
) -> Generator[PythonToken, None, None]:
    """Generate tokens from a the source code (string)."""
    lines = split_lines(code, keepends=True)
    return tokenize_lines(lines, version_info, start_pos=start_pos)


def tokenize_lines(  # noqa: C901
    lines: Iterable[str],
    version_info: PythonVersionInfo,
    start_pos: Tuple[int, int] = (1, 0),
) -> Generator[PythonToken, None, None]:
    token_collection = _get_token_collection(version_info)
    if version_info >= PythonVersionInfo(3, 7):
        return _tokenize_lines_py37_or_above(
            lines, version_info, token_collection, start_pos=start_pos
        )
    else:
        return _tokenize_lines_py36_or_below(
            lines, version_info, token_collection, start_pos=start_pos
        )


def _tokenize_lines_py36_or_below(  # noqa: C901
    lines: Iterable[str],
    version_info: PythonVersionInfo,
    token_collection: TokenCollection,
    start_pos: Tuple[int, int] = (1, 0),
) -> Generator[PythonToken, None, None]:
    """
    A heavily modified Python standard library tokenizer.

    Additionally to the default information, yields also the prefix of each
    token. This idea comes from lib2to3. The prefix contains all information
    that is irrelevant for the parser like newlines in parentheses or comments.
    """

    paren_level = 0  # count parentheses
    indents = [0]
    max = 0
    numchars = "0123456789"
    contstr = ""
    contline = None
    # We start with a newline. This makes indent at the first position
    # possible. It's not valid Python, but still better than an INDENT in the
    # second line (and not in the first). This makes quite a few things in
    # Jedi's fast parser possible.
    new_line = True
    prefix = ""  # Should never be required, but here for safety
    endprog = None  # Should not be required, but here for lint
    contstr_start: Optional[Tuple[int, int]] = None
    additional_prefix = ""
    first = True
    lnum = start_pos[0] - 1
    fstring_stack = []
    # stash and async_* are used for async/await parsing
    stashed: Optional[PythonToken] = None
    async_def: bool = False
    async_def_indent: int = 0
    async_def_newline: bool = False

    def dedent_if_necessary(start):
        nonlocal stashed
        nonlocal async_def
        nonlocal async_def_indent
        nonlocal async_def_newline

        while start < indents[-1]:
            if start > indents[-2]:
                yield PythonToken(ERROR_DEDENT, "", (lnum, 0), "")
                break
            if stashed is not None:
                yield stashed
                stashed = None
            if async_def and async_def_newline and async_def_indent >= indents[-1]:
                # We exited an 'async def' block, so stop tracking for indents
                async_def = False
                async_def_newline = False
                async_def_indent = 0
            yield PythonToken(DEDENT, "", spos, "")
            indents.pop()

    for line in lines:  # loop over lines in stream
        lnum += 1
        pos = 0
        max = len(line)
        if first:
            if line.startswith(BOM_UTF8_STRING):
                additional_prefix = BOM_UTF8_STRING
                line = line[1:]
                max = len(line)

            # Fake that the part before was already parsed.
            line = "^" * start_pos[1] + line
            pos = start_pos[1]
            max += start_pos[1]

            first = False

        if contstr:  # continued string
            if endprog is None:
                raise Exception("Logic error!")
            endmatch = endprog.match(line)
            if endmatch:
                pos = endmatch.end(0)
                if contstr_start is None:
                    raise Exception("Logic error!")
                if stashed is not None:
                    raise Exception("Logic error!")
                yield PythonToken(STRING, contstr + line[:pos], contstr_start, prefix)
                contstr = ""
                contline = None
            else:
                contstr = contstr + line
                contline = contline + line
                continue

        while pos < max:
            if fstring_stack:
                tos = fstring_stack[-1]
                if not tos.is_in_expr():
                    string, pos = _find_fstring_string(
                        token_collection.endpats, fstring_stack, line, lnum, pos
                    )
                    if string:
                        if stashed is not None:
                            raise Exception("Logic error!")
                        yield PythonToken(
                            FSTRING_STRING,
                            string,
                            tos.last_string_start_pos,
                            # Never has a prefix because it can start anywhere and
                            # include whitespace.
                            prefix="",
                        )
                        tos.previous_lines = ""
                        continue
                    if pos == max:
                        break

                rest = line[pos:]
                (
                    fstring_end_token,
                    additional_prefix,
                    quote_length,
                ) = _close_fstring_if_necessary(
                    fstring_stack, rest, (lnum, pos), additional_prefix
                )
                pos += quote_length
                if fstring_end_token is not None:
                    if stashed is not None:
                        raise Exception("Logic error!")
                    yield fstring_end_token
                    continue

            pseudomatch = token_collection.pseudo_token.match(line, pos)
            if not pseudomatch:  # scan for tokens
                match = token_collection.whitespace.match(line, pos)
                if pos == 0:
                    # pyre-fixme[16]: `Optional` has no attribute `end`.
                    yield from dedent_if_necessary(match.end())
                pos = match.end()
                new_line = False
                yield PythonToken(
                    ERRORTOKEN,
                    line[pos],
                    (lnum, pos),
                    # pyre-fixme[16]: `Optional` has no attribute `group`.
                    additional_prefix + match.group(0),
                )
                additional_prefix = ""
                pos += 1
                continue

            prefix = additional_prefix + pseudomatch.group(1)
            additional_prefix = ""
            start, pos = pseudomatch.span(2)
            spos = (lnum, start)
            token = pseudomatch.group(2)
            if token == "":
                assert prefix
                additional_prefix = prefix
                # This means that we have a line with whitespace/comments at
                # the end, which just results in an endmarker.
                break
            initial = token[0]

            if new_line and initial not in "\r\n\\#":
                new_line = False
                if paren_level == 0 and not fstring_stack:
                    i = 0
                    indent_start = start
                    while line[i] == "\f":
                        i += 1
                        # TODO don't we need to change spos as well?
                        indent_start -= 1
                    if indent_start > indents[-1]:
                        if stashed is not None:
                            yield stashed
                            stashed = None
                        yield PythonToken(INDENT, "", spos, "")
                        indents.append(indent_start)
                    yield from dedent_if_necessary(indent_start)

            if initial in numchars or (  # ordinary number
                initial == "." and token != "." and token != "..."
            ):
                if stashed is not None:
                    yield stashed
                    stashed = None
                yield PythonToken(NUMBER, token, spos, prefix)
            elif pseudomatch.group(3) is not None:  # ordinary name
                if token in token_collection.always_break_tokens:
                    fstring_stack[:] = []
                    paren_level = 0
                    # We only want to dedent if the token is on a new line.
                    if re.match(r"[ \f\t]*$", line[:start]):
                        while True:
                            indent = indents.pop()
                            if indent > start:
                                if (
                                    async_def
                                    and async_def_newline
                                    and async_def_indent >= indent
                                ):
                                    # We dedented outside of an 'async def' block.
                                    async_def = False
                                    async_def_newline = False
                                    async_def_indent = 0
                                if stashed is not None:
                                    yield stashed
                                    stashed = None
                                yield PythonToken(DEDENT, "", spos, "")
                            else:
                                indents.append(indent)
                                break
                if str.isidentifier(token):
                    should_yield_identifier = True
                    if token in ("async", "await") and async_def:
                        # We're inside an 'async def' block, all async/await are
                        # tokens.
                        if token == "async":
                            yield PythonToken(ASYNC, token, spos, prefix)
                        else:
                            yield PythonToken(AWAIT, token, spos, prefix)
                        should_yield_identifier = False

                    # We are possibly starting an 'async def' section
                    elif token == "async" and not stashed:
                        stashed = PythonToken(NAME, token, spos, prefix)
                        should_yield_identifier = False

                    # We actually are starting an 'async def' section
                    elif (
                        token == "def"
                        and stashed is not None
                        and stashed[0] is NAME
                        and stashed[1] == "async"
                    ):
                        async_def = True
                        async_def_indent = indents[-1]
                        yield PythonToken(ASYNC, stashed[1], stashed[2], stashed[3])
                        stashed = None

                    # We are either not stashed, or we output an ASYNC token above.
                    elif stashed:
                        yield stashed
                        stashed = None

                    # If we didn't bail early due to possibly recognizing an 'async def',
                    # then we should yield this token as normal.
                    if should_yield_identifier:
                        yield PythonToken(NAME, token, spos, prefix)
                else:
                    yield from _split_illegal_unicode_name(token, spos, prefix)
            elif initial in "\r\n":
                if any(not f.allow_multiline() for f in fstring_stack):
                    # Would use fstring_stack.clear, but that's not available
                    # in Python 2.
                    fstring_stack[:] = []

                if not new_line and paren_level == 0 and not fstring_stack:
                    if async_def:
                        async_def_newline = True
                    if stashed:
                        yield stashed
                        stashed = None
                    yield PythonToken(NEWLINE, token, spos, prefix)
                else:
                    additional_prefix = prefix + token
                new_line = True
            elif initial == "#":  # Comments
                assert not token.endswith("\n")
                additional_prefix = prefix + token
            elif token in token_collection.triple_quoted:
                endprog = token_collection.endpats[token]
                endmatch = endprog.match(line, pos)
                if endmatch:  # all on one line
                    pos = endmatch.end(0)
                    token = line[start:pos]
                    if stashed is not None:
                        yield stashed
                        stashed = None
                    yield PythonToken(STRING, token, spos, prefix)
                else:
                    contstr_start = (lnum, start)  # multiple lines
                    contstr = line[start:]
                    contline = line
                    break

            # Check up to the first 3 chars of the token to see if
            #  they're in the single_quoted set. If so, they start
            #  a string.
            # We're using the first 3, because we're looking for
            #  "rb'" (for example) at the start of the token. If
            #  we switch to longer prefixes, this needs to be
            #  adjusted.
            # Note that initial == token[:1].
            # Also note that single quote checking must come after
            #  triple quote checking (above).
            elif (
                initial in token_collection.single_quoted
                or token[:2] in token_collection.single_quoted
                or token[:3] in token_collection.single_quoted
            ):
                if token[-1] in "\r\n":  # continued string
                    # This means that a single quoted string ends with a
                    # backslash and is continued.
                    contstr_start = lnum, start
                    endprog = (
                        token_collection.endpats.get(initial)
                        or token_collection.endpats.get(token[1])
                        or token_collection.endpats.get(token[2])
                    )
                    contstr = line[start:]
                    contline = line
                    break
                else:  # ordinary string
                    if stashed is not None:
                        yield stashed
                        stashed = None
                    yield PythonToken(STRING, token, spos, prefix)
            elif (
                token in token_collection.fstring_pattern_map
            ):  # The start of an fstring.
                fstring_stack.append(
                    FStringNode(
                        token_collection.fstring_pattern_map[token],
                        "r" in token or "R" in token,
                    )
                )
                if stashed is not None:
                    yield stashed
                    stashed = None
                yield PythonToken(FSTRING_START, token, spos, prefix)
            elif initial == "\\" and line[start:] in (
                "\\\n",
                "\\\r\n",
                "\\\r",
            ):  # continued stmt
                additional_prefix += prefix + line[start:]
                break
            else:
                if token in "([{":
                    if fstring_stack:
                        fstring_stack[-1].open_parentheses(token)
                    else:
                        paren_level += 1
                elif token in ")]}":
                    if fstring_stack:
                        fstring_stack[-1].close_parentheses(token)
                    else:
                        if paren_level:
                            paren_level -= 1
                elif (
                    token == ":"
                    and fstring_stack
                    and fstring_stack[-1].parentheses_count
                    - fstring_stack[-1].format_spec_count
                    == 1
                ):
                    fstring_stack[-1].format_spec_count += 1

                if stashed is not None:
                    yield stashed
                    stashed = None
                yield PythonToken(OP, token, spos, prefix)

    if contstr:
        yield PythonToken(ERRORTOKEN, contstr, contstr_start, prefix)
        if contstr.endswith("\n") or contstr.endswith("\r"):
            new_line = True

    if stashed is not None:
        yield stashed
        stashed = None

    end_pos = lnum, max
    # As the last position we just take the maximally possible position. We
    # remove -1 for the last new line.
    for indent in indents[1:]:
        yield PythonToken(DEDENT, "", end_pos, "")
    yield PythonToken(ENDMARKER, "", end_pos, additional_prefix)


def _tokenize_lines_py37_or_above(  # noqa: C901
    lines: Iterable[str],
    version_info: PythonVersionInfo,
    token_collection: TokenCollection,
    start_pos: Tuple[int, int] = (1, 0),
) -> Generator[PythonToken, None, None]:
    """
    A heavily modified Python standard library tokenizer.

    Additionally to the default information, yields also the prefix of each
    token. This idea comes from lib2to3. The prefix contains all information
    that is irrelevant for the parser like newlines in parentheses or comments.
    """

    def dedent_if_necessary(start):
        while start < indents[-1]:
            if start > indents[-2]:
                yield PythonToken(ERROR_DEDENT, "", (lnum, 0), "")
                break
            yield PythonToken(DEDENT, "", spos, "")
            indents.pop()

    paren_level = 0  # count parentheses
    indents = [0]
    max = 0
    numchars = "0123456789"
    contstr = ""
    contline = None
    # We start with a newline. This makes indent at the first position
    # possible. It's not valid Python, but still better than an INDENT in the
    # second line (and not in the first). This makes quite a few things in
    # Jedi's fast parser possible.
    new_line = True
    prefix = ""  # Should never be required, but here for safety
    endprog = None  # Should not be required, but here for lint
    contstr_start: Optional[Tuple[int, int]] = None
    additional_prefix = ""
    first = True
    lnum = start_pos[0] - 1
    fstring_stack = []
    for line in lines:  # loop over lines in stream
        lnum += 1
        pos = 0
        max = len(line)
        if first:
            if line.startswith(BOM_UTF8_STRING):
                additional_prefix = BOM_UTF8_STRING
                line = line[1:]
                max = len(line)

            # Fake that the part before was already parsed.
            line = "^" * start_pos[1] + line
            pos = start_pos[1]
            max += start_pos[1]

            first = False

        if contstr:  # continued string
            if endprog is None:
                raise Exception("Logic error!")
            endmatch = endprog.match(line)
            if endmatch:
                pos = endmatch.end(0)
                if contstr_start is None:
                    raise Exception("Logic error!")
                yield PythonToken(STRING, contstr + line[:pos], contstr_start, prefix)
                contstr = ""
                contline = None
            else:
                contstr = contstr + line
                contline = contline + line
                continue

        while pos < max:
            if fstring_stack:
                tos = fstring_stack[-1]
                if not tos.is_in_expr():
                    string, pos = _find_fstring_string(
                        token_collection.endpats, fstring_stack, line, lnum, pos
                    )
                    if string:
                        yield PythonToken(
                            FSTRING_STRING,
                            string,
                            tos.last_string_start_pos,
                            # Never has a prefix because it can start anywhere and
                            # include whitespace.
                            prefix="",
                        )
                        tos.previous_lines = ""
                        continue
                    if pos == max:
                        break

                rest = line[pos:]
                (
                    fstring_end_token,
                    additional_prefix,
                    quote_length,
                ) = _close_fstring_if_necessary(
                    fstring_stack, rest, (lnum, pos), additional_prefix
                )
                pos += quote_length
                if fstring_end_token is not None:
                    yield fstring_end_token
                    continue

            pseudomatch = token_collection.pseudo_token.match(line, pos)
            if not pseudomatch:  # scan for tokens
                match = token_collection.whitespace.match(line, pos)
                if pos == 0:
                    # pyre-fixme[16]: `Optional` has no attribute `end`.
                    for t in dedent_if_necessary(match.end()):
                        yield t
                pos = match.end()
                new_line = False
                yield PythonToken(
                    ERRORTOKEN,
                    line[pos],
                    (lnum, pos),
                    # pyre-fixme[16]: `Optional` has no attribute `group`.
                    additional_prefix + match.group(0),
                )
                additional_prefix = ""
                pos += 1
                continue

            prefix = additional_prefix + pseudomatch.group(1)
            additional_prefix = ""
            start, pos = pseudomatch.span(2)
            spos = (lnum, start)
            token = pseudomatch.group(2)
            if token == "":
                assert prefix
                additional_prefix = prefix
                # This means that we have a line with whitespace/comments at
                # the end, which just results in an endmarker.
                break
            initial = token[0]

            if new_line and initial not in "\r\n\\#":
                new_line = False
                if paren_level == 0 and not fstring_stack:
                    i = 0
                    indent_start = start
                    while line[i] == "\f":
                        i += 1
                        # TODO don't we need to change spos as well?
                        indent_start -= 1
                    if indent_start > indents[-1]:
                        yield PythonToken(INDENT, "", spos, "")
                        indents.append(indent_start)
                    for t in dedent_if_necessary(indent_start):
                        yield t

            if initial in numchars or (  # ordinary number
                initial == "." and token != "." and token != "..."
            ):
                yield PythonToken(NUMBER, token, spos, prefix)
            elif pseudomatch.group(3) is not None:  # ordinary name
                if token in token_collection.always_break_tokens:
                    fstring_stack[:] = []
                    paren_level = 0
                    # We only want to dedent if the token is on a new line.
                    if re.match(r"[ \f\t]*$", line[:start]):
                        while True:
                            indent = indents.pop()
                            if indent > start:
                                yield PythonToken(DEDENT, "", spos, "")
                            else:
                                indents.append(indent)
                                break
                if str.isidentifier(token):
                    # py37 doesn't need special tokens for async/await, and we could
                    # emit NAME, but then we'd need different grammar for py36 and py37.
                    if token == "async":
                        yield PythonToken(ASYNC, token, spos, prefix)
                    elif token == "await":
                        yield PythonToken(AWAIT, token, spos, prefix)
                    else:
                        yield PythonToken(NAME, token, spos, prefix)
                else:
                    for t in _split_illegal_unicode_name(token, spos, prefix):
                        yield t  # yield from Python 2
            elif initial in "\r\n":
                if any(not f.allow_multiline() for f in fstring_stack):
                    # Would use fstring_stack.clear, but that's not available
                    # in Python 2.
                    fstring_stack[:] = []

                if not new_line and paren_level == 0 and not fstring_stack:
                    yield PythonToken(NEWLINE, token, spos, prefix)
                else:
                    additional_prefix = prefix + token
                new_line = True
            elif initial == "#":  # Comments
                assert not token.endswith("\n")
                additional_prefix = prefix + token
            elif token in token_collection.triple_quoted:
                endprog = token_collection.endpats[token]
                endmatch = endprog.match(line, pos)
                if endmatch:  # all on one line
                    pos = endmatch.end(0)
                    token = line[start:pos]
                    yield PythonToken(STRING, token, spos, prefix)
                else:
                    contstr_start = (lnum, start)  # multiple lines
                    contstr = line[start:]
                    contline = line
                    break

            # Check up to the first 3 chars of the token to see if
            #  they're in the single_quoted set. If so, they start
            #  a string.
            # We're using the first 3, because we're looking for
            #  "rb'" (for example) at the start of the token. If
            #  we switch to longer prefixes, this needs to be
            #  adjusted.
            # Note that initial == token[:1].
            # Also note that single quote checking must come after
            #  triple quote checking (above).
            elif (
                initial in token_collection.single_quoted
                or token[:2] in token_collection.single_quoted
                or token[:3] in token_collection.single_quoted
            ):
                if token[-1] in "\r\n":  # continued string
                    # This means that a single quoted string ends with a
                    # backslash and is continued.
                    contstr_start = lnum, start
                    endprog = (
                        token_collection.endpats.get(initial)
                        or token_collection.endpats.get(token[1])
                        or token_collection.endpats.get(token[2])
                    )
                    contstr = line[start:]
                    contline = line
                    break
                else:  # ordinary string
                    yield PythonToken(STRING, token, spos, prefix)
            elif (
                token in token_collection.fstring_pattern_map
            ):  # The start of an fstring.
                fstring_stack.append(
                    FStringNode(
                        token_collection.fstring_pattern_map[token],
                        "r" in token or "R" in token,
                    )
                )
                yield PythonToken(FSTRING_START, token, spos, prefix)
            elif initial == "\\" and line[start:] in (
                "\\\n",
                "\\\r\n",
                "\\\r",
            ):  # continued stmt
                additional_prefix += prefix + line[start:]
                break
            else:
                if token in "([{":
                    if fstring_stack:
                        fstring_stack[-1].open_parentheses(token)
                    else:
                        paren_level += 1
                elif token in ")]}":
                    if fstring_stack:
                        fstring_stack[-1].close_parentheses(token)
                    else:
                        if paren_level:
                            paren_level -= 1
                elif (
                    token == ":"
                    and fstring_stack
                    and fstring_stack[-1].parentheses_count
                    - fstring_stack[-1].format_spec_count
                    == 1
                ):
                    fstring_stack[-1].format_spec_count += 1

                yield PythonToken(OP, token, spos, prefix)

    if contstr:
        yield PythonToken(ERRORTOKEN, contstr, contstr_start, prefix)
        if contstr.endswith("\n") or contstr.endswith("\r"):
            new_line = True

    end_pos = lnum, max
    # As the last position we just take the maximally possible position. We
    # remove -1 for the last new line.
    for indent in indents[1:]:
        yield PythonToken(DEDENT, "", end_pos, "")
    yield PythonToken(ENDMARKER, "", end_pos, additional_prefix)


def _split_illegal_unicode_name(
    token: str, start_pos: Tuple[int, int], prefix: str
) -> Generator[PythonToken, None, None]:
    def create_token():
        return PythonToken(ERRORTOKEN if is_illegal else NAME, found, pos, prefix)

    found = ""
    is_illegal = False
    pos = start_pos
    for i, char in enumerate(token):
        if is_illegal:
            if str.isidentifier(char):
                yield create_token()
                found = char
                is_illegal = False
                prefix = ""
                pos = start_pos[0], start_pos[1] + i
            else:
                found += char
        else:
            new_found = found + char
            if str.isidentifier(new_found):
                found = new_found
            else:
                if found:
                    yield create_token()
                    prefix = ""
                    pos = start_pos[0], start_pos[1] + i
                found = char
                is_illegal = True

    if found:
        yield create_token()
