# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved.

from typing import List, Set

from availsim4core.src.context.rca.rca_record import RootCauseAnalysisRecord
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.context.system.rca_trigger import RootCauseAnalysisTrigger
from availsim4core.src.timeline.record import Record
from availsim4core.src.timeline.record_component import RecordComponent


class RootCauseAnalysisManager:
    """
    Class managing the root cause analysis across DES iterations; contains a trigger set and, a set of components built 
    from the root component and a list of RCA records, where the output of the root cause analysis is stored.
    """
    __slots__ = 'root_cause_analysis_trigger_set', 'root_component_set', 'root_cause_analysis_record_list'

    def __init__(self,
                 root_cause_analysis_trigger_set:Set[RootCauseAnalysisTrigger],
                 root_component_set:Set[Component]):
        self.root_cause_analysis_trigger_set = root_cause_analysis_trigger_set
        self.root_component_set = root_component_set
        self.root_cause_analysis_record_list: List[RootCauseAnalysisRecord] = []

    def __eq__(self, other):
        return self.root_cause_analysis_trigger_set == other.root_cause_analysis_trigger_set and \
                self.root_component_set == other.root_component_set and \
                self.root_cause_analysis_record_list == other.root_cause_analysis_record_list

    def _append_rca_snapshot(self,
                             record: RecordComponent,
                             seed: int,
                             phase_name: str):
        new_rca_dump = RootCauseAnalysisRecord(seed,
                                               record,
                                               phase_name,
                                               self.root_component_set)
        self.root_cause_analysis_record_list.append(new_rca_dump)

    def trigger_root_cause_analysis_check(self,
                                          changed_records_list: List[Record],
                                          seed: int,
                                          phase_name: str):
        for record in changed_records_list:
            if isinstance(record, RecordComponent) \
                and record.check_if_in_rca_triggers(self.root_cause_analysis_trigger_set, phase_name):
                self._append_rca_snapshot(record, seed, phase_name)
