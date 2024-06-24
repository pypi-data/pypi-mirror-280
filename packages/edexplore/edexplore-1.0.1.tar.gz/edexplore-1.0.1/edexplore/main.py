import numpy as np
import pandas as pd
import ipywidgets as widgets

from edexplore.defined import filter_df, process_subset

from edexplore.constants import REGEX_DICT
from edexplore.helpers import sample, logger


def interact(df):

    topwidgets, columns = {}, list(df.columns)

    # Box 01
    topwidgets['operated_columns'] = widgets.SelectMultiple(
        options=columns,
        layout={"width" : "190px", "height" : "100px"}, disabled=False
    )

    topwidgets['buttons'] = widgets.RadioButtons(
        options=['is null', 'is not null', 'is duplicated', 'drop duplicates'],
        layout={"width" : "130px"}, disabled=False
    )

    # Box 02
    topwidgets['regex'] = widgets.Dropdown(
        options=["is string", "is numeric", "suspicious str.", "extra spaces", "lead./trail. spaces",
                 "missing spaces", "html tags", "unicode char.", "is not null"],
        value=None, description='regex',
        layout={"width" : "210px"}, disabled=False
    )

    topwidgets['regex_column'] = widgets.SelectMultiple(
        options=columns,
        layout={"width" : "270px", "height" : "80px"},
        disabled=False
    )

    # Box 03
    topwidgets['range_on'] = widgets.Dropdown(
        options=columns, value=None,
        description='low:high', layout={"width" : "210px"},
        disabled=False
    )

    topwidgets['small_to_large'] = widgets.IntSlider(
        value=50, min=0, max=100, step=1,
        description='str length %',
        disabled=False, continuous_update=False,
        orientation='horizontal', layout={"width" : "300px"}
    )

    topwidgets['min_to_max'] = widgets.IntSlider(
        value=50, min=0, max=100, step=1,
        description='num range %',
        disabled=False, continuous_update=False,
        orientation='horizontal', layout={"width" : "300px"},
    )

    topwidgets['_sample'] = widgets.ToggleButton(
        value=False, description='Sample',
        layout={"width" : "90px", "height" : "30px"},
        icon='refresh', disabled=False,
        button_style='warning'
    )
    
    def subset(operated_columns, buttons, regex, regex_column, range_on, min_to_max, small_to_large, _sample):
        """
        Only the filtering happens here.
        """
        filtered_df = filter_df(df, operated_columns, buttons, regex, regex_column, REGEX_DICT)
        process_subset(filtered_df, logger, range_on, min_to_max, small_to_large, _sample, sample, display)

    # Here we resume original function code.
    out = widgets.interactive_output(subset, topwidgets)
    wids = list(topwidgets.values())

    # Box 01
    row_01_sub_01 = widgets.HBox([wids[0], wids[1]], layout={"border":"1px solid black"})
    # Box 02
    row_01_sub_02 = widgets.VBox([wids[2], wids[3]], layout={"border":"1px solid black"})
    # Box 03
    row_01_sub_03_02 = widgets.VBox([wids[5], wids[6]])
    row_01_sub_03 = widgets.VBox([wids[4], row_01_sub_03_02], layout={"border":"1px solid black"})

    # Combine Row 01
    row_01 = widgets.HBox([row_01_sub_01, row_01_sub_02, row_01_sub_03], layout=widgets.Layout(justify_content="space-between"))
    # Sample button in Row 02
    row_02 = widgets.HBox([wids[7]])

    return widgets.VBox([row_01, row_02, out])
