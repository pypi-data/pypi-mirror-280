import logging

from edexplore.constants import NUM_REGEX, STR_REGEX

logging.basicConfig(format='%(message)s')
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


def sample(df):
    row = df.sample()
    for i in row:
        print(i)
        print("", row[i].iloc[0], '\n')

def column_reorderer(df_columns, columns):
    # reorder condition columns
    columns_all = list(df_columns)
    for c in columns:
        columns_all.remove(c)
    columns_new = columns + columns_all
    return columns_new

def _column_conditions(columns, df, buttons):
    if buttons == 'is null':
        filtered_df = df[df[columns].isnull().all(1)]
    if buttons == 'is not null':
        filtered_df = df[df[columns].notnull().all(1)]
    elif buttons == 'is duplicated':
        tf = df[df.duplicated(subset=columns)]
        # Duplicates are included together for clarity.
        if len(columns) == 1:
            _duplicates = tf[columns[0]].unique()
            _condition = df[columns[0]].isin(_duplicates)
            filtered_df = df[_condition]
        else:
            filtered_df = tf
        filtered_df = filtered_df.sort_values(by=columns)
    elif buttons == 'drop duplicates':
        filtered_df = df.drop_duplicates(subset=columns)
    else:
        pass

    columns_new = column_reorderer(df.columns, columns)

    return filtered_df[columns_new]

def _regex_conditions(columns, df, regex):
    INDICES = []
    _df = df.astype('object')
    for f in columns:
        if regex == "is not null":
            INDICES.extend( _df[_df[f].notnull()].index )
        elif regex == "suspicious str.":
            # filter out is numberic and is string rows and return the rest.
            stage_01 = _df[_df[f].notnull()]

            stage_02 = stage_01[stage_01[f].astype(str).str.contains(NUM_REGEX) == False]
            stage_03 = stage_02[stage_02[f].astype(str).str.contains(STR_REGEX) == False]
            if stage_03.empty:
                pass
            else:
                INDICES.extend( stage_03.index )
        else:
            temp_df = _df[_df[f].notnull()]
            INDICES.extend( temp_df[temp_df[f].astype(str).str.contains(regex)].index )
    
    filtered_df = df[df.index.isin( list(set(INDICES)) )]

    columns_new = column_reorderer(df.columns, columns)

    return filtered_df[columns_new]

def _range_filter(df, key, qv):
    temp_df = df.reset_index()[["index", key]]
    
    temp_df = temp_df[ temp_df[key].astype(str).str.contains(NUM_REGEX) ]
    temp_df[key] = temp_df[key].astype(float)
    temp_df = temp_df.sort_values(by=key)
    
    temp_df['r'] = (temp_df[key].
                        reset_index().index / len(temp_df[key]) * 100)
    temp_df['r'] = temp_df['r'].apply(lambda x: int(x))

    condition_1 = temp_df['r'] > (qv - 1.01)
    condition_2 = temp_df['r'] < (qv + 1.01)
    result = temp_df[condition_1 & condition_2]
    
    return result['index'].to_list()

def _length_filter(df, key, qv):
    temp_df = df.reset_index()[["index", key]]
    
    temp_df = temp_df[ temp_df[key].notnull() ]
    temp_df[key] = temp_df[key].astype(str).str.len()
    temp_df = temp_df.sort_values(by=key)
    
    temp_df['r'] = (temp_df[key].
                        reset_index().index / len(temp_df[key]) * 100)
    temp_df['r'] = temp_df['r'].apply(lambda x: int(x))

    condition_1 = temp_df['r'] > (qv - 1.01)
    condition_2 = temp_df['r'] < (qv + 1.01)
    result = temp_df[condition_1 & condition_2]

    return result['index'].to_list()

def _range_process(df, range_on, min_to_max, small_to_large):
    if min_to_max != 50:
        temp_df = df.copy()
        idx = _range_filter(temp_df, range_on, min_to_max)
        temp_df = temp_df[ temp_df.index.isin( idx ) ]
    elif small_to_large != 50:
        temp_df = df.copy()
        idx = _length_filter(temp_df, range_on, small_to_large)
        temp_df = temp_df[ temp_df.index.isin( idx ) ]
    else:
        temp_df = df.copy()

    columns_new = column_reorderer(temp_df.columns, [range_on])

    return temp_df[columns_new]