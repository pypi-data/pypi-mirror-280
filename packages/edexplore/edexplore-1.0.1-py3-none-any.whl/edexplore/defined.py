import numpy as np

from edexplore.helpers import _column_conditions, _regex_conditions
from edexplore.helpers import _range_filter, _length_filter, _range_process

def filter_df(df, operated_columns, buttons, regex, regex_column, REGEX_DICT):
    filtered_df = df.copy()
    
    columns = list(operated_columns)
    if columns:
        filtered_df = _column_conditions(columns, filtered_df, buttons)
        
    field_01 = list(regex_column)
    if field_01 and regex:
        filtered_df = _regex_conditions(field_01, filtered_df, REGEX_DICT[regex])

    return filtered_df

def process_subset(filtered_df, logger, range_on, min_to_max, small_to_large, _sample, sample, display):
    if filtered_df.empty:
        logger.info("No data!")
    elif range_on:
        temp_df = _range_process(filtered_df, range_on, min_to_max, small_to_large)
        
        if temp_df.empty:
            logger.info("No data!")
        elif _sample:
            sample(temp_df)
        else:
            display(temp_df)
    else:
        if _sample:
            sample(filtered_df)
        else:
            display(filtered_df)
    # Nothing to return, only sample or display calls.
