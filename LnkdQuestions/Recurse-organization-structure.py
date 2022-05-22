

from operator import contains
import pip._vendor.requests
import json

def callcurl(url):
    if 'A123456789' in url:
        ret_json = {
                    "name": "Flynn Mackie",
                    "title": "Senior VP of Engineering",
                    "reports": ["A123456793", "A1234567898"]  }
        return json.dumps(ret_json)

    if 'A123456793' in url:
        ret_json = {
                    "name": "Wesley Thomas",
                    "title": "VP of Design",
                    "reports": ["A123456693", "A1234566898"]
                    }
        return json.dumps(ret_json)

    if 'A1234567898' in url:
        ret_json = {
                    "name": "Machinegun Kelly",
                    "title": "VP of Banking",
                    "reports": ["A123456693", "A1234566898"]
                    }
        return json.dumps(ret_json)        

    if 'A123456693' in url:
        ret_json = {
                    "name": "Randall Cosmo",
                    "title": "Director of Design",
                    "reports": ["B123456693"]
                    }
        return json.dumps(ret_json)   

    if 'A123456693' in url:
        ret_json = {
                    "name": "Randall Cosmo",
                    "title": "Director of Design",
                    "reports": ["B123456693"]
                    }
        return json.dumps(ret_json)  


    ret_json ={
                "name": "Jamie Ross",
                "title": "GIMP"
                }
    return json.dumps(ret_json)                          

def print_employee_hierarchy(id, tab_size=0):
    # get info using requests
    # parse the info to get: name, title, reports
    # for every id in reports -> recurse print_emp_hierarchy(id)

    #resp = pip._vendor.requests.get("http://www.companyname.corp/api/employee/" + id)
    resp = callcurl("http://www.companyname.corp/api/employee/" + id)
    resp_json = resp.json()
    # resp_json.get("name")
    name = resp_json["name"]
    title = resp_json["title"]
    reports = resp_json["reports"]

    for _ in range(tab_size):
        print ("\t")
    print (name, title)

    if not reports: 
        return

    tab_size += 1

    for id in reports:
        print_employee_hierarchy(tab_size, id)

print_employee_hierarchy('A123456789', 0)      