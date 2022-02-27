#     Copyright 2021, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Reformulation of boolean and/or expressions.

Consult the Developer Manual for information. TODO: Add ability to sync
source code comments with Developer Manual sections.

"""

from nuitka.nodes.ConditionalNodes import (
    ExpressionConditionalAnd,
    ExpressionConditionalOr,
    makeNotExpression,
)

from .TreeHelpers import buildNode, buildNodeList, getKind


def buildBoolOpNode(provider, node, source_ref):
    bool_op = getKind(node.op)

    if bool_op == "Or":
        # The "or" may be short circuit and is therefore not a plain operation.
        values = buildNodeList(provider, node.values, source_ref)

        for value in values[:-1]:
            value.setCompatibleSourceReference(values[-1].getSourceReference())

        source_ref = values[-1].getSourceReference()

        return makeOrNode(values=values, source_ref=source_ref)

    elif bool_op == "And":
        # The "and" may be short circuit and is therefore not a plain operation.
        values = buildNodeList(provider, node.values, source_ref)

        for value in values[:-1]:
            value.setCompatibleSourceReference(values[-1].getSourceReference())

        source_ref = values[-1].getSourceReference()

        return makeAndNode(values=values, source_ref=source_ref)
    elif bool_op == "Not":
        # The "not" is really only a unary operation and no special.
        return makeNotExpression(
            expression=buildNode(provider, node.operand, source_ref)
        )
    else:
        assert False, bool_op


def makeOrNode(values, source_ref):
    values = list(values)

    result = values.pop()

    # When we encounter, "or", we expect it to be at least two values.
    assert values

    while values:
        result = ExpressionConditionalOr(
            left=values.pop(), right=result, source_ref=source_ref
        )

    return result


def makeAndNode(values, source_ref):
    values = list(values)

    result = values.pop()

    # Unlike "or", for "and", this is used with only one value.

    while values:
        result = ExpressionConditionalAnd(
            left=values.pop(), right=result, source_ref=source_ref
        )

    return result
