import yaml

file = open("g:/Repositories/uvacs-advising/_scripts/courses.yml", 'r')
course_listing = yaml.safe_load(file)
for course_offering in course_listing:
    print(course_offering['course'])