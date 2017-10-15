from services.SQLService import *

import requests
from bs4 import BeautifulSoup
import re

faculties = ["ACCT","ACTL","AERO","ANAT","ARCH","ARTS","ASIA","ATSI","AUST","AVEN","AVIA","AVIF","AVIG","BABS","BEES","BEIL","BENV","BINF","BIOC","BIOM","BIOS","BIOT","BLDG","CEIC","CHEM","CHEN","CLIM","CODE","COMD","COMM","COMP","CONS","CRIM","CRTV","CVEN","DATA","DIPP","ECON","EDST","ELEC","ENGG","ENGL","ENVP","ENVS","EXCH","FINS","FNDN","FOOD","GBAT","GENC","GENE","GENL","GENM","GENS","GENT","GENY","GEOL","GEOS","GMAT","GSBE","GSOE","HESC","HIST","HUML","HUMS","IDES","IEST","INDC","INFS","INST","INTA","INTD","JAPN","JURD","LAND","LAWS","LING","MANF","MARK","MATH","MATS","MBAX","MDCN","MDIA","MECH","MFAC","MFIN","MGMT","MICR","MINE","MMAN","MNGT","MNNG","MODL","MSCI","MTRN","MUPS","MUSC","NANO","NAVL","NCHR","NEUR","OBST","OPTM","PAED","PATH","PHAR","PHCM","PHIL","PHOP","PHSL","PHTN","PHYS","PLAN","POLS","POLY","PSCY","PSYC","PTRL","REGZ","REST","RISK","SCIF","SENG","SLSP","SOCF","SOCW","SOLA","SOMS","SOSS","SPRC","SRAP","STAM","SURG","SUSD","SWCH","TABL","TELE","UDES","VISN","WOMS","YENG","YMED","ADAD","SAED","SAHT","SART","SDES","SOMA","ZBUS","ZEIT","ZGEN","ZHSS","ZINT","ZPEM"]

activities = {
    "CLN": "Clinical",
    "DST": "Distance",
    "FLD": "Field Studies",
    "LA1": "Lab 1",
    "LA2": "Lab 2",
    "LAB": "Lab",
    "LE1": "Lecture 1",
    "LE2": "Lecture 2",
    "LEC": "Lecture",
    "OTH": "Other",
    "PRJ": "Project",
    "SEM": "Seminar",
    "STD": "Studio",
    "THE": "Thesis",
    "TLB": "Tut-Lab",
    "TU1": "Tutorial 1",
    "TU2": "Tutorial 2",
    "TUT": "Tutorial",
    "WEB": "Web Stream"
}

days = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4
}



def valid_details(details):
    return details != ' ' and details[:3] in days.keys()

def parse_detail_time(detail_time):
    split_detail_time = detail_time.split('-')
    start_time = int(split_detail_time[0])
    if len(split_detail_time) > 1:
        end_time = int(split_detail_time[1])
        length = int(split_detail_time[1]) - start_time
    else:
        length = 1

    return start_time, length


for fac in faculties:

    request, class_table_index = requests.get('http://nss.cse.unsw.edu.au/sitar/classes2017/'+fac+'_S2.html'), 3
    # request, class_table_index = requests.get('http://classutil.unsw.edu.au/'+fac+'_S1.html'), 2 # Current classutil, already set to 18s1 so no use for now


    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        class_table = soup.find_all('table')[class_table_index]

        for row in class_table.find_all('tr')[1:-16]:
            if not row.get('class'):
                td = row.find_all('td')
                course_code = td[0].get_text().strip()
                # course_name = td[1].get_text()
            else:
                td = row.find_all('td')
                activity = activities.get(td[0].get_text(), td[0].get_text())
                class_id = td[1].get_text()
                details = td[7].get_text()

                if valid_details(details):

                    # print(course_code[:4], course_code[4:], class_id, activity)
                    for detail in details.split('; '):
                        m = re.search(r'(\w+) ([\d\-:]+)[#/]?.*', detail)
                        detail_day, detail_time = m.group(1), m.group(2)

                        # ignore courses that aren't on the hour
                        if ':' not in detail_time:
                            start_time, length = parse_detail_time(detail_time)

                            # only take weekday courses
                            if detail_day in days.keys():
                                print('Faculty: {}, Code: {}, ID: {}, Day: {}, Activity: {}, Starts: {}, Length: {}'.format(course_code[:4], course_code[4:], class_id, days[detail_day], activity, start_time, length))

                                sql = "INSERT IGNORE INTO courses (faculty, course_code, class_id, day, activity, start_time, length) VALUES ('{}', {}, '{}', {}, '{}', {}, {})".format(course_code[:4], course_code[4:], class_id, days[detail_day], activity, start_time, length)
                                execute_sql(sql)
