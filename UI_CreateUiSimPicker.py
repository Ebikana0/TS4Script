import sims4.commands
import sims4

from ui.ui_dialog_picker import logger, TunablePickerDialogVariant, SimPickerRow, ObjectPickerRow, ObjectPickerTuningFlags, PurchasePickerRow, LotPickerRow
from ui.ui_dialog_picker import TunableUiOutfitPickerSnippet, OutfitPickerRow, UiSimPicker, SimPickerRow
from sims4.tuning.tunable import Tunable, get_default_display_name, TunableVariant, TunableList, TunableFactory
import services
import sims4
from sims4.localization import LocalizationHelperTuning
from ui.ui_text_input import UiTextInput
from typing import Any, Callable, Union, Iterator, Tuple

def CreateUiSimPicker(sim_info,_title,_text,_choices,_min_selectable,_max_selectable,_should_show_names,_hide_row_descriptions,_column_count):
    #UI SIM PICKER
    picker = UiSimPicker.TunableFactory().default(
                    sim_info,
                    title=lambda **_: LocalizationHelperTuning.get_raw_text(_title),
                    text=lambda **_: LocalizationHelperTuning.get_raw_text(_text),
                    min_selectable=_min_selectable,
                    max_selectable=_max_selectable,
                    should_show_names=False,
                    hide_row_description=_hide_row_descriptions,
                    column_count=_column_count
                )
    return picker

@sims4.commands.Command('uitest_chose', command_type=sims4.commands.CommandType.Live)
def myfirstscript(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("Creating22")

    def _on_chosen(dialog):
        output("a")
        result = dialog.get_result_tags()[-1] or dialog.get_result_tags()[0]
        output(str(result))
    try:
        sim = services.get_active_sim()
        household = sim.household.sim_info_gen()
        pick = CreateUiSimPicker(sim,"title","text",household,1,2,False,False,8)
        pick.add_row(SimPickerRow(sim.sim_id, tag=sim.sim_info))
        pick.show_dialog(on_response=_on_chosen)
        output("info:" + str(pick.ui_responses))

    except Exception as ex:
        output(str(ex))
