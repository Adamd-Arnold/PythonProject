## Course Catalogue in Python Using Dictionaries
from course_list import COURSE_CATALOG

## Make a tuple of all the course dictionaries for easy access
course_catalogue = tuple(COURSE_CATALOG.values())
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

'''
To print accounting classes only with Freshman year, we would do:
for course in accounting_classes:
    if course["Year"] == "Freshman":
        print(course["course_name"])

'''
