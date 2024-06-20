import pandas as pd
from . import error_quotient as eq
from . import repeated_error_density as red
from . import watwin as wt
from datetime import datetime, timedelta


def time_difference_greater_than_x_minutes(timestamp1: str | float, timestamp2: str | float, x: int):
    """
    Function to check if two timestamps have a time difference greater than a handed over integer.

    :param timestamp1: str or float representing the earlier timestamp
    :param timestamp2: str or float representing the later timestamp
    :param x: int defining the max time difference

    return: bool, True if time difference is greater than x, False otherwise
    """
    # Convert timestamps into Datetime-objects
    if isinstance(timestamp1, str):
        dt1 = datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S')
    elif isinstance(timestamp1, float):
        dt1 = datetime.fromtimestamp(timestamp1)
    else:
        dt1 = timestamp1
    if isinstance(timestamp2, str):
        dt2 = datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S')
    elif isinstance(timestamp2, float):
        dt2 = datetime.fromtimestamp(timestamp2)
    else:
        dt2 = timestamp2

    # Calculate the difference between the time stamps
    time_difference = abs(dt2 - dt1)

    # Check whether the difference is greater than x minutes
    return time_difference > timedelta(minutes=x)


def get_user_entries_sorted(df: pd.DataFrame, course_id: str, user_id: str, task_id: str = None):
    """
    Function to filter a pandas DataFrame by a given course id and user id and sort it via the column timestamp ascending.

    :param df: pandas DataFrame
    :param course_id: str defining the course id
    :param user_id: str defining the user id
    :param user_id: str defining the task id, if not given ignore this one

    return: sorted new pandas DataFrame
    """
    if task_id is None:
        user_entries = df.loc[(df['course_id'] == course_id) & (df['user_id'] == user_id)]
    else:
        user_entries = df.loc[(df['course_id'] == course_id) & (df['user_id'] == user_id) & (df['task_id'] == task_id)]
    user_entries_sorted = user_entries.sort_values(by='timestamp')
    return user_entries_sorted


def create_sessions(df: pd.DataFrame, groupby_columns: list, threshold_seconds: int) -> None:
    """
    Function to add column session with corresponding values to a pandas DataFrame.
    Function directly changes parameter df

    :param df: pandas DataFrame
    :param groupby_columns: list that indicates the first grouping by
    :param threshold_seconds: str defining the task id, if not given ignore this one

    return: Nothing
    """

    if "session" in df.columns:
        df.loc[:, "session"] = None
    else:
        df["session"] = None
    df_groups = df.groupby(groupby_columns)
    for group_name, group in df_groups:
        group = group.sort_values(by='timestamp')
        index_list = group.index.tolist()
        current_session = 1
        if len(index_list) > 0:
            # add default session for first statement
            df.at[index_list[0], 'session'] = current_session
            for i in range(0, len(index_list) - 1):
                current_dt = group.at[index_list[i], "timestamp"]
                next_dt = group.at[index_list[i + 1], "timestamp"]

                if time_difference_greater_than_x_minutes(current_dt, next_dt, threshold_seconds):
                    current_session += 1

                df.at[index_list[i + 1], 'session'] = current_session


def convert_dataframe_groups_into_dict(df_groups: pd.core.groupby.DataFrameGroupBy) -> dict:
    """
    Function to turn groups of panda DataFrame into a dictionary.

    :param df_groups: pandas DataFrameGroupBy object with all groups

    :return: dictionary in form of {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
        key_group_1 is a tuple of elements and depends on level:
                user level => ('course_id', 'user_id')
                user task level => ('course_id', 'user_id', 'task_id')
                user session level => ('course_id', 'user_id', 'session_id')
                user task session level => ('course_id', 'user_id', 'task_id', 'session_id')

    """
    result_dict = {}  # {key: [event1, event2, ...]}

    # group_name is a tuple with different numbers of elements:
    # user level => ('course_id', 'user_id')
    # user task level => ('course_id', 'user_id', 'task_id')
    # user session level => ('course_id', 'user_id', 'session_id')
    # user task session level => ('course_id', 'user_id', 'task_id', 'session_id')
    for group_name, group in df_groups:
        result_dict[group_name] = group.to_dict(orient="records")

    return result_dict


def prepare_dataframes(df: pd.DataFrame, level: str = "user") -> pd.core.groupby.DataFrameGroupBy:
    """
    Function to prepare and filter dataframes uniformly.

    :param df: pandas DataFrame with all data:
        Columns: "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"

    :param level: str which defines the level to be evaluated ("user", "user task", "user session", "user task session")

    :return: pandas DataFrameGroupBy (with filtered data based in level.
        Each Group in DataFrameGroupBy has a Group Name and a DataFrame
        Each DataFrame in the DataFrameGroupBy Object has columns: "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"


    """
    possible_options = ["user", "user task", "user session", "user task session"]
    if level not in possible_options:
        raise TypeError(
            f"Wrong value for param level. Handed over {level}, but needs to be an option from {possible_options}.")

    # user level
    if level == "user":
        df_groups = df.groupby(['course_id', 'user_id'])

    # user task level
    elif level == "user task":
        df_groups = df.groupby(['course_id', 'user_id', 'task_id'])

    # user session level
    elif level == "user session":
        create_sessions(df, ['course_id', 'user_id'], 20)
        # create_sessions(df, ['course_id', 'user_id'], 20)
        df_groups = df.groupby(['course_id', 'user_id', 'session'])

    # user task session level
    elif level == "user task session":
        # first add a column to whole dataframe that indicates the session for each user with value None
        # df_help_groups = df.groupby(['course_id', 'user_id', 'task_id'])
        create_sessions(df, ['course_id', 'user_id', 'task_id'], 20)
        # create_sessions(df, ['course_id', 'user_id', 'task_id'], 20, True)
        df_groups = df.groupby(['course_id', 'user_id', 'task_id', 'session'])

    return df_groups


def error_quotient(data: pd.DataFrame | dict, level: str = "user") -> dict:
    """
    Function to calculate the error quotient values for a given set of data based on the level.

    :param data: pandas DataFrame or dict with all data.
        Necessary columns of dataframe: "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"
        Structure for dict: {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
            key_group_1 is a tuple of elements and depends on level:
                user level => ('course_id', 'user_id')
                user task level => ('course_id', 'user_id', 'task_id')
                user session level => ('course_id', 'user_id', 'session_id')
                user task session level => ('course_id', 'user_id', 'task_id', 'session_id')

    :param level: str which defines the level to be evaluated ("user", "user task", "user session", "user task session")

    :return: dictionary which holds all values for error quotient in form of {key_group_1: (nominator, denominator), key_group_2: (nominator, denominator), ...}, e.g.:
        {
            ('C001', 'U001'): (5, 24),
            ('C002', 'U001'): (0, 0)
        }

    """

    possible_options = ["user", "user task", "user session", "user task session"]
    if level not in possible_options:
        raise TypeError(
            f"Wrong value for param level. Handed over {level}, but needs to be an option from {possible_options}.")
    if isinstance(data, pd.DataFrame):
        prepared_df = prepare_dataframes(data, level)
        prepared_dict = convert_dataframe_groups_into_dict(prepared_df)
    else:
        prepared_dict = data

    all_scores = {}
    for key, events in prepared_dict.items():
        sorted_events = sorted(events, key=lambda x: x['timestamp'])
        all_scores[key] = eq.calculate_total_score_error_quotient(sorted_events)

    return all_scores


def repeated_error_density(data: pd.DataFrame | dict, level: str = "user") -> dict:
    """
    Function to calculate the repeated error density values for a given set of data based on the level.

    :param data: pandas DataFrame or dict with all data.
        Necessary columns of dataframe: "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"
        Structure for dict: {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
            key_group_1 is a tuple of elements and depends on level:
                user level => ('course_id', 'user_id')
                user task level => ('course_id', 'user_id', 'task_id')
                user session level => ('course_id', 'user_id', 'session_id')
                user task session level => ('course_id', 'user_id', 'task_id', 'session_id')

    :param level: str which defines the level to be evaluated ("user", "user task", "user session", "user task session")

    :return: dictionary which holds all values for error quotient in form of {key_group_1: float, key_group_2: float, ...}, e.g.:
        {
            ('C001', 'U001'): 1 / 2,
            ('C002', 'U001'): 0
        }

    """

    possible_options = ["user", "user task", "user session", "user task session"]
    if level not in possible_options:
        raise TypeError(
            f"Wrong value for param level. Handed over {level}, but needs to be an option from {possible_options}.")

    if isinstance(data, pd.DataFrame):
        prepared_df = prepare_dataframes(data, level)
        prepared_dict = convert_dataframe_groups_into_dict(prepared_df)
    else:
        prepared_dict = data

    all_scores = {}
    for key, events in prepared_dict.items():
        sorted_events = sorted(events, key=lambda x: x['timestamp'])
        all_scores[key] = red.calculate_red(red.sanitize_events_for_red(red.convert_to_tuple(sorted_events)))

    return all_scores


def watwin(data: pd.DataFrame | dict, level: str = "user") -> dict:
    """
    Function to calculate the Watwin and RR values for a given set of data based on the level.

    :param data: pandas DataFrame or dict with all data.
        Necessary columns of dataframe: "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"
        Structure for dict: {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
            key_group_1 is a tuple of elements and depends on level:
                user level => ('course_id', 'user_id')
                user task level => ('course_id', 'user_id', 'task_id')
                user session level => ('course_id', 'user_id', 'session_id')
                user task session level => ('course_id', 'user_id', 'task_id', 'session_id')

    :param level: str which defines the level to be evaluated ("user", "user task", "user session", "user task session")

    :return: dictionary which holds all values for error quotient in form of {key_group_1: float, key_group_2: float, ...}, e.g.:
        {
            ('C001', 'U001'): 1 / 2,
            ('C002', 'U001'): 0
        }

    """

    possible_options = ["user", "user task", "user session", "user task session"]
    if level not in possible_options:
        raise TypeError(
            f"Wrong value for param level. Handed over {level}, but needs to be an option from {possible_options}.")

    if isinstance(data, pd.DataFrame):
        prepared_df = prepare_dataframes(data, level)
        prepared_dict = convert_dataframe_groups_into_dict(prepared_df)
    else:
        prepared_dict = data

    # preprocess all data before calculating times for geenralized errors
    preprocessed_data = watwin_preprocessing(prepared_dict)

    # calculate times for generalized errors
    generalized_error_times = watwin_get_generalized_error_times(data, prepared_dict, preprocessed_data)

    # calculate watwin score
    watwin_scores, rr_scores = watwin_calculation(preprocessed_data, generalized_error_times)


    return watwin_scores, rr_scores


def watwin_preprocessing(prepared_dict: dict) -> dict:
    """
    Preprocessing data for Watwin and RR calculation

    :param prepared_dict: dictionary in form of {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
    :return: dictionary in form of {key_group_1: [(event1, event2, timespan), (event3, event5, timespan), .....], key_group_2: [(event1, event2, timespan), (event4, event5, timespan), .....], ... }
        each event is a dictionary with timestamp, success, error_name, line, code
    """
    preprocessed_data = {}  # {key_group_1': (event1, event2, timespan), (event3, event4, timespan), ...}
    for key, events in prepared_dict.items():
        sorted_events = sorted(events, key=lambda x: x['timestamp'])
        preprocessed_data[key] = wt.preprocessing_watwin(sorted_events)

    return preprocessed_data


def watwin_get_generalized_error_times(data: pd.DataFrame | dict, prepared_dict: dict, preprocessed_data) -> dict:
    """
    Calculating the generalized error times for Watwin and RR in each course

    Watwin: 2 MAD_e and mean for all generalized errors over all students in a course
    RR: Q1 and Q3 for all generalized errors over all students in a course

    :param data: pandas DataFrame or dict with all data.
        Necessary columns of dataframe: "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"
        Structure for dict: {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
            key_group_1 is a tuple of elements and depends on level:
                user level => ('course_id', 'user_id')
                user task level => ('course_id', 'user_id', 'task_id')
                user session level => ('course_id', 'user_id', 'session_id')
                user task session level => ('course_id', 'user_id', 'task_id', 'session_id')

    :param prepared_dict: dictionary in form of {key_group_1: [event1, event2, ...], key_group_2: [event1, event2, ...], ... }
    :param preprocessed_data: dictionary in form of {key_group_1: [(event1, event2, timespan), (event3, event5, timespan), .....], key_group_2: [(event1, event2, timespan), (event4, event5, timespan), .....], ... }
        each event is a dictionary with timestamp, success, error_name, line, code
    :return: dictionary in form of {key_group_1: {"watwin": {"deviation": two_mad_e_generalized_errors, "mean": mean_generalized_errors}, "rr": {"q1": q1_generalized_errors, "q3": q3_generalized_errors}}, ...}
        two_mad_e_generalized_errors, mean_generalized_errors, q1_generalized_errors & q3_generalized_errors are dicts in form of {"SyntaxError": timedelta, ...}
    """
    generalized_error_times = {}
    if isinstance(data, pd.DataFrame):
        all_course_ids = data['course_id'].unique()
    else:
        all_course_ids = set([elem[0] for elem in list(prepared_dict.keys())])

    # calculation for mean & deviation for correcting generalized errors always based on a whole class
    for course in all_course_ids:
        course_data = {key: value for key, value in preprocessed_data.items() if key[0] == course}
        times = wt.get_times_generalized_errors(course_data)
        for key, value in preprocessed_data.items():
            if key[0] == course:
                generalized_error_times[key] = times

    return generalized_error_times


def watwin_calculation(preprocessed_data: dict, generalized_error_times: dict) -> tuple:
    """
    Function to calculate Watwin and RR scores

    :param preprocessed_data: dictionary in form of {key_group_1: [(event1, event2, timespan), (event3, event5, timespan), .....], key_group_2: [(event1, event2, timespan), (event4, event5, timespan), .....], ... }
        each event is a dictionary with timestamp, success, error_name, line, code
    :param generalized_error_times: dictionary in form of {key_group_1: {"watwin": {"deviation": two_mad_e_generalized_errors, "mean": mean_generalized_errors}, "rr": {"q1": q1_generalized_errors, "q3": q3_generalized_errors}}, ...}
        two_mad_e_generalized_errors, mean_generalized_errors, q1_generalized_errors & q3_generalized_errors are dicts in form of {"SyntaxError": timedelta, ...}
    :return: tuple in form of (watwin_scores, rr_scores)
        watwin_scores and rr_scores are dictionaries in form of {key_group_1: float, key_group_2: float, ...}
    """
    watwin_scores = {}
    rr_scores = {}
    for key, value in preprocessed_data.items():
        results = wt.calculate_watwin_and_rr(value, generalized_error_times[key])  # [0]
        watwin_scores[key] = results[0]
        rr_scores[key] = results[1]

    return watwin_scores, rr_scores
