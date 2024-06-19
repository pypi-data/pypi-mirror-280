# SPDX-FileCopyrightText: 2022 Copyright DB InfraGO AG and the capellambse-context-diagrams contributors
# SPDX-License-Identifier: Apache-2.0
"""
Functionality for collection of model data from an instance of [`MelodyModel`][capellambse.model.MelodyModel]
and conversion of it into [`_elkjs.ELKInputData`][capellambse_context_diagrams._elkjs.ELKInputData].
"""

from __future__ import annotations

import collections.abc as cabc
import logging
import typing as t

from capellambse.model import common, layers
from capellambse.model.crosslayer import interaction
from capellambse.model.modeltypes import DiagramType as DT

from .. import _elkjs, context, filters
from . import makers

logger = logging.getLogger(__name__)

SourceAndTarget = tuple[common.GenericElement, common.GenericElement]

PHYSICAL_CONNECTOR_ATTR_NAMES = {"physical_ports"}
"""Attribute of PhysicalComponents for receiving connections."""
CONNECTOR_ATTR_NAMES = {"ports", "inputs", "outputs"}
"""Attribute of GenericElements for receiving connections."""
DIAGRAM_TYPE_TO_CONNECTOR_NAMES: dict[DT, set[str]] = {
    DT.OAB: set(),
    DT.OAIB: set(),
    DT.OCB: set(),
    DT.MCB: set(),
    DT.SAB: CONNECTOR_ATTR_NAMES,
    DT.SDFB: CONNECTOR_ATTR_NAMES,
    DT.LAB: CONNECTOR_ATTR_NAMES,
    DT.LDFB: CONNECTOR_ATTR_NAMES,
    DT.PAB: CONNECTOR_ATTR_NAMES | PHYSICAL_CONNECTOR_ATTR_NAMES,
    DT.PDFB: CONNECTOR_ATTR_NAMES | PHYSICAL_CONNECTOR_ATTR_NAMES,
}
"""Supported diagram types mapping to the attribute name of connectors."""
MARKER_SIZE = 3
"""Default size of marker-ends in pixels."""
MARKER_PADDING = makers.PORT_PADDING
"""Default padding of markers in pixels."""
PackageTypes: tuple[type[common.GenericElement], ...] = (
    layers.oa.EntityPkg,
    layers.la.LogicalComponentPkg,
    layers.ctx.SystemComponentPkg,
    layers.pa.PhysicalComponentPkg,
)


def collector(
    diagram: context.ContextDiagram,
    *,
    width: int | float = makers.EOI_WIDTH,
    no_symbol: bool = False,
) -> _elkjs.ELKInputData:
    """Returns ``ELKInputData`` with only centerbox in children and config."""
    data = makers.make_diagram(diagram)
    data.children = [
        makers.make_box(
            diagram.target,
            width=width,
            no_symbol=no_symbol,
            slim_width=diagram.slim_center_box,
        )
    ]
    return data


def collect_exchange_endpoints(
    ex: ExchangeData | common.GenericElement,
) -> SourceAndTarget:
    """Safely collect exchange endpoints from ``ex``."""
    if isinstance(ex, ExchangeData):
        if ex.is_hierarchical:
            return ex.exchange.target, ex.exchange.source
        return ex.exchange.source, ex.exchange.target
    return ex.source, ex.target


class ExchangeData(t.NamedTuple):
    """Exchange data for ELK."""

    exchange: common.GenericElement
    """An exchange from the capellambse model."""
    elkdata: _elkjs.ELKInputData
    """The collected elkdata to add the edges in there."""
    filter_iterable: cabc.Iterable[str]
    """
    A string that maps to a filter label adjuster
    callable in
    [`FILTER_LABEL_ADJUSTERS`][capellambse_context_diagrams.filters.FILTER_LABEL_ADJUSTERS].
    """
    params: dict[str, t.Any] | None = None
    """Optional dictionary of additional render params."""
    is_hierarchical: bool = False
    """True if exchange isn't global, i.e. nested inside a box."""


def exchange_data_collector(
    data: ExchangeData,
    endpoint_collector: cabc.Callable[
        [common.GenericElement], SourceAndTarget
    ] = collect_exchange_endpoints,
) -> SourceAndTarget:
    """Return source and target port from `exchange`.

    Additionally inflate `elkdata.children` with input data for ELK.
    You can handover a filter name that corresponds to capellambse
    filters. This will apply filter functionality from
    [`filters.FILTER_LABEL_ADJUSTERS`][capellambse_context_diagrams.filters.FILTER_LABEL_ADJUSTERS].

    Parameters
    ----------
    data
        Instance of [`ExchangeData`][capellambse_context_diagrams.collectors.generic.ExchangeData]
        storing all needed elements for collection.
    endpoint_collector
        Optional collector function for Exchange endpoints. Defaults to
        [`collect_exchange_endpoints`][capellambse_context_diagrams.collectors.generic.collect_exchange_endpoints].

    Returns
    -------
    source, target
        A tuple consisting of the exchange's source and target elements.
    """
    source, target = endpoint_collector(data.exchange)
    if data.is_hierarchical:
        target, source = source, target

    params = (data.params or {}).copy()
    # Remove simple render parameters from params
    no_edgelabels: bool = params.pop("no_edgelabels", False)
    params.pop("transparent_background", False)
    _ = params.pop("font_family", "Open Sans")
    _ = params.pop("font_size", 12)

    render_adj: dict[str, t.Any] = {}
    for name, value in params.items():
        try:
            filters.RENDER_ADJUSTERS[name](value, data.exchange, render_adj)
        except KeyError:
            logger.exception(
                "There is no render parameter solver labelled: '%s' "
                "in filters.RENDER_ADJUSTERS",
                name,
            )

    data.elkdata.edges.append(
        _elkjs.ELKInputEdge(
            id=render_adj.get("id", data.exchange.uuid),
            sources=[render_adj.get("sources", source.uuid)],
            targets=[render_adj.get("targets", target.uuid)],
        )
    )

    label = collect_label(data.exchange)
    for filter in data.filter_iterable:
        try:
            label = filters.FILTER_LABEL_ADJUSTERS[filter](
                data.exchange, label
            )
        except KeyError:
            logger.exception(
                "There is no filter labelled: '%s' in "
                "filters.FILTER_LABEL_ADJUSTERS",
                filter,
            )

    if label and not no_edgelabels:
        data.elkdata.edges[-1].labels = makers.make_label(
            render_adj.get("labels_text", label),
            max_width=makers.MAX_LABEL_WIDTH,
        )

    return source, target


def collect_label(obj: common.GenericElement) -> str | None:
    """Return the label of a given object.

    The label usually comes from the `.name` attribute. Special handling
    for [`interaction.AbstractCapabilityExtend`][capellambse.model.crosslayer.interaction.AbstractCapabilityExtend]
    and [interaction.AbstractCapabilityInclude`][capellambse.model.crosslayer.interaction.AbstractCapabilityInclude].
    """
    if isinstance(obj, interaction.AbstractCapabilityExtend):
        return "« e »"
    elif isinstance(obj, interaction.AbstractCapabilityInclude):
        return "« i »"
    return "" if obj.name.startswith("(Unnamed") else obj.name


def move_parent_boxes_to_owner(
    boxes: dict[str, _elkjs.ELKInputChild],
    obj: common.GenericElement,
    data: _elkjs.ELKInputData,
    filter_types: tuple[type, ...] = PackageTypes,
) -> None:
    """Move boxes to their owner box."""
    boxes_to_remove: list[str] = []
    for child in data.children:
        if not child.children:
            continue

        owner = obj._model.by_uuid(child.id)
        if (
            isinstance(owner, filter_types)
            or not (oowner := owner.owner)
            or isinstance(oowner, filter_types)
            or not (oowner_box := boxes.get(oowner.uuid))
        ):
            continue

        oowner_box.children.append(child)
        boxes_to_remove.append(child.id)

    data.children = [b for b in data.children if b.id not in boxes_to_remove]


def move_edges(
    boxes: dict[str, _elkjs.ELKInputChild],
    connections: list[common.GenericElement],
    data: _elkjs.ELKInputData,
) -> None:
    """Move edges to boxes."""
    edges_to_remove: list[str] = []
    for c in connections:
        source_owner_uuids = get_all_owners(c.source)
        target_owner_uuids = get_all_owners(c.target)
        if c.source == c.target:
            source_owner_uuids.remove(c.source.uuid)
            target_owner_uuids.remove(c.source.uuid)

        common_owner_uuid = None
        for owner in source_owner_uuids:
            if owner in target_owner_uuids:
                common_owner_uuid = owner
                break

        if not common_owner_uuid or not (
            owner_box := boxes.get(common_owner_uuid)
        ):
            continue

        for edge in data.edges:
            if edge.id == c.uuid:
                owner_box.edges.append(edge)
                edges_to_remove.append(edge.id)
    data.edges = [e for e in data.edges if e.id not in edges_to_remove]


def get_all_owners(obj: common.GenericElement) -> list[str]:
    """Return the UUIDs from all owners of ``obj``."""
    owners: list[str] = []
    current = obj
    while current is not None:
        owners.append(current.uuid)
        try:
            current = current.owner
        except AttributeError:
            break
    return owners
