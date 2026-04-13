## Course Catalogue in Python Using Dictionaries
from course_list import COURSE_CATALOG

## Make a tuple of all the course dictionaries for easy access
course_catalogue = tuple(COURSE_CATALOG.values())
course_catalogue_index = list(course_catalogue)


student_year = ""
student_major = ""
major_names = ["Accounting", "Aviation", "Biology", "Business", "Communication", "Computer Science", "Criminal Justice", "Cybersecurity", "Economics", "Education", "Engineering", "English", "Exercise Science", "Finance", "General Studies", "Management", "Marine Science", "Marketing", "Music", "Nursing", "Philosophy", "Political Science", "Psychology"]
course_code = ""
completed_courses = []
selected_courses = []


def year_rank(year):
    if year == "Rising Freshman":
        return 0
    if year == "Freshman":
        return 1
    if year == "Sophomore":
        return 2
    if year == "Junior":
        return 3
    if year == "Senior":
        return 4
    return -1


def export_selected_classes(selected_courses, completed_courses): #Text file of selected classes
    export_file_name = "student_selection_export.txt"
    with open(export_file_name, "w", encoding="utf-8") as export_file:
        export_file.write("Student Class Selection Export\n")
        export_file.write("=" * 32 + "\n")
        export_file.write(f"Year: {student_year}\n")
        export_file.write(f"Major: {major_names[int(student_major)]}\n\n")
        export_file.write("Future Courses:\n")

        print("Future Courses:\n")
        if not selected_courses:
            export_file.write("- No courses selected.\n")
        else:
            for course in selected_courses:
                print_course(course)
                export_file.write(
                    f"- {course['course_code']}: {course['course_name']} "
                    f"({course['Year']}, {course['credit_hours']} credits)\n"
                )
        export_file.write("Completed Courses:\n")
        print("Completed Courses:\n")
        if not completed_courses: 
            export_file.write("- No other courses completed.\n")
        else:
            for course in completed_courses:
                print_course(course)
                export_file.write(
                    f"- {course['course_code']}: {course['course_name']} "
                    f"({course['Year']}, {course['credit_hours']} credits)\n"
                )
    

    print(f"\n-> Your selected classes were exported to {export_file_name}\n")

def set_student_info():  # Gets student year + major
    global student_year
    global student_major
    print("\n --- Enter your info ---\n")
    student_year = input("\n-> What year are you in? [Type Rising Freshman, Freshman, Sophmore, Junior, or Senior]: ").strip().title()
    if student_year == "Sophmore":
        student_year = "Sophomore"
    student_major = input("\n-> What's your major? (Enter the corresponding #, type ? for list of majors): ").strip()
    if student_major == "?":
        print_majors()
        student_major = input("\n -> What's your major? (Enter the corresponding #, type ? for list of courses): ").strip() # Add input validation
            

def print_course(course_dict): # Prints a received course object
    print(f"Course: {course_dict['course_name']}, {course_dict['course_code']}") # Prints course name and code
    print(f"Taught by: {course_dict['professor']}, worth {course_dict['credit_hours']} credit hours. \n") # Prints professor and credit hours

def courses_by_year(course_dict): # Finds the classes corresponding with the student's year and major
    global student_year
    if course_dict["Year"] == "Freshman" and student_year == "Freshman":
        print_course(course_dict)
    elif course_dict["Year"] == "Sophomore" and student_year == "Sophomore":
        print_course(course_dict)
    elif course_dict["Year"] == "Junior" and student_year == "Junior":
        print_course(course_dict)
    elif course_dict["Year"] == "Senior" and student_year == "Senior":
        print_course(course_dict)

def courses_by_major(course_dict): # Finds the classes corresponding with the student's major   
    if course_dict["Year"] == "Freshman":
        print_course(course_dict)
    elif course_dict["Year"] == "Sophomore":
        print_course(course_dict)
    elif course_dict["Year"] == "Junior":
        print_course(course_dict)
    elif course_dict["Year"] == "Senior":
        print_course(course_dict)
    
def future_courses(course_dict):
    global student_year
    # Prints only the classes not taken (assuming all sophmores taken freshman classes, etc.)
    if student_year == "Rising Freshman":
        courses_by_major(course_dict) # all courses in the major
    elif student_year == "Freshman":
        if course_dict["Year"] == "Sophomore":
            print_course(course_dict)
        if course_dict["Year"] == "Junior":
            print_course(course_dict)
        if course_dict["Year"] == "Senior":
            print_course(course_dict)
    elif student_year == "Sophmore":
        if course_dict["Year"] == "Junior":
            print_course(course_dict)
        if course_dict["Year"] == "Senior":
            print_course(course_dict)
    elif student_year == "Junior":
        if course_dict["Year"] == "Senior":
            print_course(course_dict)    
# define log_course to write to a file with student's classes, can be in JSON format



##print(course_catalogue_index[0].values()) # This will print the course names for the accounting courses.

def print_majors():
    courses = """
    Majors and Corresponding #

    0. Accounting
    1. Aviation
    2. Biology
    3. Business
    4. Communication
    5. Computer Science
    6. Criminal Justice
    7. Cybersecurity
    8. Economics
    9. Education
    10. Engineering
    11. English
    12. Exercise Science
    13. Finance
    14. General Studies
    15. Management
    16. Marine Science
    17. Marketing
    18. Music
    19. Nursing
    20. Philosophy
    21. Political Science
    22. Psychology

    """
    print(courses)
    
    
######This is the list of tuples for classes in the course catalogue. It has the dictionary for each class with the pointers to the course code and course name from the above indexes, w/ Professor, credit hours, and year offered.

course =

aviation_classes = [
    {"course_code": "AVI 101", "course_name": "Introduction to Aviation", "professor": "Prof. James Carter", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "AVI 120", "course_name": "Private Pilot Ground School", "professor": "Prof. Elena Brooks", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "AVI 230", "course_name": "Instrument Flight Theory", "professor": "Prof. Marcus Reed", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "AVI 310", "course_name": "Aviation Safety", "professor": "Prof. Dana Mitchell", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "AVI 360", "course_name": "Air Traffic Systems", "professor": "Prof. Aaron Phillips", "credit_hours": 4, "Year": "Senior"}
    ]

biology_classes = [
    {"course_code": "BIO 110", "course_name": "Principles of Biology I", "professor": "Prof. Hannah Cole", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "BIO 111", "course_name": "Principles of Biology II", "professor": "Prof. Victor Lane", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "BIO 220", "course_name": "Genetics", "professor": "Prof. Priya Menon", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "BIO 330", "course_name": "Microbiology", "professor": "Prof. Samuel Ortiz", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "BIO 410", "course_name": "Ecology", "professor": "Prof. Rachel Kim", "credit_hours": 4, "Year": "Senior"}
]

business_classes = [
    {"course_code": "BUS 101", "course_name": "Introduction to Business", "professor": "Prof. Lauren Hayes", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "ACC 201", "course_name": "Financial Accounting", "professor": "Prof. Michael Grant", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "ECO 201", "course_name": "Microeconomics", "professor": "Prof. Nina Wallace", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "MKT 301", "course_name": "Principles of Marketing", "professor": "Prof. Derek Sullivan", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "FIN 320", "course_name": "Corporate Finance", "professor": "Prof. Olivia Turner", "credit_hours": 4, "Year": "Senior"}
]
engineering_classes = [
    {"course_code": "ENG 101", "course_name": "Introduction to Engineering", "professor": "Prof. David Wright", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "ENG 201", "course_name": "Engineering Graphics", "professor": "Prof. Jennifer Lopez", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "ENG 301", "course_name": "Thermodynamics", "professor": "Prof. Robert Hill", "credit_hours": 4, "Year": "Junior"},
    {"course_code": "ENG 401", "course_name": "Capstone Design Project", "professor": "Prof. Amanda Scott", "credit_hours": 4, "Year": "Senior"}
]
Finance_classes = [
    {"course_code": "FIN 301", "course_name": "Principles of Finance", "professor": "Prof. Olivia Turner", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "FIN 320", "course_name": "Corporate Finance", "professor": "Prof. Olivia Turner", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "FIN 330", "course_name": "Investments", "professor": "Prof. Ethan Baker", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "FIN 410", "course_name": "Financial Markets", "professor": "Prof. Sophia Wilson", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "FIN 420", "course_name": "International Finance", "professor": "Prof. Liam Davis", "credit_hours": 4, "Year": "Senior"}
]

accounting_classes = [
    {"course_code": "ACC 201", "course_name": "Financial Accounting", "professor": "Prof. Michael Grant", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "ACC 202", "course_name": "Managerial Accounting", "professor": "Prof. Lauren Hayes", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "ACC 310", "course_name": "Intermediate Accounting I", "professor": "Prof. Trevor Adams", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "ACC 311", "course_name": "Intermediate Accounting II", "professor": "Prof. Diana Brooks", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "ACC 420", "course_name": "Auditing", "professor": "Prof. Henry Collins", "credit_hours": 4, "Year": "Senior"}
]

communication_classes = [
    {"course_code": "COM 101", "course_name": "Public Speaking", "professor": "Prof. Megan Price", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "COM 210", "course_name": "Interpersonal Communication", "professor": "Prof. Tyler Simmons", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "COM 230", "course_name": "Mass Media and Society", "professor": "Prof. Rachel Dunn", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "COM 320", "course_name": "Organizational Communication", "professor": "Prof. Jordan Bell", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "COM 350", "course_name": "Digital Media Production", "professor": "Prof. Avery Long", "credit_hours": 4, "Year": "Senior"}
]

computer_science_classes = [
    {"course_code": "CS 110", "course_name": "Introduction to Programming", "professor": "Prof. Isaac Flores", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "CS 220", "course_name": "Data Structures", "professor": "Prof. Chloe Bennett", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "CS 230", "course_name": "Computer Organization", "professor": "Prof. Noah Perry", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "CS 310", "course_name": "Algorithms", "professor": "Prof. Emma Stewart", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "CS 340", "course_name": "Database Systems", "professor": "Prof. Lucas Rivera", "credit_hours": 4, "Year": "Senior"}
]

criminal_justice_classes = [
    {"course_code": "CRJ 101", "course_name": "Introduction to Criminal Justice", "professor": "Prof. Caleb Morris", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "CRJ 210", "course_name": "Criminology", "professor": "Prof. Hailey Ross", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "CRJ 230", "course_name": "Policing in America", "professor": "Prof. Brandon Cook", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "CRJ 320", "course_name": "Corrections", "professor": "Prof. Sydney Morgan", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "CRJ 410", "course_name": "Criminal Law", "professor": "Prof. Adrian Hayes", "credit_hours": 4, "Year": "Senior"}
]

cybersecurity_classes = [
    {"course_code": "CYB 210", "course_name": "Introduction to Cybersecurity", "professor": "Prof. Ethan Clark", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "CYB 220", "course_name": "Network Security", "professor": "Prof. Maya Peterson", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "CYB 310", "course_name": "Ethical Hacking", "professor": "Prof. Jason Reed", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "CYB 320", "course_name": "Digital Forensics", "professor": "Prof. Natalie Gray", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "CYB 410", "course_name": "Security Operations", "professor": "Prof. Owen King", "credit_hours": 4, "Year": "Senior"}
]

economics_classes = [
    {"course_code": "ECO 201", "course_name": "Microeconomics", "professor": "Prof. Nina Wallace", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "ECO 202", "course_name": "Macroeconomics", "professor": "Prof. Peter Lang", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "ECO 310", "course_name": "Intermediate Microeconomics", "professor": "Prof. Grace Hart", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "ECO 311", "course_name": "Intermediate Macroeconomics", "professor": "Prof. Simon West", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "ECO 420", "course_name": "Econometrics", "professor": "Prof. Leah Ford", "credit_hours": 4, "Year": "Senior"}
]

education_classes = [
    {"course_code": "EDU 200", "course_name": "Foundations of Education", "professor": "Prof. Amber Fisher", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "EDU 240", "course_name": "Educational Psychology", "professor": "Prof. Blake Turner", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "EDU 300", "course_name": "Classroom Management", "professor": "Prof. Caitlin Ward", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "EDU 330", "course_name": "Assessment and Instruction", "professor": "Prof. Devin Brooks", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "EDU 410", "course_name": "Student Teaching Seminar", "professor": "Prof. Emily Scott", "credit_hours": 4, "Year": "Senior"}
]

english_classes = [
    {"course_code": "ENG 101", "course_name": "English Composition I", "professor": "Prof. William Young", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "ENG 102", "course_name": "English Composition II", "professor": "Prof. Hannah Webb", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "ENG 220", "course_name": "Introduction to Literature", "professor": "Prof. Colin Hayes", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "ENG 320", "course_name": "American Literature", "professor": "Prof. Maria Diaz", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "ENG 410", "course_name": "Advanced Writing", "professor": "Prof. Sarah Cole", "credit_hours": 4, "Year": "Senior"}
]

exercise_science_classes = [
    {"course_code": "EXS 101", "course_name": "Introduction to Exercise Science", "professor": "Prof. Ryan Foster", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "EXS 220", "course_name": "Kinesiology", "professor": "Prof. Lauren Price", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "EXS 230", "course_name": "Exercise Physiology", "professor": "Prof. Gavin Hill", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "EXS 320", "course_name": "Biomechanics", "professor": "Prof. Zoe Turner", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "EXS 410", "course_name": "Strength and Conditioning", "professor": "Prof. Connor White", "credit_hours": 4, "Year": "Senior"}
]

general_studies_classes = [
    {"course_code": "ENG 101", "course_name": "English Composition I", "professor": "Prof. William Young", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "MAT 103", "course_name": "College Algebra", "professor": "Prof. Linda Cooper", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "BIO 100", "course_name": "General Biology", "professor": "Prof. Karen Mills", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "HIS 201", "course_name": "U.S. History", "professor": "Prof. Daniel Ross", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "PSY 101", "course_name": "Introduction to Psychology", "professor": "Prof. Anna Bell", "credit_hours": 4, "Year": "Senior"}
]

management_classes = [
    {"course_code": "MGT 301", "course_name": "Principles of Management", "professor": "Prof. Lauren Hayes", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "MGT 320", "course_name": "Organizational Behavior", "professor": "Prof. Jacob Lewis", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "MGT 330", "course_name": "Human Resource Management", "professor": "Prof. Priya Shah", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "MGT 410", "course_name": "Operations Management", "professor": "Prof. Marcus Lane", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "MGT 420", "course_name": "Strategic Management", "professor": "Prof. Olivia Hart", "credit_hours": 4, "Year": "Senior"}
]

marine_science_classes = [
    {"course_code": "MSC 101", "course_name": "Introduction to Marine Science", "professor": "Prof. Elijah Moore", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "MSC 220", "course_name": "Oceanography", "professor": "Prof. Chloe Bennett", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "MSC 240", "course_name": "Marine Ecology", "professor": "Prof. Lucas Dean", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "MSC 320", "course_name": "Marine Conservation", "professor": "Prof. Mia Sanders", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "MSC 410", "course_name": "Coastal Processes", "professor": "Prof. Ryan Blake", "credit_hours": 4, "Year": "Senior"}
]

marketing_classes = [
    {"course_code": "MKT 301", "course_name": "Principles of Marketing", "professor": "Prof. Derek Sullivan", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "MKT 320", "course_name": "Consumer Behavior", "professor": "Prof. Alexis Ward", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "MKT 330", "course_name": "Digital Marketing", "professor": "Prof. Colin Marsh", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "MKT 410", "course_name": "Marketing Research", "professor": "Prof. Brooke Ellis", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "MKT 420", "course_name": "Strategic Marketing", "professor": "Prof. Adam Price", "credit_hours": 4, "Year": "Senior"}
]

music_classes = [
    {"course_code": "MUS 101", "course_name": "Music Appreciation", "professor": "Prof. Laura Bennett", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "MUS 120", "course_name": "Music Theory I", "professor": "Prof. Jason Monroe", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "MUS 121", "course_name": "Music Theory II", "professor": "Prof. Natalie Cruz", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "MUS 220", "course_name": "History of Western Music", "professor": "Prof. Ethan Keller", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "MUS 410", "course_name": "Senior Recital", "professor": "Prof. Sophia Reed", "credit_hours": 4, "Year": "Senior"}
]

nursing_classes = [
    {"course_code": "NUR 201", "course_name": "Foundations of Nursing", "professor": "Prof. Julia Myers", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "NUR 220", "course_name": "Health Assessment", "professor": "Prof. Daniel Kim", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "NUR 301", "course_name": "Adult Health Nursing", "professor": "Prof. Rebecca Sloan", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "NUR 320", "course_name": "Pharmacology", "professor": "Prof. Nathan Cole", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "NUR 410", "course_name": "Community Health Nursing", "professor": "Prof. Olivia Marsh", "credit_hours": 4, "Year": "Senior"}
]

philosophy_classes = [
    {"course_code": "PHI 101", "course_name": "Introduction to Philosophy", "professor": "Prof. Grant Lawson", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "PHI 210", "course_name": "Ethics", "professor": "Prof. Amber Pierce", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "PHI 220", "course_name": "Logic", "professor": "Prof. Derek Blake", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "PHI 320", "course_name": "Political Philosophy", "professor": "Prof. Hannah Reid", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "PHI 410", "course_name": "Philosophy of Mind", "professor": "Prof. Victor Young", "credit_hours": 4, "Year": "Senior"}
]

political_science_classes = [
    {"course_code": "POL 101", "course_name": "Introduction to Political Science", "professor": "Prof. Thomas Green", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "POL 220", "course_name": "American Government", "professor": "Prof. Melissa Cole", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "POL 230", "course_name": "International Relations", "professor": "Prof. Kevin Stone", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "POL 320", "course_name": "Comparative Politics", "professor": "Prof. Rachel Hayes", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "POL 410", "course_name": "Public Policy", "professor": "Prof. Brian Scott", "credit_hours": 4, "Year": "Senior"}
]

psychology_classes = [
    {"course_code": "PSY 101", "course_name": "Introduction to Psychology", "professor": "Prof. Anna Bell", "credit_hours": 3, "Year": "Freshman"},
    {"course_code": "PSY 220", "course_name": "Developmental Psychology", "professor": "Prof. Dylan Hunter", "credit_hours": 3, "Year": "Sophomore"},
    {"course_code": "PSY 230", "course_name": "Abnormal Psychology", "professor": "Prof. Megan Fox", "credit_hours": 3, "Year": "Junior"},
    {"course_code": "PSY 310", "course_name": "Cognitive Psychology", "professor": "Prof. Isaac Reed", "credit_hours": 4, "Year": "Senior"},
    {"course_code": "PSY 340", "course_name": "Research Methods in Psychology", "professor": "Prof. Claire Wood", "credit_hours": 4, "Year": "Senior"}
]


# Indexs to print courses by major and year. This will be used in the if statements to print courses by major and year.
accounting_classes_index = list(accounting_classes) # Index for accounting classes
aviation_classes_index = list(aviation_classes) # Index for aviation classes
biology_classes_index = list(biology_classes)
business_classes_index = list(business_classes)
engineering_classes_index = list(engineering_classes)
Finance_classes_index = list(Finance_classes)
communication_classes_index = list(communication_classes)
computer_science_classes_index = list(computer_science_classes)
criminal_justice_classes_index = list(criminal_justice_classes)
cybersecurity_classes_index = list(cybersecurity_classes)
economics_classes_index = list(economics_classes)
education_classes_index = list(education_classes)
engineering_classes_index = list(engineering_classes)
english_classes_index = list(english_classes)
exercise_science_classes_index = list(exercise_science_classes)
general_studies_classes_index = list(general_studies_classes)
management_classes_index = list(management_classes)
marine_science_classes_index = list(marine_science_classes)
marketing_classes_index = list(marketing_classes)
music_classes_index = list(music_classes)
nursing_classes_index = list(nursing_classes)
philosophy_classes_index = list(philosophy_classes)
political_science_classes_index = list(political_science_classes)
psychology_classes_index = list(psychology_classes)

# lets remkae the all course index to be the same order as we gave the user:
all_courses_index = [accounting_classes_index, aviation_classes_index, biology_classes_index, business_classes_index, communication_classes_index, computer_science_classes_index, criminal_justice_classes_index, cybersecurity_classes_index, economics_classes_index, education_classes_index, engineering_classes_index, english_classes_index, exercise_science_classes_index, Finance_classes_index, general_studies_classes_index, management_classes_index, marine_science_classes_index, marketing_classes_index, music_classes_index, nursing_classes_index, philosophy_classes_index, political_science_classes_index, psychology_classes_index]

# to access the accounting classes for example, we would do
accounting_classes = all_courses_index[0]

set_student_info()

classes_menu = """
Do you want to:
1.) See your major's courses for this year
2.) See all your major's courses
3.) View course catalogue
4.) Save your completed courses
5.) View future courses
(Type 1 - 5, * to stop.) 
"""

menu_opt = input(classes_menu).strip()

while menu_opt != "*":
    if menu_opt == "1":
        print("\n --- Printing your courses this year --- \n")
        # This prints the classes for students by major and year, cycling through the courses for the major and checking the year of the course against the student's year. 
        selected_courses = []
        for course in all_courses_index[int(student_major)]: # This will print all the courses for the user major and year.
            if course["Year"] == student_year:
                selected_courses.append(course)
                print_course(course)
        if not selected_courses:
            print("No courses found for your current year.\n")
        menu_opt = input(classes_menu).strip()
    elif menu_opt == "2": # This is seeing all the courses for the major
        print("\n --- Printing your major's courses --- \n")
        selected_courses = list(all_courses_index[int(student_major)])
        for course in all_courses_index[int(student_major)]: # This will print all the courses for the user major and year.
            courses_by_major(course)
        menu_opt = input(classes_menu).strip()
    elif menu_opt == "3": # Prints ALL of the courses
        print("\n --- Printing all courses --- \n")
        for i in range(0, len(all_courses_index)):
            for course in all_courses_index[i]:
                print_course(course)
        menu_opt = input(classes_menu).strip()
    elif menu_opt == "4": #Log your completed courses
            print("\n --- This is for logging all completed courses. --- \n")
            print("\n --- Printing your eligible completed courses --- \n")
            eligible_courses = []
            for course in all_courses_index[int(student_major)]:
                if year_rank(course["Year"]) <= year_rank(student_year):
                    eligible_courses.append(course)
                    print_course(course)
            print("\n")
            course_code = ""
            while course_code != "*":
                course_code = input("---> Type the course code (etc, PHIL 402), * to quit: ").strip().upper()
                if course_code == "*":
                    break
                found_match = False
                for course in eligible_courses:
                    if course["course_code"].upper() == course_code:
                        found_match = True
                        if course not in completed_courses:
                            print_course(course)
                            completed_courses.append(course)
                        else:
                            print("That course is already saved as completed.\n")
                if not found_match:
                    print("Course code not found in eligible courses for your year.\n")
            menu_opt = input(classes_menu).strip()
    elif menu_opt == "5":
        print("\n --- Printing future courses --- \n")
        selected_courses = []
        for course in all_courses_index[int(student_major)]: # This will print all the FUTURE courses for the user major and year.
            if course not in completed_courses:
                if student_year == "Rising Freshman":
                    selected_courses.append(course)
                elif student_year == "Freshman" and course["Year"] in ["Sophomore", "Junior", "Senior"]:
                    selected_courses.append(course)
                elif student_year == "Sophomore" and course["Year"] in ["Junior", "Senior"]:
                    selected_courses.append(course)
                elif student_year == "Junior" and course["Year"] == "Senior":
                    selected_courses.append(course)
        if student_year == "Senior":
            print("\n-> Finish up your current classes, then you're done! You got this! \n")
        export_selected_classes(selected_courses, completed_courses) 
        menu_opt = input(classes_menu).strip()
    else:
        print("Please choose 1-5 or * to stop.\n")
        menu_opt = input(classes_menu).strip()

export_selected_classes(selected_courses, completed_courses)
print("\nThanks for using the course planner. Goodbye!\n")
        
       
