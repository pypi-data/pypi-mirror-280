import re
import string
import Levenshtein as lvs
from collections import defaultdict
from datetime import datetime, timedelta
import statistics
import pandas as pd


################################################
################################################
##  Preparing a Set of Compilation Pairings   ##
################################################
################################################
def preprocessing_watwin(compilation_events: list) -> list:
    """
    Function to preprocess data for watwin

    :param compilation_events:
       list with events of one user in one file: [e1, e2, e3 .....]
       each event is a dictionary with timestamp, success, error_name, line, code

    :return: list with tuples of events of one user in one file: [(e1, e2, timespan), (e4, e5, timespan), .....]
        each event is a dictionary with timestamp, success, error_name, line, code

    """

    sorted_events = sorted(compilation_events, key=lambda x: x['timestamp'])
    events_tuple = pair_construction(sorted_events)
    pair_pruning_events = pair_pruning(events_tuple, sorted_events)
    filtered_events = filtering_commented_and_deletion_fixes(pair_pruning_events)
    timespan_events = time_estimation(sorted(sorted_events, key=lambda x: x['timestamp']),
                                      filtered_events)

    return timespan_events


################################################
##            1. Pair Construction            ##
################################################
def pair_construction(compilation_events: list) -> list:
    """
    function to create tuples of compilation events for a file / cell / line: [(e1, e2), (e2, e3), ...]

    :param compilation_events:
       list with events of one user in one file: [e1, e2, e3 .....]
       each event is a dictionary with timestamp, success, error_name, line, code
    :return:
       list with tuples of consecutive events of one user in one file: [(e1, e2), (e2, e3), .....]
       each event is a dictionary with timestamp, success, error_name, line, code
    """
    return [({key: value for key, value in compilation_events[i].items()},
             {key: value for key, value in compilation_events[i + 1].items()}) for i in
            range(len(compilation_events) - 1)]


################################################
##            2. Pair Pruning                 ##
################################################
def pair_pruning(events_tuple: list, compilation_events: list) -> list:
    """
    function to remove all "unwanted" event pairs:
        Remove temporarily comments from all code snapshots from pair Construction using regex expressions
        Remove all pairings (ef, et) that have the same code snapshot
        Remove all pairings (ef, et) where ef has no compilation error (success)
        Add comments back to all remaining pairings

    :param events_tuple:
        list with tuples of consecutive events of one user in one file: [(e1, e2), (e2, e3), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    :param compilation_events:
        list with events of one user in one file: [e1, e2, e3 .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    :return:
        list with tuples of events of one user in one file: [(e1, e2), (e3, e4), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    """
    # Create an extra tuple as a copy for later on
    events_tuple_index = {i: ({key: value for key, value in events_tuple[i][0].items()},
                              {key: value for key, value in events_tuple[i][1].items()}) for i in
                          range(len(events_tuple))}

    # Remove temporarily comments from all code snapshots from pair Construction using regex expressions
    compilation_events_comments_removed = [{key: value for key, value in event.items()} for event in compilation_events]
    for elem in compilation_events_comments_removed:
        comments = extract_comments(elem['input_code'])

        for comment in comments:
            start_index = elem['input_code'].find(comment)
            end_index = start_index + len(comment)
            while start_index > 1:
                # whitespace
                if string.whitespace in elem['input_code'][start_index - 1:start_index]:
                    start_index -= 1
                # newline \n is also just counted as 1
                # T.B.D.: What do to if after comment is no newline?
                elif "\n" in elem['input_code'][start_index - 1:start_index]:
                    start_index -= 1
                # tab \t is also just counted as 1
                elif "\t" in elem['input_code'][start_index - 1:start_index]:
                    start_index -= 1
                else:
                    break

            elem['input_code'] = delete_characters(elem['input_code'], start_index, end_index)

    # Remove all pairings (ef, et) that have the same code snapshot
    compilation_events_comments_removed_tuple_index = {
        i: (compilation_events_comments_removed[i], compilation_events_comments_removed[i + 1], i) for i in
        range(len(compilation_events_comments_removed) - 1)}

    keys_to_be_removed = []
    for key, value in compilation_events_comments_removed_tuple_index.items():
        # for key, value in copy.deepcopy(compilation_events_comments_removed_tuple_index).items():
        if value[0]["input_code"] == value[1]["input_code"]:
            keys_to_be_removed.append(key)
            # compilation_events_comments_removed_tuple_index.pop(key)
    for key in keys_to_be_removed:
        compilation_events_comments_removed_tuple_index.pop(key)

    # Remove all pairings (ef, et) where ef has no compilation error (success)
    keys_to_be_removed = []
    for key, value in compilation_events_comments_removed_tuple_index.items():
        # for key, value in copy.deepcopy(compilation_events_comments_removed_tuple_index).items():
        # rint(value)
        if value[0]["success"] == True:
            keys_to_be_removed.append(key)
            # compilation_events_comments_removed_tuple_index.pop(key)
    for key in keys_to_be_removed:
        compilation_events_comments_removed_tuple_index.pop(key)

    # Add comments back to all remaining pairings
    for key, value in compilation_events_comments_removed_tuple_index.items():
        compilation_events_comments_removed_tuple_index[key] = events_tuple_index[key]

    return [({key_ef: value_ef for key_ef, value_ef in value[0].items()},
             {key_et: value_et for key_et, value_et in value[1].items()}) for key, value in
            sorted(compilation_events_comments_removed_tuple_index.items())]


def extract_comments(code: str) -> list:
    """
    function for extracting comments from a code snippet
    :param code:
        string with complete code including \n and \t, e.g.:
        ''from numpy import *\n\nx = array(eval(input("Digite o vetor : ")))\n\nm = mean(x)\n\nproduto = 1'
    :return: list with comments in code where each element is either a single line comment or a mutliline comment
    """
    comment_pattern = r'(?:(?P<comment>(?:^\s*)?(?:#.*?$)|(?:^\s*)?(?:\'\'\'.*?\'\'\')|(?:^\s*)?(?:\"\"\".*?\"\"\")))'
    comments = re.findall(comment_pattern, code, re.MULTILINE | re.DOTALL | re.UNICODE)
    return comments


def delete_characters(origin_string: str, start_index: int, end_index: int) -> str:
    """
    function to delete characters in a string based on the index
    :param origin_string: string to be deleted from
    :param start_index: index where deletions should start
    :param end_index: index where deletions should stop (excluding)
    :return: string
    """
    if start_index < 0 or end_index < 0:
        raise ValueError("Index cannot be negative.")
    if end_index < start_index:
        raise ValueError("End index cannot be less than start index.")
    return origin_string[:start_index] + origin_string[end_index:]


################################################
## 3. Filtering Commented and Deletion Fixes  ##
################################################
def filtering_commented_and_deletion_fixes(pair_pruning_events: list) -> list:
    """
    function to remove all event pairs with commented and deletion fixes:
        Remove deletion fixes via diff ration of both code snippets in a event tuple
        Remove commented fixes (error in event ef of tuple (ef, et) has been removes by commenting error line surrounding in et
    :param pair_pruning_events:
        list with tuples of events of one user in one file: [(e1, e2), (e3, e4), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    :return:
        list with tuples of events of one user in one file: [(e1, e2), (e4, e5), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    """
    pair_pruning_events_copy = [({key_ef: value_ef for key_ef, value_ef in elem[0].items()},
                                 {key_et: value_et for key_et, value_et in elem[1].items()}) for elem in
                                pair_pruning_events]

    for index, elem in reversed(list(enumerate(pair_pruning_events))):
        # Calculate deletion fixes:
        # 1. get diff ratio between code snapshots ef and et including inserts, changes and deletes
        df = calculate_diff_inserts_deletes_changes(elem[0]["input_code"], elem[1]["input_code"])

        # 2. if $df.insertions == 0 & df.changes == 0 & df.deletes > 0$, remove the pair (ef, et)
        if df["insert"] == 0 and df['replace'] == 0 and df["delete"] > 0:
            pair_pruning_events_copy.pop(index)
            continue

        # 3. remove event pair (ef, et) with commented fixes:
        try:
            # 3.1 Get code surrounding of error location of event ef
            line_number_ef = int(elem[0]['error_line']) - 1  # -1 as we start by counting with 0 in programming
            code_lines_ef = elem[0]['input_code'].split('\n')
            surrounding_lines = 0
            if line_number_ef < surrounding_lines:
                code_surrounding_ef = code_lines_ef[0: line_number_ef + 1 + surrounding_lines]
            else:
                code_surrounding_ef = code_lines_ef[
                                      line_number_ef - surrounding_lines: line_number_ef + 1 + surrounding_lines]

            # 3.2 Check if code surrounding has become commented in et
            # 3.2.1. get all comments from event et
            comments_et = extract_comments(elem[1]['input_code'])

            # 3.2.2. check if the elements from code_surrounding_ef are in the comments of et and delete event pair if so
            for elem in code_surrounding_ef:
                # if elem in comments_et:
                if any(elem in string for string in comments_et):
                    pair_pruning_events_copy.pop(index)
                    continue

        except:
            print("#########################################################################")
            print("Can not get line number.")

    return pair_pruning_events_copy


def calculate_diff_inserts_deletes_changes(code1: str, code2: str) -> dict:
    """
    function to calculate the diff ratio of two code snippets via levenshtein distance
        need package levenshtein: pip install levenshtein
        using levenshtein editops method: https://rapidfuzz.github.io/Levenshtein/levenshtein.html#editops
            "Find sequence of edit operations transforming one string to another."
            [('delete', 0, 0), ('insert', 3, 2), ('replace', 3, 3)]
    :param code1:
        string with complete code including \n and \t, e.g.:
        ''from numpy import *\n\nx = array(eval(input("Digite o vetor : ")))\n\nm = mean(x)\n\nproduto = 1'
    :param code2:
        string with complete code including \n and \t, e.g.:
        ''from numpy import *\n\nx = array(eval(input("Digite o vetor : ")))\n\nm = mean(x)\n\nproduto = 1'
    :return: dictionary with keys delete, replace & insert, e.g. {'delete': 0, 'replace': 0, 'insert': 3}
    """

    # Find sequence of edit operations transforming one string to another via package levenshtein
    diff_edits = lvs.editops(code1, code2)

    # Initialize counters
    operation_counts = {'delete': 0, 'replace': 0, 'insert': 0}

    # Count occurrences of each operation
    for operation, _, _ in diff_edits:
        operation_counts[operation] += 1

    return operation_counts


"""
4. Error Message Generalization

Remove detailed information of error messages for each pairing: “unknown class - Pet” becomes “unknown class”
=> Not necessary as we already only have the exception names itself

"""


################################################
##             5. Time Estimation             ##
################################################
def time_estimation(all_compilation_events: list, filtered_events: list) -> list:
    """
    Function to get the time spent working on each code snippet
        event pairs ((e1, e2), (e2, e3), ....) are on a per-task basis
        => this would fail to take into account whether a student has spent time working on other files between ef and et
        ==> calculate time based on all compilations h = [h1, h2, ...] for all files in a session ordered by timestamp

    :param all_compilation_events:
        list with all compilation events of one user = [h1, h2, h3, ... ]
        each event is a dictionary with timestamp, success, error_name, line, code
    :param filtered_events:
        list with tuples of events of one user in one file: [(e1, e2), (e4, e5), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    :return:
        list with tuples of events of one user in one file: [(e1, e2, timespan), (e4, e5, timespan), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    """

    # copy of the compilation events to avoid modifying the original data
    all_compilation_events_copy = [{key: value for key, value in event.items()} for event in all_compilation_events]
    filtered_events_copy = [
        ({key: value for key, value in elem[0].items()}, {key: value for key, value in elem[1].items()}) for elem in
        filtered_events]

    # Create a dictionary with days as keys and all corresponding events in that day as a list as value
    all_compilation_events_dict = defaultdict(list)
    for d in all_compilation_events_copy:
        # Extract date from timestamp
        if isinstance(d['timestamp'], str):
            d['timestamp'] = datetime.strptime(d['timestamp'], '%Y-%m-%d %H:%M:%S').timestamp()
            timestamp = datetime.fromtimestamp(d['timestamp'])
        elif isinstance(d['timestamp'], float):
            timestamp = datetime.fromtimestamp(d['timestamp'])
        else:
            timestamp = d['timestamp']
            d['timestamp'] = d['timestamp'].timestamp()

        date = timestamp.strftime('%Y-%m-%d')
        all_compilation_events_dict[date].append(d)
    all_compilation_events_dict = dict(all_compilation_events_dict)

    # Sort all compilation events by timestamp
    for key, value in all_compilation_events_dict.items():
        all_compilation_events_dict[key] = sorted(value, key=lambda x: x['timestamp'])

    # For every (ef, et) check if the timestamp of at least one element of h is in between (ef >  hi > et)), if so:
    for index, elem in enumerate(filtered_events_copy):
        if isinstance(elem[0]['timestamp'], str):
            ef_timestamp = datetime.strptime(elem[0]['timestamp'], '%Y-%m-%d %H:%M:%S').timestamp()
        elif isinstance(elem[0]['timestamp'], pd.Timestamp):
            ef_timestamp = elem[0]['timestamp'].timestamp()
        else:
            ef_timestamp = elem[0]['timestamp']

        if isinstance(elem[1]['timestamp'], str):
            et_timestamp = datetime.strptime(elem[1]['timestamp'], '%Y-%m-%d %H:%M:%S').timestamp()
        elif isinstance(elem[1]['timestamp'], pd.Timestamp):
            et_timestamp = elem[1]['timestamp'].timestamp()
        else:
            et_timestamp = elem[1]['timestamp']

        datetime_ef = datetime.fromtimestamp(ef_timestamp)
        datetime_et = datetime.fromtimestamp(et_timestamp)
        date_ef = datetime_ef.strftime('%Y-%m-%d')
        date_et = datetime_et.strftime('%Y-%m-%d')

        index_ef = find_index_by_timestamp(all_compilation_events_dict[date_ef], ef_timestamp)
        index_et = find_index_by_timestamp(all_compilation_events_dict[date_et], et_timestamp)

        # Events from the same day
        if date_ef == date_et:
            # Consecutive events
            if index_ef == (index_et + 1):
                time = datetime_et - datetime_ef
            # Not consecutive events
            else:
                timestamp_hi = all_compilation_events_dict[date_et][index_et - 1]['timestamp']
                time = datetime_et - datetime.fromtimestamp(timestamp_hi)

        # Events not from the same day
        else:
            if index_et > 0:
                timestamp_hi = all_compilation_events_dict[date_et][index_et - 1]['timestamp']
                time = datetime_et - datetime.fromtimestamp(timestamp_hi)
            else:
                if are_consecutive_dates(date_ef, date_et):
                    index_last_event_date_ef = len(all_compilation_events_dict[date_ef]) - 1
                    if index_ef == index_last_event_date_ef:
                        time = datetime_et - datetime_ef
                    else:
                        timestamp_hi = all_compilation_events_dict[date_ef][index_last_event_date_ef]['timestamp']
                        time = datetime_et - datetime.fromtimestamp(timestamp_hi)
                else:
                    previous_date_found = False
                    current_date = date_et
                    while not previous_date_found:
                        prev_date = get_previous_date(current_date)
                        if prev_date in all_compilation_events_dict:
                            previous_date_found = True
                        current_date = prev_date
                    timestamp_hi = all_compilation_events_dict[prev_date][index_et - 1]['timestamp']
                    time = datetime_et - datetime.fromtimestamp(timestamp_hi)

        filtered_events_copy[index] = (elem[0], elem[1], time)
    return filtered_events_copy


def find_index_by_timestamp(list_of_dicts: list, target_timestamp: str) -> int:
    """
    fucntion to find the index of an event in a list by timestamp ('2023-08-24 06:23:48')
    :param
        list with all compilation events in one session h = [h1, h2, h3, ... ]
        each event is a dictionary with timestamp, success, error_name, line, code
    :param target_timestamp: str with timestamp, e.g. '2023-08-24 06:23:48'
    :return: index of element in list_of_dicts as int
    """
    for index, d in enumerate(list_of_dicts):
        if d['timestamp'] == target_timestamp:
            return index
    return -1  # If the timestamp is not found, return -1


def are_consecutive_dates(date1_str: str, date2_str: str) -> bool:
    """
    function to check if two dates are consecutive or not
    :param date1_str: str with date, e.g. '2023-08-24'
    :param date2_str: str with date, e.g. '2023-08-24'
    :return: boolean
    """
    # Convert string date to datetime object
    if isinstance(date1_str, str) and isinstance(date2_str, str):
        date1 = datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.strptime(date2_str, '%Y-%m-%d').date()
    # Convert string dates to datetime objects
    elif (isinstance(date1_str, float) and isinstance(date2_str, float)) or (
            isinstance(date1_str, int) and isinstance(date2_str, int)):
        date1 = datetime.fromtimestamp(date1_str, "%Y-%m-%d")
        date2 = datetime.fromtimestamp(date2_str, "%Y-%m-%d")

    # Calculate the difference between the dates
    difference = abs(date1 - date2)

    # Check if the difference is exactly one day
    if difference == timedelta(days=1):
        return True
    else:
        return False


def get_previous_date(date_str: str) -> str:
    """
    function to get the previous date of a given one
    :param date_str: str with date, e.g. '2023-08-24'
    :return: str with date, e.g. '2023-08-23'
    """
    # Convert string date to datetime object
    if isinstance(date_str, str):
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    # convert float to datetime object
    elif isinstance(date_str, float) or isinstance(date_str, int):
        date = datetime.fromtimestamp(date_str, "%Y-%m-%d")  # here we used a timestmap object and not a string

    # Subtract one day
    previous_date = date - timedelta(days=1)

    # Convert back to string
    previous_date_str = previous_date.strftime("%Y-%m-%d")

    return previous_date_str


################################################
##             5. Time Estimation             ##
################################################
def get_times_generalized_errors(all_compilation_events_dict: dict) -> dict:
    """
    Calculating the generalized error times for Watwin and RR in each course

    Watwin: 2 MAD_e and mean for all generalized errors over all students in a course
    RR: Q1 and Q3 for all generalized errors over all students in a course

    :param all_compilation_events_dict: dictionary with arbitrary nesting. Innermost value must correspond to a list: [(e1, e2, timespan), (e3, e4, timespan), ...]
        e.g.:  {key_group_1: [(e1, e2, timespan), (e3, e4, timespan), ...], ...}
        each event is a dictionary with timestamp, success, error_name, line, code

    :return: dictionary in form of {key_group_1: {"watwin": {"deviation": two_mad_e_generalized_errors, "mean": mean_generalized_errors}, "rr": {"q1": q1_generalized_errors, "q3": q3_generalized_errors}}, ...}
        two_mad_e_generalized_errors, mean_generalized_errors, q1_generalized_errors & q3_generalized_errors are dicts in form of {"SyntaxError": timedelta, ...}
    """
    generalized_errors_time_spans = find_all_timespans_generalized_errors(all_compilation_events_dict, "error_name")

    ##################
    ##    Watwin    ##
    ##################
    # calculate MAD (median absolute deviation) for each generalized error type
    # 1. calculate mad for each generalized error
    mad_generalized_errors = {key: median_abs_deviation_timedelta(value) for key, value in
                              generalized_errors_time_spans.items()}

    # MAD / 0,6745 is the standard deviation
    # 2. calculate 2 MAD_e for each generalized error
    two_mad_e_generalized_errors = {key: 2 * value / 0.6745 for key, value in mad_generalized_errors.items()}

    # 3. calculate mean for each generalized error
    mean_generalized_errors = {key: mean_timedelta(value) for key, value in generalized_errors_time_spans.items()}

    ############################
    ##    Robuste Realtive    ##
    ############################
    # 1. calculate first quartile
    q1_generalized_errors = {key: percentile(value, .25) for key, value in generalized_errors_time_spans.items()}

    # 2. calculate second quartile
    q3_generalized_errors = {key: percentile(value, .75) for key, value in generalized_errors_time_spans.items()}

    result = {"watwin": {"deviation": two_mad_e_generalized_errors, "mean": mean_generalized_errors},
              "rr": {"q1": q1_generalized_errors, "q3": q3_generalized_errors}}

    return result


def median_abs_deviation_timedelta(data: list) -> timedelta:
    """
    Get median absolute deviation for a given list of datetime.timedelta objects

    :param data: list of datetime.timedelta objects
    :return: datetime.timedelta
    """
    # Convert timedeltas to seconds
    arr_seconds = [td.total_seconds() for td in data]

    # Calculate median
    median_seconds = median(arr_seconds)

    # Calculate absolute deviations
    abs_deviations_seconds = [abs(elem - median_seconds) for elem in arr_seconds]

    # Convert back to timedelta
    abs_deviations_timedelta = [timedelta(seconds=seconds) for seconds in abs_deviations_seconds]

    # Calculate median of absolute deviations
    return median(abs_deviations_timedelta)


def median(data: list) -> timedelta | int | float:
    """
    Get median for a given list of datetime.timedelta objects | integers | floats

    :param data: list of datetime.timedelta objects | integers | floats
    :return: datetime.timedelta | int | float
    """
    sorted_data = sorted(data)

    index = len(sorted_data) * 0.5

    # Number of datapoints is even
    if index.is_integer():
        # get the middle of the two points
        upper_index = int(index)
        lower_index = upper_index - 1
        return (sorted_data[lower_index] + sorted_data[upper_index]) / 2
    else:
        return sorted_data[int(index)]


def percentile(data: list, per: float):
    """
    Function to calculate the percentile of a given list.
    Not usable for classical mean, as for datasets with odd length we d not take the middle of two values

    :param data: list of data points (integers or floats)
    :param per: percentile to be looked for

    :return: int or float with the percentile

    """
    # Sort the data
    sorted_data = sorted(data)

    # Find the index corresponding to the desired percentile
    index = len(sorted_data) * per

    # If the index is an integer, return the corresponding value
    if index.is_integer():
        return sorted_data[int(index - 1)]  # need to take index - 1 due to counting from0 and not from 1

    # If the index is not an integer, interpolate between the values at the nearest indices
    upper_index = int(index)  # need to take int(index) directly due to counting from0 and not from 1

    return sorted_data[upper_index]


def aggregate_error_timespans(events):
    """
    Aggregates timespans between consecutive occurrences of each error type from a list of event dictionaries.
    Should replace the function find_all_timespans_generalized_errors()

    :param events: List of dictionaries, each representing a compilation event with 'timestamp' and 'error_name'.
    :return: A dictionary with error names as keys and lists of timedelta objects as values, representing the timespans
             between consecutive occurrences of each error.
    """
    error_timestamps = {}
    error_timespans = {}

    # First, collect all timestamps for each error type.
    for event in events:
        error_name = event.get("error_name")
        timestamp = event.get("timestamp")

        if error_name and timestamp and error_name != "None":
            if error_name not in error_timestamps:
                error_timestamps[error_name] = []
            error_timestamps[error_name].append(timestamp)

    # Now, calculate the timespans between consecutive timestamps for each error type.
    for error_name, timestamps in error_timestamps.items():
        # Ensure timestamps are sorted to correctly calculate timespans between them.
        timestamps.sort()
        error_timespans[error_name] = []

        for i in range(1, len(timestamps)):
            start_timestamp = timestamps[i - 1]
            end_timestamp = timestamps[i]
            timespan = end_timestamp - start_timestamp
            error_timespans[error_name].append(timedelta(seconds=timespan))

    return error_timespans


def find_all_timespans_generalized_errors(dic: dict, key: str) -> set:
    """
    Get all error types in a given dictionary as well as all timespans to repair this error type

    :param dic: dictionary with arbitrary nesting. Innermost value must correspond to a list: [(e1, e2, timespan), (e3, e4, timespan), ...]
        e.g.:  {key_group_1: [(e1, e2, timespan), (e3, e4, timespan), ...], ...}
        each event is a dictionary with timestamp, success, error_name, line, code
    :param key: str with key name looking for
    :return: dictionary with all founded values of given key als key and all timespans of corresponding key
        {"NameError": [timedelta, timedelta, ...], ...}
    """
    timespans = {}

    # function for collecting unique values for the key 'key'
    def collect_unique_values(dictionary: dict):
        for value in dictionary.values():
            if isinstance(value, dict):
                collect_unique_values(value)
            if isinstance(value, list):
                for event_tuple in value:
                    if key in event_tuple[0].keys():
                        error_name = event_tuple[0][key]
                        if error_name not in timespans:
                            timespans[error_name] = []
                        # event_tuple[2] is the time for reparing this error
                        timespans[error_name].append(event_tuple[2])

    # Call the function to collect unique values for each nested dictionary
    collect_unique_values(dic)

    return timespans


def mean_timedelta(timedelta_list: list) -> timedelta:
    """
    Clculate the mean (average) of a list with timedeltas. statistics.mean can not work with timedeltas

    :param timedelta_list: list with timedeltas
    :return: mean of all value in timedelta_list
    """
    # Convert timedeltas to total seconds
    total_seconds = sum(td.total_seconds() for td in timedelta_list)

    # Calculate the average in seconds
    average_seconds = total_seconds / len(timedelta_list)

    # Convert average back to timedelta
    average_timedelta = timedelta(seconds=average_seconds)

    return average_timedelta


################################################
################################################
##         Quantify Programming Behaviour     ##
################################################
################################################
def calculate_watwin_and_rr(compilation_events: list, times_generalized_errors: dict) -> tuple:
    """
    function to calculate both watwin and robuste relative score for a given list of compilation events:
        1. calculate scores for each event (ef, et, timespan)
        2. normalize each score
        3. get the average of all scores
    :param compilation_events:
        list with tuples of events of one user in one file: [(e1, e2, timespan), (e4, e5, timespan), .....]
        each event is a dictionary with timestamp, success, error_name, line, code
    :param times_generalized_errors:
    :return: tuple with numbers: watwin_score, robuste_relative_score
    """
    all_scores_watwin = []
    all_scores_rr = []
    if len(compilation_events) > 0:
        for index, elem in enumerate(compilation_events):
            score_watwin, score_rr = calculate_score_for_pairs_for_watwin_and_rr(elem[0], elem[1], elem[2],
                                                                                 times_generalized_errors)
            score_watwin, score_rr = normalize_scores_watwin_rr(score_watwin, score_rr)
            all_scores_watwin.append(score_watwin)
            all_scores_rr.append(score_rr)
        average_watwin, average_rr = average_watwin_rr(all_scores_watwin, all_scores_rr)
        return average_watwin, average_rr
    return 0, 0


def calculate_score_for_pairs_for_watwin_and_rr(event_ef: dict, event_et: dict, time_resolve_ef: timedelta,
                                                times_generalized_errors: dict) -> tuple:
    """
    function to calculates the score for a given pair of events for watwin and / or robust relative algorithm
        1. frequency scoring
        2. time scoring: error resolve times are compared to a group of similar errors

    :param event_ef: first event as dict with timestamp, success, error_name, line, code
    :param event_et: second event as dict with timestamp, success, error_name, line, code
    :param time_resolve_ef: timedelta of solving first event
    :param times_generalized_errors:
        dictionary with 2 MAD_e and mean for watwin and Q1 and Q3 for robuste relative for all generalized errors:
        {"watwin": {"deviation": two_mad_e_generalized_errors, "mean": mean_generalized_errors},
         "rr": {"q1": q1_generalized_errors, "q2": q2_generalized_errors}}
    :return: tuple with two integers: score_watwin, score_rr
    """
    score_watwin = 0
    score_rr = 0

    # 1. frequency scoring
    # both events have an error
    try:
        if (event_ef["success"] == "False" and event_et["success"] == "False") or \
                (event_ef["success"] == False and event_et["success"] == False):
            # same full error message
            if event_ef["error_name"] == event_et["error_name"]:
                score_watwin += 4
                score_rr += 1
            # same generalised error message
            if event_ef["error_name"] == event_et["error_name"]:
                score_watwin += 4
                score_rr += 5
            # same line
            if (event_ef['task_id'] == event_et['task_id']) and (event_ef['error_line'] == event_et['error_line']):
                score_watwin += 2
                score_rr += 2
    except Exception as e:
        print("event_ef", event_ef)
        print("event_et", event_et)
        raise Exception()

    # 2. time scoring
    # first event has an error, second event not OR both events have an error
    if (event_ef["success"] == "False" and event_et["success"] == "False") or \
            (event_ef["success"] == "False" and event_et["success"] == "True") or \
            (event_ef["success"] == False and event_et["success"] == False) or \
            (event_ef["success"] == False and event_et["success"] == True):
        generalized_error_ef = event_ef["error_name"]

        ##################
        ##    Watwin    ##
        ##################
        if time_resolve_ef < (times_generalized_errors["watwin"]["mean"][generalized_error_ef] -
                              times_generalized_errors["watwin"]["deviation"][generalized_error_ef]):
            score_watwin += 1
        elif time_resolve_ef > (times_generalized_errors["watwin"]["mean"][generalized_error_ef] -
                                times_generalized_errors["watwin"]["deviation"][generalized_error_ef]):
            score_watwin += 25
        else:
            score_watwin += 15

        ############################
        ##    Robuste Realtive    ##
        ############################
        if time_resolve_ef <= times_generalized_errors["rr"]["q1"][generalized_error_ef]:
            score_rr += 3
        elif time_resolve_ef >= times_generalized_errors["rr"]["q3"][generalized_error_ef]:
            score_rr += 8
        else:
            score_rr += 5

    return score_watwin, score_rr


def normalize_scores_watwin_rr(score_watwin: int, score_rr: int) -> tuple:
    return score_watwin / 35, score_rr / 16


def average_watwin_rr(scores_watwin: list, scores_rr: list) -> tuple:
    return statistics.mean(scores_watwin), statistics.mean(scores_rr)
