# pyerrormetrics

pyerrormetrics is a library designed to calculate different error metrics (Error Quotient, Repeated Error Density, Watwin Algorithm) for a given set of python code executions.

The calculation can take place at different levels:
- user: data is aggregated per user
- user task: data is aggregated across all tasks of a user
- user session: data is aggregated across all sessions of a user
- user task session: data is aggregated across all tasks and sessions of a user

A session is defined as any sequence of consecutive events occurring within a 20-minute interval.

*IMPORTANT: 
A user always refers to one course. 
Therefore, if a user appears in several courses, it is considered separately for each course.
The calculation is therefore always carried out at course level.*

## Installation

### Via PyPi
``pip install pyerrormetrics``

### Without PyPi
1. Clone repository
2. Open Terminal and change directory to the cloned repository
3. Generate distribution archives on local machine: ``python setup.py sdist bdist_wheel``
4. Install the package on local machine: ``pip install .`` <br>  Alternatively, you can also install it in development mode: ``pip install -e .``

## Usage of pyerrormetrics
To use the methods from pyerrormetrics, you can either hand over a pandas DataFrame or a dictionary to the methods `error_quotient`, `repeated_error_density` and `watwin`.

### Handing over a pandas DataFrame
The pandas DataFrame should have at least the columns:
- course_id: str
- user_id: str
- task_id: str
- timestamp: str
- input_code: str
- success: bool
- error_name: str
- error_line: int

Furthermore, you can have more column to presort your data for yourself, e.g.:
- output
- environment
- language
- version


````python
import pyerrormetrics

# data is a pandas Dataframe with columns "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"
eq = pyerrormetrics.error_quotient(data, "user session")
red = pyerrormetrics.repeated_error_density(data, "user session")
watwin, rr = pyerrormetrics.watwin(data, "user session")

````

### Handing over a dictionary
The dictionary structure to be handed over depends on the analysis level:
- user level & user task level: <br>
  - Structure: `{key_group_1: [{'user_id': str, 'course_id': str, 'task_id': str, 'timestamp': str, 'input_code': str, 'success': bool, 'error_name': str, 'error_line': int}, ...], ...} `
  - Example: `{('C001', 'U001', 1): [{'user_id': 'U001', 'course_id': 'C001', 'task_id': 'T001', 'timestamp': '2024-04-01 10:00:00', 'input_code': 'print("Hello, world!")', 'success': False, 'error_name': 'a', 'error_line': 1}]}`
- user session level & user task session level: <br>
  - Structure: `{key_group_1: [{'user_id': str, 'course_id': str, 'task_id': str, 'timestamp': str, 'input_code': str, 'success': bool, 'error_name': str, 'error_line': int, 'session': int}, ...], ...} `
  - Example: `{('C001', 'U001', 1): [{'user_id': 'U001', 'course_id': 'C001', 'task_id': 'T001', 'timestamp': '2024-04-01 10:00:00', 'input_code': 'print("Hello, world!")', 'success': False, 'error_name': 'a', 'error_line': 1, 'session': 1}]}`

Similar to the dataframe you can have more keys for each event, e.g. `output`, `environment`, `language` or `version`, to presort your data beforehand.

The dictionary needs to be already correctly formatted, e.g. in terms of the analysis level.

Due to time performance you can prepare and turn your pandas DataFrame into a dict beforehand only once, e.g. if you want to calculate more than one error metric:
````python
import pyerrormetrics

# data is a pandas Dataframe with columns "course_id", "user_id", "task_id", "environment", "language", "version", "timestamp", "input_code", "output", "success", "error_name", "error_line"
prepared_df_dict_user_session = pyerrormetrics.convert_dataframe_groups_into_dict(pyerrormetrics.prepare_dataframes(data, "user session"))

# prepared_df_dict_user_session is a dict with {key_group_1: [{event1}, {event2}, {event3}], key_group_2: [{event1}, {event2}], ...}
eq = pyerrormetrics.error_quotient(prepared_df_dict_user_session, "user session")
red = pyerrormetrics.repeated_error_density(prepared_df_dict_user_session, "user session")
watwin, rr = pyerrormetrics.watwin(prepared_df_dict_user_session, "user session")
````

### Available functions:
- `error_quotient`
- `repeated_error_density`
- `watwin`
- `prepare_dataframes`
- `convert_dataframe_groups_into_dict`


## Testing

### Unittests
```
python -m unittest discover tests "*_test.py"
```

### Performance
```
python -m cProfile -o <xyz>.txt <file>.py
python -m snakeviz <xyz>.txt
```