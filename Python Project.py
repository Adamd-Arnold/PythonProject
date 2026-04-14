from course_list import COURSE_CATALOG

student_year = ""
student_major = ""
completed_courses = []
selected_courses = []

major_names = [
    "Accounting", "Aviation", "Biology", "Business", "Communication",
    "Computer Science", "Criminal Justice", "Cybersecurity", "Economics",
    "Education", "Engineering", "English", "Exercise Science", "Finance",
    "General Studies", "Management", "Marine Science", "Marketing", "Music",
    "Nursing", "Philosophy", "Political Science", "Psychology"
]



def year_rank(year):
    order = {
        "Rising Freshman": 0,
        "Freshman": 1,
        "Sophomore": 2,
        "Junior": 3,
        "Senior": 4
    }
    return order.get(year, -1)



def print_course(course):
    print(f"Course: {course['name']}, {course['code']}")
    print(f"Taught by: {course['prof']}, {course['credits']} credits\n")



def export_selected_classes(selected_courses, completed_courses):
    file_name = "student_selection_export.txt"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"Year: {student_year}\n")
        f.write(f"Major: {student_major}\n\n")

        f.write("Future Courses:\n")
        for c in selected_courses:
            f.write(f"{c['code']} - {c['name']} ({c['year']})\n")

        f.write("\nCompleted Courses:\n")
        for c in completed_courses:
            f.write(f"{c['code']} - {c['name']} ({c['year']})\n")

    print(f"\nExported to {file_name}\n")


def set_student_info():
    global student_year, student_major

    print("\n--- Enter Info ---\n")

    student_year = input(
        "Year (Rising Freshman, Freshman, Sophomore, Junior, Senior): "
    ).strip().title()

    major_input = input(
        "Major number (? for list): "
    ).strip()

    if major_input == "?":
        print_majors()
        major_input = input("Major number: ").strip()

    try:
        index = int(major_input)
        student_major = major_names[index]
    except (ValueError, IndexError):
        print("Invalid major selection. Defaulting to Accounting.")
        student_major = "Accounting"


# Major List
def print_majors():
    for i, major in enumerate(major_names):
        print(f"{i}. {major}")


#List of Courses

courses = {
   
    "Aviation": [
        {"code": "AVI 101", "name": "Introduction to Aviation", "prof": "James Carter", "credits": 3, "year": "Freshman"},
        {"code": "AVI 120", "name": "Private Pilot Ground School", "prof": "Elena Brooks", "credits": 3, "year": "Sophomore"},
        {"code": "AVI 230", "name": "Instrument Flight Theory", "prof": "Marcus Reed", "credits": 3, "year": "Junior"},
        {"code": "AVI 310", "name": "Aviation Safety", "prof": "Dana Mitchell", "credits": 4, "year": "Senior"},
        {"code": "AVI 360", "name": "Air Traffic Systems", "prof": "Aaron Phillips", "credits": 4, "year": "Senior"},
    ],

    "Biology": [
        {"code": "BIO 110", "name": "Principles of Biology I", "prof": "Hannah Cole", "credits": 3, "year": "Freshman"},
        {"code": "BIO 111", "name": "Principles of Biology II", "prof": "Victor Lane", "credits": 3, "year": "Sophomore"},
        {"code": "BIO 220", "name": "Genetics", "prof": "Priya Menon", "credits": 3, "year": "Junior"},
        {"code": "BIO 330", "name": "Microbiology", "prof": "Samuel Ortiz", "credits": 4, "year": "Senior"},
        {"code": "BIO 410", "name": "Ecology", "prof": "Rachel Kim", "credits": 4, "year": "Senior"},
    ],

    "Business": [
        {"code": "BUS 101", "name": "Introduction to Business", "prof": "Lauren Hayes", "credits": 3, "year": "Freshman"},
        {"code": "ACC 201", "name": "Financial Accounting", "prof": "Michael Grant", "credits": 3, "year": "Sophomore"},
        {"code": "ECO 201", "name": "Microeconomics", "prof": "Nina Wallace", "credits": 3, "year": "Junior"},
        {"code": "MKT 301", "name": "Principles of Marketing", "prof": "Derek Sullivan", "credits": 4, "year": "Senior"},
        {"code": "FIN 320", "name": "Corporate Finance", "prof": "Olivia Turner", "credits": 4, "year": "Senior"},
    ],

    "Engineering": [
        {"code": "ENG 101", "name": "Introduction to Engineering", "prof": "David Wright", "credits": 3, "year": "Freshman"},
        {"code": "ENG 201", "name": "Engineering Graphics", "prof": "Jennifer Lopez", "credits": 3, "year": "Sophomore"},
        {"code": "ENG 301", "name": "Thermodynamics", "prof": "Robert Hill", "credits": 4, "year": "Junior"},
        {"code": "ENG 401", "name": "Capstone Design Project", "prof": "Amanda Scott", "credits": 4, "year": "Senior"},
    ],

    "Finance": [
        {"code": "FIN 301", "name": "Principles of Finance", "prof": "Olivia Turner", "credits": 3, "year": "Junior"},
        {"code": "FIN 320", "name": "Corporate Finance", "prof": "Olivia Turner", "credits": 4, "year": "Senior"},
        {"code": "FIN 330", "name": "Investments", "prof": "Ethan Baker", "credits": 4, "year": "Senior"},
        {"code": "FIN 410", "name": "Financial Markets", "prof": "Sophia Wilson", "credits": 4, "year": "Senior"},
        {"code": "FIN 420", "name": "International Finance", "prof": "Liam Davis", "credits": 4, "year": "Senior"},
    ],

    "Accounting": [
        {"code": "ACC 201", "name": "Financial Accounting", "prof": "Michael Grant", "credits": 3, "year": "Freshman"},
        {"code": "ACC 202", "name": "Managerial Accounting", "prof": "Lauren Hayes", "credits": 3, "year": "Sophomore"},
        {"code": "ACC 310", "name": "Intermediate Accounting I", "prof": "Trevor Adams", "credits": 3, "year": "Junior"},
        {"code": "ACC 311", "name": "Intermediate Accounting II", "prof": "Diana Brooks", "credits": 4, "year": "Senior"},
        {"code": "ACC 420", "name": "Auditing", "prof": "Henry Collins", "credits": 4, "year": "Senior"},
    ],

    "Computer Science": [
        {"code": "CS 110", "name": "Introduction to Programming", "prof": "Isaac Flores", "credits": 3, "year": "Freshman"},
        {"code": "CS 220", "name": "Data Structures", "prof": "Chloe Bennett", "credits": 3, "year": "Sophomore"},
        {"code": "CS 230", "name": "Computer Organization", "prof": "Noah Perry", "credits": 3, "year": "Junior"},
        {"code": "CS 310", "name": "Algorithms", "prof": "Emma Stewart", "credits": 4, "year": "Senior"},
        {"code": "CS 340", "name": "Database Systems", "prof": "Lucas Rivera", "credits": 4, "year": "Senior"},
    ],

    "Cybersecurity": [
        {"code": "CYB 210", "name": "Introduction to Cybersecurity", "prof": "Ethan Clark", "credits": 3, "year": "Freshman"},
        {"code": "CYB 220", "name": "Network Security", "prof": "Maya Peterson", "credits": 3, "year": "Sophomore"},
        {"code": "CYB 310", "name": "Ethical Hacking", "prof": "Jason Reed", "credits": 3, "year": "Junior"},
        {"code": "CYB 320", "name": "Digital Forensics", "prof": "Natalie Gray", "credits": 4, "year": "Senior"},
        {"code": "CYB 410", "name": "Security Operations", "prof": "Owen King", "credits": 4, "year": "Senior"},
    ],

    "Psychology": [
        {"code": "PSY 101", "name": "Introduction to Psychology", "prof": "Anna Bell", "credits": 3, "year": "Freshman"},
        {"code": "PSY 220", "name": "Developmental Psychology", "prof": "Dylan Hunter", "credits": 3, "year": "Sophomore"},
        {"code": "PSY 230", "name": "Abnormal Psychology", "prof": "Megan Fox", "credits": 3, "year": "Junior"},
        {"code": "PSY 310", "name": "Cognitive Psychology", "prof": "Isaac Reed", "credits": 4, "year": "Senior"},
        {"code": "PSY 340", "name": "Research Methods", "prof": "Claire Wood", "credits": 4, "year": "Senior"},
    ]
}


# ---------------- START ----------------
set_student_info()

# FINAL SAFETY CHECK (FIXES YOUR LINE 174 ERROR)
if student_major not in courses:
    print("Major not found in course catalog. Defaulting to Accounting.")
    student_major = "Accounting"


# ---------------- MENU ----------------
menu = """
1. Courses this year
2. All major courses
3. Full catalog
4. Save completed courses
5. Future courses
(* to exit)
"""

choice = input(menu).strip()


# ---------------- LOOP ----------------
while choice != "*":

    # 1 - YEAR COURSES
    if choice == "1":
        print("\n--- Courses this year ---\n")
        selected_courses = []

        for c in courses[student_major]:
            if c["year"] == student_year:
                print_course(c)
                selected_courses.append(c)

    # 2 - ALL MAJOR
    elif choice == "2":
        print("\n--- Major courses ---\n")
        for c in courses[student_major]:
            print_course(c)

    # 3 - ALL COURSES
    elif choice == "3":
        print("\n--- Full catalog ---\n")
        for major in courses:
            for c in courses[major]:
                print_course(c)

    # 4 - COMPLETED
    elif choice == "4":
        print("\n--- Eligible courses ---\n")
        eligible = []

        for c in courses[student_major]:
            if year_rank(c["year"]) <= year_rank(student_year):
                print_course(c)
                eligible.append(c)

        code = ""
        while code != "*":
            code = input("Enter course code (* to quit): ").strip().upper()

            if code == "*":
                break

            found = False

            for c in eligible:
                if c["code"].upper() == code:
                    found = True
                    if c not in completed_courses:
                        completed_courses.append(c)
                        print("Added:", c["name"])
                    else:
                        print("Already completed.")

            if not found:
                print("Not found.")

    # 5 - FUTURE
    elif choice == "5":
        print("\n--- Future courses ---\n")
        selected_courses = []

        for c in courses[student_major]:
            if year_rank(c["year"]) > year_rank(student_year):
                selected_courses.append(c)
                print_course(c)

        export_selected_classes(selected_courses, completed_courses)

    else:
        print("Invalid option.")

    choice = input(menu).strip()


# END
# Do not export again on exit: option 5 already exports future courses,
# and exporting here can overwrite that file with a non-future selection.
print("\nGoodbye!\n")
