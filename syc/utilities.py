import pandas as pd
import numpy as np
def time_extractor(data,year):
    """
     Extract the timeline windows needed for the hydration-break analysis.
    Parameters
    data : pandas.DataFrame
        Event-level match data containing a 'match_time' column.
    year : int
        Tournament year. Supported years are 2022 and 2026.
    Returns
    tuple of pandas.DataFrame
        Four DataFrames representing the before/after windows.
    """
    if year==2026:
        data_12_22=data[(data['match_time']>=pd.Timedelta('00:12:00'))
                        &(data['match_time']<pd.Timedelta('00:22:00'))]
        data_25_35 = data[(data['match_time'] >= pd.Timedelta('00:25:00'))
                          & (data['match_time'] < pd.Timedelta('00:35:00'))]
        data_57_67 = data[(data['match_time'] >= pd.Timedelta('00:57:00'))
                          & (data['match_time'] < pd.Timedelta('01:07:00'))]
        data_70_80 = data[(data['match_time'] >= pd.Timedelta('01:10:00'))
                          & (data['match_time'] < pd.Timedelta('01:20:00'))]
        return data_12_22,data_25_35,data_57_67,data_70_80
    elif year==2022:
        data_12_22 = data[(data['match_time'] >= pd.Timedelta('00:12:00'))
                          & (data['match_time'] < pd.Timedelta('00:22:00'))]
        data_22_32 = data[(data['match_time'] >= pd.Timedelta('00:22:00'))
                          & (data['match_time'] < pd.Timedelta('00:32:00'))]
        data_57_67 = data[(data['match_time'] >= pd.Timedelta('00:57:00'))
                          & (data['match_time'] < pd.Timedelta('01:07:00'))]
        data_67_77 = data[(data['match_time'] >= pd.Timedelta('01:07:00'))
                          & (data['match_time'] < pd.Timedelta('01:17:00'))]
        return data_12_22, data_22_32, data_57_67, data_67_77
    else:
        raise ValueError('invalid year input.supported years are 2022 and 2026')
def statistics(data):
    return pd.DataFrame(
        {
            'mean':np.mean(data),
            'count':data.count(),
            'standard deviation':data.std(),
            'minimum':data.min(),
            'median':data.median(),
            'maximum':data.max(),
            '25th quartile':np.quantile(data,q=0.25),
            '75th quartile':np.quantile(data,q=0.75),
            'IQR':np.quantile(data,q=0.75)-np.quantile(data,q=0.25)
        },index=[0]
    )