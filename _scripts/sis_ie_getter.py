import requests
import json
import csv

# first experiment: pull a page of CS courses and print info about them
def main():
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232' + \
    '&page=1&subject=CS'
    r = requests.get(url)

    for c in r.json():
        print(c['subject'], c['catalog_nbr'], c['component'], c['descr'], c['class_nbr'], c['class_capacity'], c['enrollment_available'])

# second experiment: using a list of courses, make a request for each and print info about them
def main2():
    clist = [('MATH','3100'), ('PSYC','2150'), ('STAT','2120')]
    # clist = [('CS','1115')]  # what happens if course not found? answer: empty list returned

    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1'

    for c in clist:
        r = requests.get(url + '&subject=' + c[0] + '&catalog_nbr=' + c[1])
        for c in r.json():
            print(c['subject'], c['catalog_nbr'] + '-' + c['class_section'], c['component'], c['descr'], \
                  c['class_nbr'], c['class_capacity'], c['enrollment_available'])

# third experiment: using CSV file, make a request for each and print HTML <TR> table markup for each course
def main3():
    url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&page=1'
    with open('test1.csv') as csvfile:
        course_reader = csv.reader(csvfile)
        for row in course_reader:
            r = requests.get(url + '&subject=' + row[0] + '&catalog_nbr=' + row[1])
            for c in r.json():
                # get course identifying info
                course_id = c['subject'] + ' ' + c['catalog_nbr'] + '-' + c['class_section'];
                course_id = course_id + ' (' + c['component'] + ')' if c['component'] != "LEC" else course_id
                # get meeting day and time
                m = c['meetings']
                if len(m) > 1: # debugging. Not sure what to do in this case. Probably nothing for now.
                    print('*** Meetings list > 1 ***')
                if c['instruction_mode'] == 'OA':  #  recognize online asynchronous courses
                    day = "Online"
                else: # get days and times and cleanup formatting
                    day = m[0]['days'] + ' ' + m[0]['start_time'][0:5] + '-' + m[0]['end_time'][0:5]
                    day = day.replace('.', ':')
                # print a single table row <TR> entry for the course
                print('<TR><TD>' + course_id + '</TD>', end=" ")
                print('<TD>' + c['descr'] + '</TD>', end=" ")
                print('<TD>' + day + '</TD>', end=" ")
                print('<TD>' + str(c['enrollment_available']) + '</TD></TR>')

if __name__ == '__main__':
    main3()

