"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2017
SEE COPYRIGHT NOTICE BELOW
"""

from __future__ import annotations

import dataclasses as dtcl
import textwrap as text
import typing as h
from datetime import datetime as date_time_t

import PyQt6.QtWidgets as wdgt
from logger_36 import LOGGER
from PyQt6.QtCore import QCoreApplication, QPoint, QRectF
from pyvispr.config.appearance.color import (
    BUTTON_BRUSH_STATE_DISABLED,
    BUTTON_BRUSH_STATE_DOING,
    BUTTON_BRUSH_STATE_DONE,
    BUTTON_BRUSH_STATE_ERROR,
    BUTTON_BRUSH_STATE_TODO,
    INOUT_BRUSH_ACTIVE,
    INOUT_BRUSH_INACTIVE,
    LINK_PEN_EMPTY,
    LINK_PEN_FULL,
    LINK_PEN_HALF,
    NODE_BRUSH_RESTING,
    NODE_BRUSH_RUNNING,
)
from pyvispr.constant.flow.node import (
    MSG_NEW_NODE_NAME_REQUESTED,
    MSG_NEW_NODE_OUTPUT,
    MSG_NEW_NODE_STATE,
    UNIQUE_NAME_INTAKE,
)
from pyvispr.constant.flow.value import VALUE_NOT_SET
from pyvispr.extension.object.type import TypesAreCompatible
from pyvispr.flow.functional.graph import graph_t as graph_functional_t
from pyvispr.flow.functional.node import node_t as functional_t
from pyvispr.flow.functional.node import state_e
from pyvispr.flow.visual.link import link_t
from pyvispr.flow.visual.node import node_t
from pyvispr.flow.visual.socket import active_socket_t
from pyvispr.flow.visual.value import invalid_ii_value_t
from pyvispr.runtime.backend import SCREEN_BACKEND
from sio_messenger.instance import MESSENGER

_json_description_h = tuple[
    tuple[tuple[str, str, dict[str, h.Any], float, float], ...],
    tuple[tuple, ...],
]


@dtcl.dataclass(slots=True, repr=False, eq=False)
class graph_t(wdgt.QGraphicsScene):
    functional: graph_functional_t = dtcl.field(
        init=False, default_factory=graph_functional_t
    )
    nodes: list[node_t] = dtcl.field(init=False, default_factory=list)
    links: list[link_t] = dtcl.field(init=False, default_factory=list)

    _active_socket: active_socket_t = dtcl.field(
        init=False, default_factory=active_socket_t
    )

    def __post_init__(self) -> None:
        """"""
        wdgt.QGraphicsScene.__init__(self)

        SCREEN_BACKEND.AddMessageCanal(self, "changed", self.UpdateLinkPaths)
        MESSENGER.AddCanal(MSG_NEW_NODE_NAME_REQUESTED, self.ProcessNodeRenamingRequest)
        MESSENGER.AddCanal(MSG_NEW_NODE_STATE, self.AccountForNewNodeState)
        MESSENGER.AddCanal(MSG_NEW_NODE_OUTPUT, self.AccountForNewNodeOutput)

    @classmethod
    def __NewFromJsonDescription__(cls, description: _json_description_h, /) -> graph_t:
        """"""
        output = cls()

        nodes, links = description

        original_name_of = {}
        for name_dsc, name_fct, ii_values, position_x, position_y in nodes:
            node = output.AddNode(name_dsc, wished_name=name_fct, and_return_it=True)
            original_name_of[node.functional.name] = name_fct
            for intake_name, value in ii_values.items():
                node.SetIIValue(
                    intake_name, value, output.functional.InvalidateNodeOutputs
                )
            node.setPos(position_x, position_y)

        for source, target, *sockets in links:
            for node in output.nodes:
                if original_name_of[node.functional.name] == source:
                    source = node
                elif original_name_of[node.functional.name] == target:
                    target = node
                if isinstance(source, node_t) and isinstance(target, node_t):
                    break
            for output_name, intake_name in sockets:
                output.AddLink(source, output_name, target, intake_name)

        return output

    def __DescriptionForJSON__(self) -> _json_description_h:
        """"""
        return (
            tuple(
                (
                    _elm.functional.description.name,
                    _elm.functional.name,
                    _elm.IIValue(self.functional),
                    _elm.x(),
                    _elm.y(),
                )
                for _elm in self.nodes
            ),
            tuple(
                (
                    _elm.source.functional.name,
                    _elm.target.functional.name,
                )
                + self.functional.LinksBetween(
                    _elm.source.functional, _elm.target.functional
                )
                for _elm in self.links
            ),
        )

    def AddNode(
        self,
        stripe: str,
        /,
        *,
        wished_name: str | None = None,
        and_return_it: bool = False,
    ) -> node_t | None:
        """"""
        functional = self.functional.AddNode(
            stripe, wished_name=wished_name, and_return_it=True
        )
        if functional is None:
            return None

        node = node_t.NewForFunctional(functional)
        self.nodes.append(node)

        # Otherwise the newly created visual node replaces the selection.
        self.clearSelection()
        self.addItem(node)
        if node.ii_dialog is not None:
            self.addItem(node.ii_dialog)

        if and_return_it:
            return node

    def RemoveNode(self, node: node_t, /) -> None:
        """"""
        if node.ii_dialog is not None:
            node.ii_dialog.close()

        # Do not iterate directly on the list since it can be modified in the process.
        for link in tuple(self.links):
            if (link.source is node) or (link.target is node):
                self.RemoveLink(link)

        self.functional.RemoveNode(node.functional)
        self.nodes.remove(node)
        self.removeItem(node)
        if node.ii_dialog is not None:
            self.removeItem(node.ii_dialog)

    def AddLink(
        self,
        source: node_t,
        output_name: str,
        target: node_t,
        intake_name: str,
        /,
    ) -> None:
        """"""
        self.functional.AddLink(
            source.functional, output_name, target.functional, intake_name
        )
        for link in self.links:
            if (link.source is source) and (link.target is target):
                link.AddFunctional(output_name, intake_name)
                break
        else:
            link = link_t.New(
                source,
                output_name,
                source.output_socket_coordinates,
                target,
                intake_name,
                target.intake_socket_coordinates,
            )
            self.links.append(link)
            self.addItem(link)
            self.addItem(link.arrow)

    def RemoveLink(
        self,
        link: link_t,
        /,
        output_name: str | None = None,
        intake_name: str | None = None,
    ) -> None:
        """"""
        source = link.source.functional
        target = link.target.functional

        if output_name is None:  # intake_name must also be None.
            # Deal with visual link first, otherwise LinksBetween will be empty.
            for output_name, intake_name in self.functional.LinksBetween(
                source, target
            ):
                link.RemoveFunctional(output_name, intake_name)
            self.functional.RemoveLink(
                source,
                None,
                target,
                None,
            )
        else:  # Both names are not None.
            self.functional.RemoveLink(
                source,
                output_name,
                target,
                intake_name,
            )
            link.RemoveFunctional(output_name, intake_name)

        if self.functional.links.SocketPairsOfLink(source, target) is None:
            self.links.remove(link)
            self.removeItem(link)
            self.removeItem(link.arrow)

    def MergeWith(self, other: graph_t, /) -> None:
        """"""
        MESSENGER.RemoveReceiverAction(
            other.ProcessNodeRenamingRequest, name=MSG_NEW_NODE_NAME_REQUESTED
        )
        MESSENGER.RemoveReceiverAction(
            other.AccountForNewNodeState, name=MSG_NEW_NODE_STATE
        )
        MESSENGER.RemoveReceiverAction(
            other.AccountForNewNodeOutput, name=MSG_NEW_NODE_OUTPUT
        )

        self.functional.MergeWith(other.functional)

        for node in other.nodes:
            node.true_name_request = False
            node.label.setPlainText(node.functional.name)

        self.nodes.extend(other.nodes)
        self.links.extend(other.links)
        for item in other.nodes + other.links:
            self.addItem(item)
        for node in other.nodes:
            if node.ii_dialog is not None:
                self.addItem(node.ii_dialog)
        for link in other.links:
            self.addItem(link.arrow)

    def Run(
        self,
        /,
        *,
        workflow: str | None = None,
        script_accessor: h.TextIO = None,
    ) -> None:
        """"""
        for node in self.nodes:
            functional = node.functional
            if functional.state is not state_e.todo:
                continue

            for intake_name, value in node.IIValue(self.functional).items():
                if isinstance(value, invalid_ii_value_t):
                    issues = "\n".join(value.issues)
                    LOGGER.error(
                        f"Invalid value of {functional.name}.{intake_name}:\n"
                        f"{issues}"
                    )
                    value = VALUE_NOT_SET
                functional.SetIntakeValue(intake_name, value)

        un_run_nodes = self.functional.Run(
            workflow=workflow, script_accessor=script_accessor
        )

        if un_run_nodes.__len__() > 0:
            un_run_nodes = ", ".join(sorted(_elm.name for _elm in un_run_nodes))
            if script_accessor is None:
                LOGGER.error(f"Un-run nodes: {un_run_nodes}.")
            else:
                message = (
                    f"Workflow saving as a script was incomplete "
                    f"due to the following node(s) not being runnable:\n"
                    f"{un_run_nodes}."
                )
                LOGGER.error(message)
                wdgt.QMessageBox.critical(
                    None,
                    "Workflow Saving as Script Error",
                    message,
                )

    def ProcessNodeRenamingRequest(self, node: node_t, wished_name: str, /) -> None:
        """"""
        self.functional.RenameNode(node.functional, wished_name)
        if node.functional.name != wished_name:
            node.UpdateNameFromFunctional()

    def ManageLinkAddition(
        self, node: node_t, node_is_source: bool, position: QPoint, /
    ) -> None:
        """"""
        if self._active_socket.node is None:
            self._SetActiveSocket(node, node_is_source, position)
            return

        same_node = node is self._active_socket.node
        same_kind = (node_is_source and self._active_socket.is_source) or not (
            node_is_source or self._active_socket.is_source
        )
        if same_node or same_kind:
            if same_node and same_kind:
                if node_is_source:
                    button = self._active_socket.node.out_btn
                else:
                    button = self._active_socket.node.in_btn
                self._active_socket.node = None
                button.setBrush(INOUT_BRUSH_INACTIVE)
            return

        source, source_name, target, target_name, button = self._SocketsForLink(
            node, node_is_source, position
        )
        if source is None:
            return

        self.AddLink(source, source_name, target, target_name)
        self._active_socket.node = None
        button.setBrush(INOUT_BRUSH_INACTIVE)

    def _SetActiveSocket(
        self, node: node_t, node_is_source: bool, position: QPoint, /
    ) -> None:
        """"""
        functional = node.functional
        description = functional.description
        if node_is_source:
            sockets = description.outputs
            possible_names = description.output_names
            button = node.out_btn
        else:
            sockets = description.intakes
            links = self.functional.links
            possible_names = tuple(
                _nme
                for _nme in functional.intakes
                if links.IntakeSocketIsFree(functional, _nme)
            )
            button = node.in_btn
        possible_names = tuple(
            filter(lambda _elm: _elm != UNIQUE_NAME_INTAKE, possible_names)
        )

        if possible_names.__len__() > 1:
            selected = _SelectedSocketName(possible_names, position)
        elif possible_names.__len__() > 0:
            selected = possible_names[0]
        else:
            selected = None
        if selected is None:
            return

        stripe = sockets[selected]
        if not node_is_source:
            stripe = stripe.type
        self._active_socket.node = node
        self._active_socket.is_source = node_is_source
        self._active_socket.name = selected
        self._active_socket.type = stripe
        button.setBrush(INOUT_BRUSH_ACTIVE)

    def _SocketsForLink(
        self, node: node_t, node_is_source: bool, position: QPoint, /
    ) -> tuple[
        node_t | None,
        str | None,
        node_t | None,
        str | None,
        wdgt.QGraphicsRectItem | None,
    ]:
        """"""
        functional = node.functional
        description = functional.description
        if node_is_source:
            source = node
            target, _, target_name, target_type = self._active_socket.AsTuple()
            possible_names = tuple(
                _nme
                for _nme, _tpe in description.outputs.items()
                if TypesAreCompatible(_tpe, target_type)
            )
        else:
            source, _, source_name, source_type = self._active_socket.AsTuple()
            target = node
            links = self.functional.links
            possible_names = tuple(
                _nme
                for _nme in functional.intakes
                if links.IntakeSocketIsFree(functional, _nme)
                and TypesAreCompatible(description.intakes[_nme].type, source_type)
            )
        possible_names = tuple(
            filter(lambda _elm: _elm != UNIQUE_NAME_INTAKE, possible_names)
        )
        if (n_names := possible_names.__len__()) == 0:
            return 5 * (None,)

        if n_names > 1:
            selected = _SelectedSocketName(possible_names, position)
            if selected is None:
                return 5 * (None,)
        else:
            selected = possible_names[0]
        if node_is_source:
            source_name = selected
            button = target.in_btn
        else:
            target_name = selected
            button = source.out_btn

        return source, source_name, target, target_name, button

    def UpdateLinkPaths(
        self, _: h.Sequence[QRectF] | None, /, *, even_if_still: bool = False
    ) -> None:
        """"""
        for node in self.items():
            if isinstance(node, node_t) and (
                even_if_still or node.position_has_changed
            ):
                for link in self.links:
                    link.SetPath(
                        link.source.output_socket_coordinates,
                        link.target.intake_socket_coordinates,
                    )
                node.position_has_changed = False

    def AlignOnGrid(self) -> None:
        """"""
        for node in self.nodes:
            node.AlignOnGrid()

    def Clear(self) -> None:
        """"""
        # Do not iterate directly on the list since it is modified in the process.
        while self.nodes.__len__() > 0:
            self.RemoveNode(self.nodes[0])

    def AccountForNewNodeState(self, node: functional_t, /) -> None:
        """"""
        if node.state is state_e.disabled:
            message = "Disabled"
            brushes = (NODE_BRUSH_RESTING, BUTTON_BRUSH_STATE_DISABLED)
        elif node.state is state_e.todo:
            message = "Needs Running"
            brushes = (NODE_BRUSH_RESTING, BUTTON_BRUSH_STATE_TODO)
        elif node.state is state_e.doing:
            message = f"Running since {date_time_t.now()}"
            brushes = (NODE_BRUSH_RUNNING, BUTTON_BRUSH_STATE_DOING)
        elif node.state is state_e.done:
            message = f"Run Successfully ({date_time_t.now()})"
            brushes = (NODE_BRUSH_RESTING, BUTTON_BRUSH_STATE_DONE)
        else:  # state_e.done_with_error
            message = f"Run with ERROR ({date_time_t.now()})"
            brushes = (NODE_BRUSH_RESTING, BUTTON_BRUSH_STATE_ERROR)

        for current in self.nodes:
            if current.functional is node:
                current.setBrush(brushes[0])
                current.state_btn.setBrush(brushes[1])
                current.state_btn.setToolTip(message)
                QCoreApplication.processEvents()
                break

    def AccountForNewNodeOutput(
        self, node: functional_t, has_been_set: bool, /
    ) -> None:
        """"""
        empty = []
        half = []
        full = []
        for successor, socket_pairs in self.functional.links.FirstDegreeSuccessors(
            node
        ):
            n_with_values = sum(
                1 if node.outputs[_elm].has_value else 0 for _elm, _ in socket_pairs
            )
            if n_with_values == 0:
                empty.append(successor)
            elif n_with_values < socket_pairs.__len__():
                half.append(successor)
            else:
                full.append(successor)

        for successors, pen in zip(
            (empty, half, full), (LINK_PEN_EMPTY, LINK_PEN_HALF, LINK_PEN_FULL)
        ):
            for successor in successors:
                for link in self.links:
                    if (link.source.functional is node) and (
                        link.target.functional is successor
                    ):
                        link.setPen(pen)
        QCoreApplication.processEvents()

    @property
    def bounding_box(self) -> tuple[float, float, float, float]:
        """
        "Spelled" clockwise from north.
        """
        if self.nodes.__len__() == 0:
            return 4 * (0.0,)

        nodes = self.nodes

        rectangle = nodes[0].sceneBoundingRect()
        north = rectangle.y()
        west = rectangle.x()
        south = north + rectangle.height()
        east = west + rectangle.width()
        for node in nodes[1:]:
            rectangle = node.sceneBoundingRect()
            position_x, position_y = rectangle.x(), rectangle.y()
            north = min(north, position_y)
            west = min(west, position_x)
            south = max(south, position_y + rectangle.height())
            east = max(east, position_x + rectangle.width())

        return north, east, south, west

    def __str__(self) -> str:
        """"""
        output = [
            "VISUAL GRAPH",
            f"Visual nodes: {self.nodes.__len__()}",
            f"Visual links: {self.links.__len__()}",
            f"Bounding box (NESW): {str(self.bounding_box)[1:-1]}",
            "NODE(S):",
        ]

        for node in self.nodes:
            output.append(text.indent(str(node), "    "))

        output.append("LINK(S):")
        for link in self.links:
            output.append(text.indent(str(link), "    "))

        output.extend(("", str(self.functional)))

        return "\n".join(output)


def _SelectedSocketName(
    possible_names: tuple[str, ...], position: QPoint, /
) -> str | None:
    """"""
    menu = wdgt.QMenu()
    actions = tuple(menu.addAction(_elm) for _elm in possible_names)
    selected_action = menu.exec(position)
    if selected_action is None:
        return None

    return possible_names[actions.index(selected_action)]


"""
COPYRIGHT NOTICE

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.

SEE LICENCE NOTICE: file README-LICENCE-utf8.txt at project source root.

This software is being developed by Eric Debreuve, a CNRS employee and
member of team Morpheme.
Team Morpheme is a joint team between Inria, CNRS, and UniCA.
It is hosted by the Centre Inria d'Université Côte d'Azur, Laboratory
I3S, and Laboratory iBV.

CNRS: https://www.cnrs.fr/index.php/en
Inria: https://www.inria.fr/en/
UniCA: https://univ-cotedazur.eu/
Centre Inria d'Université Côte d'Azur: https://www.inria.fr/en/centre/sophia/
I3S: https://www.i3s.unice.fr/en/
iBV: http://ibv.unice.fr/
Team Morpheme: https://team.inria.fr/morpheme/
"""
