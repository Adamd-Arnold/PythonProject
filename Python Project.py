## Course Catalogue in Python Using Dictionaries
import json

accounting_courses = {"ACCT760": "Advanced Managerial Accounting", "ACCT650": "Adv Managerial Acct & Fin Modeling", "ACCT680": "Financial Decision-making", "ACCT620": "Advanced Managerial Accounting", "ACCT201": "Principles of Accounting I"}

art_courses = {"ART102": "2D Art Foundations", "ART103": "3D Art Foundations", "ART107": "Drawing I", "ART115TI": "Visual Media Foundations", "ART202": "Illustration Methods"}

aviation_courses = {"AVM301": "Aviation History & Developmnt", "AVM302": "Aviation Economics", "AVM303RI": "Intro Unmanned Aircraft Systems", "AVM306": "Airport Planning & Management", "AVM311": "Airline Management"}

biology_courses = {"BIOL100": "Principles of Biology", "BIOL180": "Biological Diversity", "BIOL190": "Biological Unity", "BIOL215": "Human Anatomy & Physiology I", "BIOL222": "Microbiology for Health Professionals"}

business_courses = {"BUS102": "Business Scholars I", "BUS202": "Business Scholars II", "BUS302": "Business Scholars II", "BUS390": "Internship in Business", "BUS402": "Business Scholars IV"}

chemistry_courses = {"CHEM101": "Introductory College Chemistry", "CHEM101H": "Honors: Introductory College Chemistry", "CHEM120": "Urban Environmental Issues", "CHEM204": "General Chemistry I", "CHEM204H": "Hon General Chemistry I"}

communication_courses = {"COMM395": "Communication Practicum 1–3", "COMM401": "Communicating to Diverse Publics", "COMM201SI": "Introduction to Public Speaking", "COMM207WI": "Online Newswriting", "COMM332WI": "Social Media: Writing"}

computer_science_courses = {"CS102": "Introduction of Computational Thinking", "CS150": "Personal Productivity Using Technology", "CS155": "Foundations of Computer Science", "CS158": "Fundamentals of Programming", "CS199": "Introduction to Special Topics in Computing Science"}

criminal_justice_courses = {"LAW707": "Criminal Law and Procedure I", "LAW717": "Criminal Law and Procedure II", "LAW742": "Advanced Criminal Procedure", "SOC305": "Criminology", "SOC320": "Green Criminology"}

cybersecurity_courses = {"CS341": "Introduction to Cybersecurity", "CS345SI": "Network Security", "CS449": "Digital Forensics", "CS601": "Foundations of Cybersecurity", "CS610": "Cyber Threat Intelligence"}

data_science_courses = {"DSIM602": "Introduction to Applied Business Analytics", "DSIM606": "Data Mining and Predictive Analytics", "DSIM307": "Introduction to Business Analytics", "MATH270": "Introduction to Data Science", "MATH170TI": "Data Science Foundations"}

economics_courses = {"ECON201": "Principles of Macroeconomics", "ECON202": "Principles of Microeconomics", "ECON211": "Quantitative Methods Soc Sci", "ECON310": "Money & Banking", "ECON340": "Sports Economics"}

education_courses = {"EDU102": "Human Development & Learning", "EDU103": "PM 1 - Intro Found in Educatn", "EDU248": "ESOL 2 - Methods of Teaching", "EDU287": "Special Topics in Edu", "EDU312SI": "Intro to Civic Engagement"}

electrical_engineering_courses = {"EE221": "Digital I", "EE331": "Electronic Power System Dsgn", "EE222": "Analog I", "EE322": "Analog II", "EE311": "Linear Systems Design"}

engineering_courses = {"ENGR111": "Freshmen Design", "ENGR151": "Applied Physics for Engineering Design I", "ENGR151L": "Applied Physics for Engineering Lab", "ENGR152": "App Physics for Engineering Design II", "ENGR152L": "Engineering Physics II Lab"}

english_courses = {"ENGL101": "Elements of Composition", "ENGL103": "Introductory Writing", "ENGL103H": "Hon: Introductory Writing", "ENGL189": "Southern Women Writers", "ENGL200": "Aquarian Practicum"}

entrepreneurship_courses = {"ENT480": "Special Topics in Entrepreneurship", "ENT482": "Managing Growing Enterprise"}

environmental_science_courses = {"ENV101": "Intro to Environmental Studies"}

exercise_science_courses = {"EXSC101": "Intro to Exercise Science", "EXSC180": "Wingshooting I; Beginning", "EXSC181": "Wingshooting Ii; Intermediate", "EXSC182": "Wingshooting Iii; Advanced", "EXSC305": "Principles of Group Exercise"}

finance_courses = {"FIN750": "Corporate Mergers Acquisitions Valuation", "FIN610": "Practicum in Portfolio Management", "FIN612": "Investment Management", "FIN587": "ST/Portfolio Management Capstone", "FIN301": "Corporate Finance"}

general_courses = {"ENGL101": "Elements of Composition", "MATH104": "College Algebra", "HIST150": "The Modern World", "BIOL100": "Principles of Biology", "PHIL101": "Introduction to Philosophy"}

healthcare_administration_courses = {"NUR670": "Leadership and Health Policy", "HLSC301": "Epidemiology in Health Science", "HLSC412": "Public Health", "MSHI524": "Public/Population Health Informatics", "NUR630": "Epidemiology and Biostatistics"}

history_courses = {"HIST150": "The Modern World", "HIST206": "History of the United States to", "HIST207": "History of the United States From", "HIST300": "History of Sports", "HIST350": "Special Topics in History"}

information_technology_courses = {"ACCT370": "Accounting Information Systems", "CS330": "Networks & Wireless Communications", "CS600": "Network and Wireless Communications", "CS345SI": "Network Security", "CS380": "Web Programming"}

international_business_courses = {"INB555": "Competing in the Global Economy", "INB341": "International Marketing", "INB410": "Economics of Globalization", "MGT545": "Global Corporate Strategy and Policy", "POL208": "International Politics"}

management_courses = {"MGT715": "Entrepreneurial Behavior in Organizations", "MGT736": "Strategic Leadership", "MGT566": "Legal & Ethical Environment of Business", "MGT610": "Strategic Human Resource Management", "MGT620": "Responsible Leadership"}

marine_science_courses = {"MSC111": "Introduction to Oceanography", "MSC112": "Introduction Oceanography Lab", "MSC113": "Intro to Marine Biology", "MSC114": "Intro to Marine Biology Lab", "MSC304WI": "Ichthyology"}

marketing_courses = {"MKG765": "Marketing with a Global Mindset", "MKG540": "Strategic Marketing in a Digital Economy", "MKG587": "Project Class", "MKG301": "Principles of", "MKG438": "Marketing Strategy"}

mathematics_courses = {"MATH104": "College Algebra", "MATH110": "Mathematics of Motion & Change", "MATH112": "Modern Applications of Math", "MATH112H": "Honors: Modern Appl of Math", "MATH114": "Discover, Decode, Decide"}

mechanical_engineering_courses = {"ME202": "Materials in Design", "ME221": "Mechanics I", "ME222": "Mechanics II", "ME315": "Mechanical Systems Design", "ME321": "Thermofluids I"}

music_courses = {"MUS100": "Recital Attendance", "MUS111": "Essential Keyboard Skills", "MUS116": "Singer's Diction I", "MUS141": "Music Theory I", "MUS144": "Acoustics & Recording Techniques"}

nursing_courses = {"NUR530": "Financial Management of Nursing Systems", "NUR531": "Human Resource Mgt Healthcare", "NUR532": "Nursing Leadership in Healthcare Systems", "NUR112": "Introduction to Nursing", "NUR204": "Foundations of Pharmacology"}

philosophy_courses = {"PHIL101": "Introduction to Philosophy", "PHIL101H": "Hon: Intro to Philosophy", "PHIL189": "Philosophy for Coping", "PHIL212": "Ethics", "PHIL311": "Political Philosophy"}

physics_courses = {"PHYS104": "Astronomy", "PHYS111": "Principles of Physics I", "PHYS116": "Astronomy Laboratory", "PHYS125": "Aviation Physics", "PHYS151": "General Physics: Mechanics"}

political_science_courses = {"POL205": "American National Government", "POL208": "International Politics", "POL211": "Quantitative Methods for Social Science", "POL307": "Congressional Politics", "POL309": "Constitutional Law"}

psychology_courses = {"PSYC201": "Introductory Psychology", "PSYC210": "Human Growth & Development", "PSYC211": "Quantitative Methods Soc Sci", "PSYC225": "Professional Development", "PSYC250": "The Power of Difference: Conversations"}

public_health_courses = {"HLSC301": "Epidemiology in Health Science", "HLSC412": "Public Health", "NUR630": "Epidemiology and Biostatistics", "MSHI524": "Public/Population Health Informatics", "NUR587": "Population Health Informatics"}

sociology_courses = {"SOC203": "Introductory Sociology", "SOC211": "Quantitative Methods for Social Science", "SOC250": "The Power of Difference: Conversations", "SOC275TI": "Geographic Information Systems", "SOC303": "Geography of Middle East"}

software_engineering_courses = {"CS158": "Fundamentals of Programming", "CS260": "Object-Oriented Programming", "CS302": "Software Design & Development", "CS395SI": "Software Engineering", "CS380": "Web Programming"}

sport_management_courses = {"SPO300": "Introduction to the Business of Sport", "SPO320": "Sport Facility and Event Management", "SPO370": "Sport Promotion and Technology", "SIS200": "Introduction to Sports in Society", "ECON340": "Sports Economics"}

statistics_courses = {"DSIM201": "Business Statistics", "DSIM603": "Applied Statistical Modeling and Analysis", "DSIM405": "Advanced Statistics and Econometrics", "MATH206": "Statistical Methods in Science", "MATH315": "Probability"}

theatre_courses = {"THEA110": "Introduction to Theatre", "THEA113": "Acting I", "THEA114": "Acting II Scene Study", "THEA115": "Intro to Technical Theatre", "THEA199": "Special Topics"}

# JU Colleges (https://www.ju.edu/academics/colleges/index.php)

linda_berry_stein_college_of_arts_and_sciences = {"art": art_courses, "biology": biology_courses, "chemistry": chemistry_courses, "communication": communication_courses, "data_science": data_science_courses, "education": education_courses, "english": english_courses, "environmental_science": environmental_science_courses, "exercise_science": exercise_science_courses, "general": general_courses, "history": history_courses, "marine_science": marine_science_courses, "mathematics": mathematics_courses, "music": music_courses, "philosophy": philosophy_courses, "physics": physics_courses, "political_science": political_science_courses, "psychology": psychology_courses, "sociology": sociology_courses, "theatre": theatre_courses}

davis_college_of_business_and_technology = {"accounting": accounting_courses, "aviation": aviation_courses, "business": business_courses, "computer_science": computer_science_courses, "cybersecurity": cybersecurity_courses, "economics": economics_courses, "electrical_engineering": electrical_engineering_courses, "engineering": engineering_courses, "entrepreneurship": entrepreneurship_courses, "finance": finance_courses, "information_technology": information_technology_courses, "international_business": international_business_courses, "management": management_courses, "marketing": marketing_courses, "mechanical_engineering": mechanical_engineering_courses, "software_engineering": software_engineering_courses, "sport_management": sport_management_courses, "statistics": statistics_courses}

brooks_rehabilitation_college_of_healthcare_sciences = {"healthcare_administration": healthcare_administration_courses, "nursing": nursing_courses, "public_health": public_health_courses}

college_of_law = {"criminal_justice": criminal_justice_courses}

example_commit = str("")

all_colleges = {**linda_berry_stein_college_of_arts_and_sciences, **davis_college_of_business_and_technology, **brooks_rehabilitation_college_of_healthcare_sciences, **college_of_law}



# Semester 1 variables for every major
semester_1_by_major = {major_name: semester_plan[1] for major_name, semester_plan in classes_by_major_and_semester.items()}