"""Class selector CLI using ju_catalog.json."""

import json
from pathlib import Path
from typing import Any


CATALOG_PATH = Path("ju_catalog.json")
MAX_CREDITS = 18
DEFAULT_COURSE_CREDITS = 3

VALID_YEARS = {1, 2, 3, 4}
VALID_SEMESTERS = {"fall", "spring", "summer"}
YEAR_TO_TERM_KEYS = {1: {"1", "2"}, 2: {"3", "4"}, 3: {"5", "6"}, 4: {"7", "8"}}


def load_json_data(file_path: Path) -> dict[str, Any]:
    return json.loads(file_path.read_text(encoding="utf-8")) if file_path.exists() else {}


def normalize_text(value: str) -> str:
    return value.strip().lower()


def course_title(value: Any, code: str) -> str:
    return value if isinstance(value, str) else value.get("title", code) if isinstance(value, dict) else code


def iter_course_entries(
    raw_catalog: dict[str, Any],
    *,
    target_major: str | None = None,
    allowed_terms: set[str] | None = None,
):
    """Yield (CODE, value) entries from nested catalog with optional filters."""
    for college_data in raw_catalog.values():
        if not isinstance(college_data, dict):
            continue
        for major_name, semester_data in college_data.items():
            if target_major and normalize_text(major_name) != target_major:
                continue
            if not isinstance(semester_data, dict):
                continue
            for term_key, courses in semester_data.items():
                if allowed_terms and str(term_key) not in allowed_terms:
                    continue
                if not isinstance(courses, dict):
                    continue
                for code, value in courses.items():
                    yield code.strip().upper(), value


def normalize_catalog(raw_catalog: dict[str, Any]) -> dict[str, dict[str, str]]:
    catalog: dict[str, dict[str, str]] = {}
    for college_data in raw_catalog.values():
        if not isinstance(college_data, dict):
            continue
        for major_name, semester_data in college_data.items():
            if not isinstance(semester_data, dict):
                continue
            major = normalize_text(major_name)
            major_courses = catalog.setdefault(major, {})
            for courses in semester_data.values():
                if not isinstance(courses, dict):
                    continue
                for code, value in courses.items():
                    code_key = code.strip().upper()
                    major_courses.setdefault(code_key, course_title(value, code_key))
    return catalog


def prompt_name() -> str:
    while True:
        name = input("Step 1 - Enter your name: ").strip()
        if name:
            return name
        print("Name is required.")


def prompt_major(majors: list[str]) -> str:
    print("\nStep 2 - Choose your major")
    print("Available majors:")
    print(", ".join(majors[:12]))
    while True:
        major = normalize_text(input("Type major exactly as shown: "))
        if major in majors:
            return major
        print("Major not found. Please type one from the list.")


def prompt_year() -> int:
    while True:
        text = input("Step 3 - Year (1-4): ").strip()
        if text.isdigit() and int(text) in VALID_YEARS:
            return int(text)
        print("Enter 1, 2, 3, or 4.")


def prompt_semester() -> str:
    while True:
        semester = normalize_text(input("Step 4 - Semester (fall/spring/summer): "))
        if semester in VALID_SEMESTERS:
            return semester
        print("Enter fall, spring, or summer.")


def prompt_completed_courses() -> list[str]:
    print("\nStep 5 - Enter completed courses")
    raw = input("Completed courses (comma-separated, blank if none): ").strip()

    unique_codes: list[str] = []
    seen: set[str] = set()
    for item in raw.split(","):
        code = item.strip().upper()
        if not code or code in seen:
            continue
        seen.add(code)
        unique_codes.append(code)

    return unique_codes


def prompt_selected_course_codes(major_courses: dict[str, str]) -> list[str]:
    options = list(major_courses.items())
    if not options:
        return []

    print("\nStep 6 - Choose classes")
    print("Available courses for your major and year:")
    for i, (code, title) in enumerate(options[:25], start=1):
        print(f"{i}. {title} ({code})")

    print("\nEnter numbers from the list (example: 1,3,5).")
    print("You can also enter class codes if you want.")

    raw = input("Select classes: ").strip()
    while not raw:
        print("Please enter at least one selection.")
        raw = input("Select classes: ").strip()

    index_to_code = {str(i): code for i, (code, _) in enumerate(options, start=1)}
    selected: list[str] = []
    seen: set[str] = set()
    invalid: list[str] = []

    for token in (part.strip() for part in raw.split(",")):
        if not token:
            continue
        code = index_to_code.get(token) if token.isdigit() else token.upper()
        if code in major_courses and code not in seen:
            seen.add(code)
            selected.append(code)
        elif code not in major_courses:
            invalid.append(token)

    if invalid:
        print("Ignored invalid selections:", ", ".join(invalid))
    return selected


def get_major_courses_for_year(raw_catalog: dict[str, Any], major: str, year: int) -> dict[str, str]:
    allowed_terms = YEAR_TO_TERM_KEYS.get(year, set())
    return {
        code: course_title(value, code)
        for code, value in iter_course_entries(raw_catalog, target_major=major, allowed_terms=allowed_terms)
    }


def build_selected_courses(major_courses: dict[str, str], selected_codes: list[str]) -> list[dict[str, Any]]:
    return [
        {"code": code, "title": major_courses[code], "credit_hours": DEFAULT_COURSE_CREDITS}
        for code in selected_codes
        if code in major_courses
    ]


def validate_student_input(student: dict[str, Any]) -> list[str]:
    name = str(student.get("name", "")).strip()
    major = str(student.get("major", "")).strip()
    year = student.get("year")
    semester = normalize_text(str(student.get("semester", "")))
    issues: list[str] = []
    if not name:
        issues.append("Name is required.")
    if not major:
        issues.append("Major is required.")
    if not isinstance(year, int) or year not in VALID_YEARS:
        issues.append("Year must be 1, 2, 3, or 4.")
    if semester not in VALID_SEMESTERS:
        issues.append("Semester must be fall, spring, or summer.")
    return issues


def calculate_total_credits(selected_courses: list[dict[str, Any]]) -> int:
    return sum(int(course.get("credit_hours", 0)) for course in selected_courses)


def check_credit_limit(selected_courses: list[dict[str, Any]], max_credits: int = MAX_CREDITS) -> list[str]:
    total = calculate_total_credits(selected_courses)
    return [f"Credit limit exceeded: {total}/{max_credits}"] if total > max_credits else []


def build_prerequisite_map(raw_catalog: dict[str, Any]) -> dict[str, list[str]]:
    prereq_map: dict[str, list[str]] = {}
    for code, value in iter_course_entries(raw_catalog):
        if not isinstance(value, dict):
            continue
        prerequisites = value.get("prerequisites")
        if isinstance(prerequisites, list):
            prereq_map[code] = [str(item).strip().upper() for item in prerequisites if str(item).strip()]
    return prereq_map


def check_prerequisites(
    selected_courses: list[dict[str, Any]],
    completed_courses: list[str],
    prereq_map: dict[str, list[str]],
) -> list[str]:
    issues: list[str] = []
    completed = {code.strip().upper() for code in completed_courses if code.strip()}
    for course in selected_courses:
        code = str(course.get("code", "")).strip().upper()
        missing = [req for req in prereq_map.get(code, []) if req not in completed]
        if missing:
            issues.append(f"Cannot take {code}. Missing prerequisites: {', '.join(missing)}")
    return issues


def save_results(student: dict[str, Any], selected_courses: list[dict[str, Any]], issues: list[str]) -> None:
    output = {
        "student": student,
        "selected_courses": selected_courses,
        "total_credits": calculate_total_credits(selected_courses),
        "max_credits": MAX_CREDITS,
        "status": "Available" if not issues else "Not available",
        "issues": issues,
    }
    Path("selection_result.json").write_text(json.dumps(output, indent=2), encoding="utf-8")


def print_result(student: dict[str, Any], selected_courses: list[dict[str, Any]], issues: list[str]) -> None:
    total_credits = calculate_total_credits(selected_courses)
    print("\n=== Result ===")
    print(f"Student: {student['name']}")
    print(f"Major: {student['major']}")
    print(f"Year: {student['year']}")
    print(f"Semester: {student['semester']}")
    print("Selected classes:")
    for course in selected_courses:
        print(f"- {course['code']}: {course['title']}")
    print("Status: Available" if not issues else "Status: Not available")
    for issue in issues:
        print(f"- {issue}")
    print(f"Classes selected: {len(selected_courses)}")
    print(f"Total credits: {total_credits}/{MAX_CREDITS}")


def run() -> None:
    raw_catalog = load_json_data(CATALOG_PATH)
    majors = sorted(normalize_catalog(raw_catalog))
    if not majors:
        print("No majors found in ju_catalog.json.")
        return

    print("=== Class Selector ===")
    print("Follow each step. Keep inputs simple.")

    student = {
        "name": prompt_name(),
        "major": prompt_major(majors),
        "year": prompt_year(),
        "semester": prompt_semester(),
        "completed_courses": prompt_completed_courses(),
    }

    major_courses = get_major_courses_for_year(raw_catalog, student["major"], student["year"])
    if not major_courses:
        print("No courses found for this major in the selected year.")
        return

    selected_courses = build_selected_courses(major_courses, prompt_selected_course_codes(major_courses))
    if not selected_courses:
        print("No valid course codes were selected.")
        return

    issues = [
        *validate_student_input(student),
        *check_credit_limit(selected_courses),
        *check_prerequisites(selected_courses, student["completed_courses"], build_prerequisite_map(raw_catalog)),
    ]

    print_result(student, selected_courses, issues)
    save_results(student, selected_courses, issues)


if __name__ == "__main__":
    run()
