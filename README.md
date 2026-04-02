# PythonProject

## Class Selector Framework

Main script: Python Project.py

Data files:
- ju_catalog.json (existing class catalog)

### What this shell already does
- Loads the catalog from JSON.
- Asks for student name, major, year, semester.
- Shows classes by major.
- Lets student choose classes by course code.
- Checks simple credit-hour max limit.

### What your team should fill in
In Python Project.py, these functions are intentionally left as placeholders with pass:
- validate_student_profile(...)
- load_student_history(...)
- build_prerequisite_map(...)
- check_prerequisites(...)
- check_year_semester_restrictions(...)
- check_schedule_conflicts(...)
- check_capacity_limits(...)
- save_registration_result(...)

Each placeholder includes a plain-language goal in its docstring/comments.

### Run
```bash
python "Python Project.py"
```

### Team checklist
1. Confirm ju_catalog.json has the data your checks need.
2. Implement validate_student_profile(...) so inputs are clean.
3. Implement load_student_history(...) so completed classes are known.
4. Implement build_prerequisite_map(...) from available JSON fields.
5. Implement check_prerequisites(...) using completed classes.
6. Implement check_year_semester_restrictions(...) for eligibility.
7. Implement check_schedule_conflicts(...) if time data exists.
8. Implement check_capacity_limits(...) if seat counts exist.
9. Implement save_registration_result(...) to store output.
10. Uncomment the TODO lines in run_selector_shell() after each function is ready.

### Notes
1. This project now uses only ju_catalog.json as the required JSON file.
2. Keep the code general and avoid hardcoding per-course logic when possible.
