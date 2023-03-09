import requests
import json
import csv


url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=6&subject=CS'
r = requests.get(url)

for c in r.json():
    # print(c['subject'], c['catalog_nbr'], c['component'], c['descr'], c['class_nbr'], c['class_capacity'], c['enrollment_available'], c['instructors'][0]['name'], c['meetings'][0]['days'], c['meetings'][0]['start_time'], c['meetings'][0]['end_time'], c['meetings'][0]['facility_id'])

    # get course identifying info
    course_id = c['subject'] + ' ' + c['catalog_nbr'] + '-' + c['class_section'];
    course_id = course_id + ' (' + c['component'] + ')' if c['component'] != "LEC" else course_id
    m = c['meetings']

    if c['instruction_mode'] == 'OA':  #  recognize online asynchronous courses
        day = "Online"
    else: # get days and times and cleanup formatting
        day = m[0]['days'] + ' ' + m[0]['start_time'][0:5] + '-' + m[0]['end_time'][0:5]
        day = day.replace('.', ':')

    print("- course:",c['subject'], c['catalog_nbr'])
    print("  title:", c['descr'] )
    print("  type:", c['component'])
    print("  instructor:", c['instructors'][0]['name'])
    print("  day:", day)
    print("  location:", c['meetings'][0]['facility_id'])
    print()