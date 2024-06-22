# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved.

"""Module for reading Phase Jump Triggers sheet of the Excel-formatted input"""

import logging
from typing import List
from availsim4core.resources.excel_strings import SystemTemplatePhaseJumpColumn
from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.system.phase_jump_trigger import PhaseJumpTrigger
from availsim4core.src.reader.xlsx import xlsx_utils
from availsim4core.src.reader.xlsx.system_template.sheet_reader import SheetReader


class PhaseJumpTriggersSheetReader(SheetReader):
    """Class for reading the content of the phase jump triggers sheet of the Excel input"""

    def generate_phase_jump_triggers_from_row(self, row, phase_list: List[Phase]) -> List[PhaseJumpTrigger]:
        """Create a list of objects defined by the row parameter"""
        exception_message_hint = f"phase jump row: {row}"

        phase_jump_trigger_component_name = xlsx_utils.clean_str_cell_else_raise(
            row[SystemTemplatePhaseJumpColumn.COMPONENT_NAME], exception_message_hint)
        phase_jump_trigger_component_status_list = xlsx_utils.clean_list_cell(
            row[SystemTemplatePhaseJumpColumn.COMPONENT_STATUS], exception_message_hint)
        phase_jump_trigger_from_phase_list = xlsx_utils.clean_list_cell(
            row[SystemTemplatePhaseJumpColumn.FROM_PHASE], exception_message_hint)
        phase_jump_trigger_to_phase = xlsx_utils.clean_str_cell_else_raise(
            row[SystemTemplatePhaseJumpColumn.TO_PHASE], exception_message_hint)
        phase_jump_trigger_comments = xlsx_utils.get_cell_text(row)

        return PhaseJumpTrigger.build(phase_jump_trigger_component_name, phase_jump_trigger_component_status_list,
                                      phase_jump_trigger_from_phase_list, phase_jump_trigger_to_phase, phase_list,
                                      phase_jump_trigger_comments)

    def generate_phase_jump_triggers(self, system_dictionary_phase_jump, phase_list: List[Phase]):
        """
        Generates a list of (component, status, in_phase, jump_to_phase) which trigger phase jumps.
        :param system_dictionary_phase_jump:
        :return: The complete list of phase jump triggers.
        """

        phase_jump_triggers_list = []

        for row in system_dictionary_phase_jump.values():
            try:
                new_phase_jump_triggers = self.generate_phase_jump_triggers_from_row(row, phase_list)
                for phase_jump_trigger in new_phase_jump_triggers:
                    self._check_if_phase_jump_destinations_disjoint(phase_jump_trigger.component_name,
                                                                    phase_jump_trigger.to_phase,
                                                                    phase_jump_trigger.to_phase)
                phase_jump_triggers_list.extend(new_phase_jump_triggers)
            except AttributeError:
                logging.info("Non-empty line with missing content present in the phase_jump sheet."
                             "\nCheck row: %s", row)
        logging.debug("Extracted from system file phase_jump_triggers_list = %s", phase_jump_triggers_list)
        return phase_jump_triggers_list

    @staticmethod
    def _check_if_phase_jump_destinations_disjoint(component_name, target_phase: Phase, destination_phase: Phase):
        if target_phase == destination_phase:
            message = (f"The phase jump trigger set on the component {component_name} with "
                       f"status {destination_phase} features the phase "
                       f"{target_phase} both in \"FROM PHASE\" and \"TO PHASE\" fields.")
            logging.info(message)
