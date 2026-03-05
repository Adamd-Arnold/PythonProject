## Course Catalogue in Python Using Dictionaries


accounting_courses = {"ACC 201": "Financial Accounting", "ACC 202": "Managerial Accounting", "ACC 310": "Intermediate Accounting I", "ACC 311": "Intermediate Accounting II", "ACC 420": "Auditing"}

aviation_courses = {"AVI 101": "Introduction to Aviation", "AVI 120": "Private Pilot Ground School", "AVI 230": "Instrument Flight Theory", "AVI 310": "Aviation Safety", "AVI 360": "Air Traffic Systems"}

biology_courses = {"BIO 110": "Principles of Biology I", "BIO 111": "Principles of Biology II", "BIO 220": "Genetics", "BIO 330": "Microbiology", "BIO 410": "Ecology"}

business_courses = {"BUS 101": "Introduction to Business", "ACC 201": "Financial Accounting", "ECO 201": "Microeconomics", "MKT 301": "Principles of Marketing", "FIN 320": "Corporate Finance"}

communication_courses = {"COM 101": "Public Speaking", "COM 210": "Interpersonal Communication", "COM 230": "Mass Media and Society", "COM 320": "Organizational Communication", "COM 350": "Digital Media Production"}

computer_science_courses = {"CS 110": "Introduction to Programming", "CS 220": "Data Structures", "CS 230": "Computer Organization", "CS 310": "Algorithms", "CS 340": "Database Systems"}

criminal_justice_courses = {"CRJ 101": "Introduction to Criminal Justice", "CRJ 210": "Criminology", "CRJ 230": "Policing in America", "CRJ 320": "Corrections", "CRJ 410": "Criminal Law"}

cybersecurity_courses = {"CYB 210": "Introduction to Cybersecurity", "CYB 220": "Network Security", "CYB 310": "Ethical Hacking", "CYB 320": "Digital Forensics", "CYB 410": "Security Operations"}

economics_courses = {"ECO 201": "Microeconomics", "ECO 202": "Macroeconomics", "ECO 310": "Intermediate Microeconomics", "ECO 311": "Intermediate Macroeconomics", "ECO 420": "Econometrics"}

education_courses = {"EDU 200": "Foundations of Education", "EDU 240": "Educational Psychology", "EDU 300": "Classroom Management", "EDU 330": "Assessment and Instruction", "EDU 410": "Student Teaching Seminar"}

engineering_courses = {"ENGR 101": "Introduction to Engineering", "ENGR 201": "Statics", "ENGR 220": "Dynamics", "ENGR 250": "Thermodynamics", "ENGR 310": "Circuits"}

english_courses = {"ENG 101": "English Composition I", "ENG 102": "English Composition II", "ENG 220": "Introduction to Literature", "ENG 320": "American Literature", "ENG 410": "Advanced Writing"}

exercise_science_courses = {"EXS 101": "Introduction to Exercise Science", "EXS 220": "Kinesiology", "EXS 230": "Exercise Physiology", "EXS 320": "Biomechanics", "EXS 410": "Strength and Conditioning"}

finance_courses = {"FIN 301": "Principles of Finance", "FIN 320": "Corporate Finance", "FIN 330": "Investments", "FIN 410": "Financial Markets", "FIN 420": "International Finance"}

general_courses = {"ENG 101": "English Composition I", "MAT 103": "College Algebra", "BIO 100": "General Biology", "HIS 201": "U.S. History", "PSY 101": "Introduction to Psychology"}

management_courses = {"MGT 301": "Principles of Management", "MGT 320": "Organizational Behavior", "MGT 330": "Human Resource Management", "MGT 410": "Operations Management", "MGT 420": "Strategic Management"}

marine_science_courses = {"MSC 101": "Introduction to Marine Science", "MSC 220": "Oceanography", "MSC 240": "Marine Ecology", "MSC 320": "Marine Conservation", "MSC 410": "Coastal Processes"}

marketing_courses = {"MKT 301": "Principles of Marketing", "MKT 320": "Consumer Behavior", "MKT 330": "Digital Marketing", "MKT 410": "Marketing Research", "MKT 420": "Strategic Marketing"}

music_courses = {"MUS 101": "Music Appreciation", "MUS 120": "Music Theory I", "MUS 121": "Music Theory II", "MUS 220": "History of Western Music", "MUS 410": "Senior Recital"}

nursing_courses = {"NUR 201": "Foundations of Nursing", "NUR 220": "Health Assessment", "NUR 301": "Adult Health Nursing", "NUR 320": "Pharmacology", "NUR 410": "Community Health Nursing"}

philosophy_courses = {"PHI 101": "Introduction to Philosophy", "PHI 210": "Ethics", "PHI 220": "Logic", "PHI 320": "Political Philosophy", "PHI 410": "Philosophy of Mind"}

political_science_courses = {"POL 101": "Introduction to Political Science", "POL 220": "American Government", "POL 230": "International Relations", "POL 320": "Comparative Politics", "POL 410": "Public Policy"}

psychology_courses = {"PSY 101": "Introduction to Psychology", "PSY 220": "Developmental Psychology", "PSY 230": "Abnormal Psychology", "PSY 310": "Cognitive Psychology", "PSY 340": "Research Methods in Psychology"}


## Make a tuple of all the course dictionaries for easy access
course_catalogue = (accounting_courses, aviation_courses, biology_courses, business_courses, communication_courses, computer_science_courses, criminal_justice_courses, cybersecurity_courses, economics_courses, education_courses, engineering_courses, english_courses, exercise_science_courses, finance_courses, general_courses, management_courses, marine_science_courses, marketing_courses, music_courses, nursing_courses, philosophy_courses, political_science_courses, psychology_courses)
course_catalogue_index = list(course_catalogue)

print(course_catalogue_index[0].values()) # This will print the course names for the accounting courses.

'''
Major Number in the course catalogue:

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

'''


# Index for individual courses in the course catalogue:
accounting_code_index = list(course_catalogue_index[0].keys())[0]
accounting_name_index = list(course_catalogue_index[0].values())[0]



######This is the list of tuples for classes in the course catalogue. It has the dictionary for each class with the pointers to the course code and course name from the above indexes, w/ Professor, credit hours, and year offered.


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
    
'''
To print accounting classes only with Freshman year, we would do:
for course in accounting_classes:
    if course["Year"] == "Freshman":
        print(course["course_name"])

'''



