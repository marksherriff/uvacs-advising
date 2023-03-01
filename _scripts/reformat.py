## For changing copy/pasted text from Lou's List into YML for Jekyll to use


courses_file = open("courses_raw.txt", "r")

course_number = ""
course_title = ""
credits = ""
description = ""

for line in courses_file:

    if line.startswith("CS"):
        paren_open = line.index("(")
        paren_close = line.index(")")
        course_number = line[0:7]
        course_title = line[8:paren_open]
        credits = line[paren_open+1:paren_close]

    else: 
        description = line[1:]
        print("- course: " + course_number)
        print("  title: " + course_title)
        print("  credits: " + credits)
        print("  description: \"" + description + "\"") 
        print("  prereqs: None")
        print()
