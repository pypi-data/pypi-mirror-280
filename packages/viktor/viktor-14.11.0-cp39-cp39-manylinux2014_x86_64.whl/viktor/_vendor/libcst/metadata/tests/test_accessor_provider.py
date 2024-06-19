# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import dataclasses

from textwrap import dedent

import viktor._vendor.libcst as cst
from viktor._vendor.libcst.metadata import AccessorProvider, MetadataWrapper
from viktor._vendor.libcst.testing.utils import data_provider, UnitTest


class DependentVisitor(cst.CSTVisitor):
    METADATA_DEPENDENCIES = (AccessorProvider,)

    def __init__(self, *, test: UnitTest) -> None:
        self.test = test

    def on_visit(self, node: cst.CSTNode) -> bool:
        for f in dataclasses.fields(node):
            child = getattr(node, f.name)
            if type(child) is cst.CSTNode:
                accessor = self.get_metadata(AccessorProvider, child)
                self.test.assertEqual(accessor, f.name)

        return True


class AccessorProviderTest(UnitTest):
    @data_provider(
        (
            (
                """
                foo = 'toplevel'
                fn1(foo)
                fn2(foo)
                def fn_def():
                    foo = 'shadow'
                    fn3(foo)
                """,
            ),
            (
                """
                global_var = None
                @cls_attr
                class Cls(cls_attr, kwarg=cls_attr):
                    cls_attr = 5
                    def f():
                        pass
                """,
            ),
            (
                """
                iterator = None
                condition = None
                [elt for target in iterator if condition]
                {elt for target in iterator if condition}
                {elt: target for target in iterator if condition}
                (elt for target in iterator if condition)
                """,
            ),
        )
    )
    def test_accessor_provier(self, code: str) -> None:
        wrapper = MetadataWrapper(cst.parse_module(dedent(code)))
        wrapper.visit(DependentVisitor(test=self))
