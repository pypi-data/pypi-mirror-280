# SPDX-FileCopyrightText: 2022 Copyright DB InfraGO AG and the capellambse-context-diagrams contributors
# SPDX-License-Identifier: Apache-2.0

"""The Context Diagrams model extension.

This extension adds a new property to many model elements called
`context_diagram`, which allows access automatically generated diagrams
of an element's "context".

The context of an element is defined as the collection of the element
itself, its ports, the exchanges that flow into or out of the ports, as
well as the ports on the other side of the exchange and the ports'
direct parent elements.

The element of interest uses the regular styling (configurable via
function), other elements use a white background color to distinguish
them.
"""
from __future__ import annotations

import collections.abc as cabc
import logging
import typing as t
from importlib import metadata

from capellambse.diagram import COLORS, CSSdef, capstyle
from capellambse.model import common
from capellambse.model.crosslayer import fa, information
from capellambse.model.layers import ctx, la, oa, pa
from capellambse.model.modeltypes import DiagramType
from capellambse.svg import decorations

from . import _elkjs, context, styling

try:
    __version__ = metadata.version("capellambse-context-diagrams")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0+unknown"
del metadata

DefaultRenderParams = dict[str, t.Any]
SupportedClass = tuple[
    type[common.GenericElement], DiagramType, DefaultRenderParams
]
logger = logging.getLogger(__name__)

ATTR_NAME = "context_diagram"


def install_elk() -> None:
    """Install elk.js and its dependencies into the local cache directory.

    When rendering a context diagram, elk.js will be installed
    automatically into a persistent local cache directory. This function
    may be called while building a container, starting a server or
    similar tasks in order to prepare the elk.js execution environment
    ahead of time.
    """
    _elkjs._install_required_npm_pkg_versions()


def init() -> None:
    """Initialize the extension."""
    register_classes()
    register_interface_context()
    register_tree_view()
    register_realization_view()
    register_data_flow_view()
    # register_functional_context() XXX: Future


def register_classes() -> None:
    """Add the `context_diagram` property to the relevant model objects."""
    supported_classes: list[SupportedClass] = [
        (oa.Entity, DiagramType.OAB, {}),
        (
            oa.OperationalActivity,
            DiagramType.OAB,
            {"display_parent_relation": True},
        ),
        (oa.OperationalCapability, DiagramType.OCB, {}),
        (ctx.Mission, DiagramType.MCB, {}),
        (ctx.Capability, DiagramType.MCB, {"display_symbols_as_boxes": False}),
        (
            ctx.SystemComponent,
            DiagramType.SAB,
            {
                "display_symbols_as_boxes": True,
                "display_parent_relation": True,
                "render_styles": styling.BLUE_ACTOR_FNCS,
            },
        ),
        (
            ctx.SystemFunction,
            DiagramType.SAB,
            {
                "display_symbols_as_boxes": True,
                "display_parent_relation": True,
                "render_styles": styling.BLUE_ACTOR_FNCS,
            },
        ),
        (
            la.LogicalComponent,
            DiagramType.LAB,
            {
                "display_symbols_as_boxes": True,
                "display_parent_relation": True,
                "render_styles": styling.BLUE_ACTOR_FNCS,
            },
        ),
        (
            la.LogicalFunction,
            DiagramType.LAB,
            {
                "display_symbols_as_boxes": True,
                "display_parent_relation": True,
                "render_styles": styling.BLUE_ACTOR_FNCS,
            },
        ),
        (
            pa.PhysicalComponent,
            DiagramType.PAB,
            {
                "display_parent_relation": True,
            },
        ),
        (
            pa.PhysicalFunction,
            DiagramType.PAB,
            {
                "display_parent_relation": True,
            },
        ),
    ]
    patch_styles(supported_classes)
    class_: type[common.GenericElement]
    for class_, dgcls, default_render_params in supported_classes:
        accessor = context.ContextAccessor(dgcls.value, default_render_params)
        common.set_accessor(class_, ATTR_NAME, accessor)


def patch_styles(classes: cabc.Iterable[SupportedClass]) -> None:
    """Add missing default styling to default styles.

    See Also
    --------
    [capstyle.get_style][capellambse.aird.capstyle.get_style] : Default
        style getter.
    """
    cap: dict[str, CSSdef] = {
        "fill": [COLORS["_CAP_Entity_Gray_min"], COLORS["_CAP_Entity_Gray"]],
        "stroke": COLORS["dark_gray"],
        "text_fill": COLORS["black"],
    }
    capstyle.STYLES["Missions Capabilities Blank"].update(
        {"Box.Capability": cap, "Box.Mission": cap}
    )
    capstyle.STYLES["Operational Capabilities Blank"][
        "Box.OperationalCapability"
    ] = cap
    circle_style = {"fill": COLORS["_CAP_xAB_Function_Border_Green"]}
    for _, dt, _ in classes:
        capstyle.STYLES[dt.value]["Circle.FunctionalExchange"] = circle_style


def register_interface_context() -> None:
    """Add the `context_diagram` property to interface model objects."""
    common.set_accessor(
        oa.CommunicationMean,
        ATTR_NAME,
        context.InterfaceContextAccessor(
            {
                oa.EntityPkg: DiagramType.OAB.value,
                oa.Entity: DiagramType.OAB.value,
            }
        ),
    )
    common.set_accessor(
        fa.ComponentExchange,
        ATTR_NAME,
        context.InterfaceContextAccessor(
            {
                ctx.SystemComponentPkg: DiagramType.SAB.value,
                ctx.SystemComponent: DiagramType.SAB.value,
                la.LogicalComponentPkg: DiagramType.LAB.value,
                la.LogicalComponent: DiagramType.LAB.value,
                pa.PhysicalComponentPkg: DiagramType.PAB.value,
                pa.PhysicalComponent: DiagramType.PAB.value,
            },
        ),
    )


def register_functional_context() -> None:
    """Add the `functional_context_diagram` attribute to `ModelObject`s.

    !!! bug "Full of bugs"

        The functional context diagrams will be available soon.
    """
    attr_name = f"functional_{ATTR_NAME}"
    supported_classes: list[
        tuple[type[common.GenericElement], DiagramType]
    ] = [
        (oa.Entity, DiagramType.OAB),
        (ctx.SystemComponent, DiagramType.SAB),
        (la.LogicalComponent, DiagramType.LAB),
        (pa.PhysicalComponent, DiagramType.PAB),
    ]
    class_: type[common.GenericElement]
    for class_, dgcls in supported_classes:
        common.set_accessor(
            class_,
            attr_name,
            context.FunctionalContextAccessor(dgcls.value),
        )


def register_tree_view() -> None:
    """Add the ``tree_view`` attribute to ``Class``es."""
    common.set_accessor(
        information.Class,
        "tree_view",
        context.ClassTreeAccessor(DiagramType.CDB.value),
    )


def register_realization_view() -> None:
    """Add the ``realization_view`` attribute to various objects.

    Adds ``realization_view`` to Activities, Functions and Components
    of all layers.
    """
    supported_classes: list[SupportedClass] = [
        (oa.Entity, DiagramType.OAB, {}),
        (oa.OperationalActivity, DiagramType.OAIB, {}),
        (ctx.SystemComponent, DiagramType.SAB, {}),
        (ctx.SystemFunction, DiagramType.SDFB, {}),
        (la.LogicalComponent, DiagramType.LAB, {}),
        (la.LogicalFunction, DiagramType.LDFB, {}),
        (pa.PhysicalComponent, DiagramType.PAB, {}),
        (pa.PhysicalFunction, DiagramType.PDFB, {}),
    ]
    styles: dict[str, dict[str, capstyle.CSSdef]] = {}
    for class_, dgcls, _ in supported_classes:
        common.set_accessor(
            class_,
            "realization_view",
            context.RealizationViewContextAccessor("RealizationView Diagram"),
        )
        styles.update(capstyle.STYLES.get(dgcls.value, {}))

    capstyle.STYLES["RealizationView Diagram"] = styles
    capstyle.STYLES["RealizationView Diagram"].update(
        capstyle.STYLES["__GLOBAL__"]
    )
    capstyle.STYLES["RealizationView Diagram"]["Edge.Realization"] = {
        "stroke": capstyle.COLORS["dark_gray"],
        "marker-end": "FineArrowMark",
        "stroke-dasharray": "5",
    }


def register_data_flow_view() -> None:
    supported_classes: list[SupportedClass] = [
        (oa.OperationalCapability, DiagramType.OAIB, {}),  # portless
        (ctx.Capability, DiagramType.SDFB, {}),  # default
    ]
    class_: type[common.GenericElement]
    for class_, dgcls, default_render_params in supported_classes:
        accessor = context.DataFlowAccessor(dgcls.value, default_render_params)
        common.set_accessor(class_, "data_flow_view", accessor)
