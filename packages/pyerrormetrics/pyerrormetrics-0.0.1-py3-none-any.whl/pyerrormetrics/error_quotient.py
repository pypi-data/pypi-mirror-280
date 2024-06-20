def calculate_score_for_pairs_error_quotient(event1: dict, event2: dict) -> int:
    """
    Calculates Error Quotient Score for a given pair of events.

    :param event1: dict containing data for first event
    :param event2: dict containing data for second even
    :return int
    """
    score = 0
    # both events end up in an error
    if event1['success'] == False and event2['success'] == False:
        score += 2
    else:
        return 0
    # both events have same error type
    if event1['error_name'] == event2['error_name']:
        score += 3
    # both errors occur in same location
    if (event1['task_id'] == event2['task_id']) and (event1['error_line'] == event2['error_line']):
        score += 3
    # change from ef to et is at the same location
    # T.B.D.
    # if event1["line"] == event2["line"]:
    #    score += 1
    return score


def calculate_score_for_pairs_error_quotient_two_params(event1: dict, event2: dict) -> int:
    """
    Calculates Two Params Error Quotient Score for a given pair of events.

    :param event1: dict containing data for first event
    :param event2: dict containing data for second even
    :return int
    """
    score = 0
    # both events end up in an error
    if event1['success'] == False and event2['success'] == False:
        score += 8
    else:
        return 0
    # both events have same error type
    if event1['error_name'] == event2['error_name']:
        score += 3
    return score


def calculate_total_score_error_quotient(events: list) -> tuple:
    """
    Calculates the total Error Quotient score for a sequence of events.
    Total score is the sum of individual scores.

    :param events: list of events. Each event is a dictionary
    :return tuple containing nominator and denominator (total_score, num_pairs * 8)
    """
    total_score = 0
    num_pairs = len(events) - 1
    for i in range(num_pairs):
        total_score += calculate_score_for_pairs_error_quotient(events[i], events[i + 1])
    return total_score, num_pairs * 8


def calculate_total_score_error_quotient_two_params(events):
    """
    Calculates the total Two Params Error Quotient score for a sequence of events.
    Total score is the sum of individual scores.

    :param events: list of events. Each event is a dictionary
    :return tuple containing nominator and denominator (total_score, num_pairs * 11)
    """
    total_score_two_params = 0
    num_pairs = len(events) - 1
    for i in range(num_pairs):
        total_score_two_params += calculate_score_for_pairs_error_quotient_two_params(events[i], events[i + 1])
    return total_score_two_params, num_pairs * 11
