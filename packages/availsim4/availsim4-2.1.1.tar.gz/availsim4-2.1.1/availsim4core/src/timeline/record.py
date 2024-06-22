# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import Optional
from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.system.component_tree.status import Status


class Record:
    """
    Immutable
    """
    __slots__ = 'timestamp', 'phase', 'description', 'status'

    def __init__(self,
                 timestamp: float,
                 phase: Phase,
                 description: str,
                 status: Optional[Status] = None):
        self.timestamp = timestamp
        self.phase = phase
        self.description = description
        self.status = status

    def __str__(self):
        pass

    def __repr__(self):
        return f"timestamp: {self.timestamp}, description: {self.description}, status: {self.status}"

    def __eq__(self, other):
        return self.timestamp == other.timestamp \
               and self.phase == other.phase \
               and self.description == other.description \
               and self.status == other.status

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def get_result_record_entry(self):
        pass

    def check_if_in_rca_triggers(self, rca_triggers, current_phase_name):
        return False
