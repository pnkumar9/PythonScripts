

import json
#import requests

def callcurl(url):
    if 'A123456789' in url:
        ret_json = {
                    "name": "Flynn Mackie",
                    "title": "Senior VP of Engineering",
                    "reports": ["A123456793", "A1234565898"]  }
        return json.dumps(ret_json)

    if 'A123456793' in url:
        ret_json = {
                    "name": "Wesley Thomas",
                    "title": "VP of Design",
                    "reports": ["A123456693", "A1234566898"]
                    }
        return json.dumps(ret_json)

    if 'A1234565898' in url:
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
                    "reports": []
                    }
        return json.dumps(ret_json)   

    if 'A1234566898' in url:
        ret_json = {
                    "name": "Kumar Cosmo",
                    "title": "Director of Devops",
                    "reports": []
                    }
        return json.dumps(ret_json)   

    ret_json ={
                "name": "Jamie Ross",
                "title": "GIMP",
                "reports": []
                }
    return json.dumps(ret_json)                          

def print_employee_hierarchy(id, tab_size=0):
    # get info using requests
    # parse the info to get: name, title, reports
    # for every id in reports -> recurse print_emp_hierarchy(id)

    #resp = requests.get("http://www.companyname.corp/api/employee/" + id)
    resp = callcurl("http://www.companyname.corp/api/employee/" + str(id))
    #print(resp)
    #resp_json = resp.json()

    resp_json = json.loads(resp)
    # resp_json.get("name")
    name = resp_json["name"]
    title = resp_json["title"]
    reports = resp_json["reports"]

    #name = resp["name"]
    #title = resp["title"]
    #reports = resp["reports"]  
    # 

 
    if tab_size == 0:
        print(name+' - '+title)
    else:
        print(' ' * 2 * tab_size+name+' - '+title)

    if len(reports) == 0: 
        return   


    tab_size += 1

    for id in reports:
        print_employee_hierarchy(id, tab_size)

print_employee_hierarchy('A123456789', 0)      