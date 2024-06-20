def calculate_red(S):
    """
    Calculate the Repeated Error Density (RED) for a given sequence of error occurrences.

    This function computes the RED score, which is a measure of the density of repeated errors
    in a sequence of programming error events. The RED score is calculated by summing the
    squares of the number of repeated errors divided by one plus the number of repeated errors
    for each element in the sequence.

    Parameters:
    S (list): A list of integers where each integer represents the number of times a specific
              error is consecutively repeated in the sequence.

    Returns:
    float: The calculated RED score for the given sequence of error occurrences.
    """
    red = 0
    for elem in S:
        red += (elem * elem) / (elem + 1)
    return red


def sanitize_events_for_red(tup):
    """
    Prepare a sequence of error events for RED calculation by sanitizing the input data.

    This function processes a tuple of error events, converting it into a list where each element
    represents the number of consecutive repetitions of the same error, excluding 'None' errors.
    It is used to transform raw error data into a format that is suitable for calculating the RED score.

    Parameters:
    tup (tuple): A tuple containing error names or identifiers, where each element represents an
                 error event in the order they occurred.

    Returns:
    list: A list of integers where each integer represents the number of consecutive times an error
          is repeated in the sequence, not counting 'None' errors.
    """
    results = []
    count = 0

    for i in range(len(tup)):
        if tup[i] == "None" or tup[i] == None:
        # If the current error is 'None', reset the count and continue to the next iteration
            results.append(count)
            count = 0
            continue

        if i < len(tup) - 1 and tup[i] == tup[i + 1]:
            count += 1
        else:
            results.append(count)
            count = 0

    return results


def convert_to_tuple(dict_list):
    return tuple(d['error_name'] for d in dict_list)