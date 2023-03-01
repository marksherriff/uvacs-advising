import requests
import json
import csv


url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1238&page=1&subject=CS'
r = requests.get(url)

for c in r.json():
    print(c['subject'], c['catalog_nbr'], c['component'], c['descr'], c['class_nbr'], c['class_capacity'], c['enrollment_available'], c['instructors'][0]['name'], c['meetings'][0]['days'], c['meetings'][0]['start_time'], c['meetings'][0]['end_time'], c['meetings'][0]['facility_id'])