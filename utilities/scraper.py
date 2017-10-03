import requests
from bs4 import BeautifulSoup

faculties = ["ACCT","ACTL","AERO","ANAT","ARCH","ARTS","ASIA","ATSI","AUST","AVEN","AVIA","AVIF","AVIG","BABS","BEES","BEIL","BENV","BINF","BIOC","BIOM","BIOS","BIOT","BLDG","CEIC","CHEM","CHEN","CLIM","CODE","COMD","COMM","COMP","CONS","CRIM","CRTV","CVEN","DATA","DIPP","ECON","EDST","ELEC","ENGG","ENGL","ENVP","ENVS","EXCH","FINS","FNDN","FOOD","GBAT","GENC","GENE","GENL","GENM","GENS","GENT","GENY","GEOL","GEOS","GMAT","GSBE","GSOE","HESC","HIST","HUML","HUMS","IDES","IEST","INDC","INFS","INST","INTA","INTD","JAPN","JURD","LAND","LAWS","LING","MANF","MARK","MATH","MATS","MBAX","MDCN","MDIA","MECH","MFAC","MFIN","MGMT","MICR","MINE","MMAN","MNGT","MNNG","MODL","MSCI","MTRN","MUPS","MUSC","NANO","NAVL","NCHR","NEUR","OBST","OPTM","PAED","PATH","PHAR","PHCM","PHIL","PHOP","PHSL","PHTN","PHYS","PLAN","POLS","POLY","PSCY","PSYC","PTRL","REGZ","REST","RISK","SCIF","SENG","SLSP","SOCF","SOCW","SOLA","SOMS","SOSS","SPRC","SRAP","STAM","SURG","SUSD","SWCH","TABL","TELE","UDES","VISN","WOMS","YENG","YMED","ADAD","SAED","SAHT","SART","SDES","SOMA","ZBUS","ZEIT","ZGEN","ZHSS","ZINT","ZPEM"]

activities = {
    "LAB": "Lab",
    "LEC": "Lecture",
    "OTH": "Other",
    "SEM": "Seminar",
    "TUT": "Tutorial",
}


for fac in faculties:

    request, class_table_index = requests.get('http://nss.cse.unsw.edu.au/sitar/classes2017/'+fac+'_S2.html'), 3
    # request, class_table_index = requests.get('http://classutil.unsw.edu.au/'+fac+'_S1.html'), 2 # Current classutil, already set to 18s1 so no use for now


    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        class_table = soup.find_all('table')[class_table_index]

        for row in class_table.find_all('tr')[1:-16]:
            if not row.get('class'):
                td = row.find_all('td')
                course_code = td[0].get_text()
                # course_name = td[1].get_text()
            else:
                td = row.find_all('td')
                activity = activities.get(td[0].get_text(), td[0].get_text())
                details = td[7].get_text()

                if details != " ":
                    # TODO: parse details
                    print(course_code[:4], course_code[4:], activity, details)
