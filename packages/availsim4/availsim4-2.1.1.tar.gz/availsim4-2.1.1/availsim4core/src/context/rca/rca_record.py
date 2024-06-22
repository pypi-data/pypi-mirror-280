# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import Set

from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.timeline.record_component import RecordComponent


class RootCauseAnalysisRecord:
    """
    Class managing the records made by the RCA feature. It generates a snapshot of the state of the system
    """
    __slots__ = 'simulation_id', 'timestamp', 'rca_trigger_component', 'rca_trigger_status', 'rca_trigger_phase', \
                'description', 'component_statuses_dict'

    def __init__(self, 
                 simulation_id: int,
                 record: RecordComponent,
                 rca_trigger_phase: str,
                 set_components: Set[Component]):
        self.simulation_id = simulation_id
        self.timestamp = record.timestamp
        self.rca_trigger_component = f"{record.component.name}_{record.component.local_id}_{record.component.global_id}"

        self.rca_trigger_status = str(record.status)
        self.rca_trigger_phase = rca_trigger_phase
        self.description = record.description

        component_status_dump_dict = {}
        for component in set_components:  
            component_status_dump_dict[f"{component.name}_{component.local_id}_{component.global_id}"] = component.status
        self.component_statuses_dict = component_status_dump_dict

    def __hash__(self):
        return hash((type(self), self.simulation_id, self.timestamp, self.rca_trigger_component,
                     self.rca_trigger_status, self.rca_trigger_phase, self.description, self.component_statuses_dict))

    def __eq__(self, other):
        if not isinstance(other, RootCauseAnalysisRecord):
            return NotImplemented
        return self.simulation_id == other.simulation_id and \
               self.timestamp == other.timestamp and \
               self.rca_trigger_component == other.rca_trigger_component and \
               self.rca_trigger_status == other.rca_trigger_status and \
               self.rca_trigger_phase == other.rca_trigger_phase and \
               self.description == other.description and \
               self.component_statuses_dict == other.component_statuses_dict
