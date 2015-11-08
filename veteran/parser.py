import json
with open('raw_home.json','r') as data_file:
    home = json.load(data_file)
home_update = open("home.json", "a")


for i in xrange(len(home)):
    if (home[i]["title"] != ""):
        title = home[i]["title"]
        content=home[i]["content"]
        link=home[i]["linkName"]
        dicts={"title":title,"content":content,"link":link}
        home_update.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))
home_update.close()

with open('raw_family.json','r') as data_file:
    family = json.load(data_file)
family_update = open("family.json", "a")


for i in xrange(len(family)):
    if (family[i]["title"] != ""):
        title = family[i]["title"]
        content=family[i]["content"]
        link=family[i]["linkName"]
        dicts={"title":title,"content":content,"link":link}
        family_update.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))
family_update.close()

with open('raw_facilities.json','r') as data_file2:
    facilities = json.load(data_file2)
facilities_update = open("facilities.json", "a")

for i in xrange(len(facilities)):
    if (facilities[i]["facility_id"] != ""):
        name = facilities[i]["name"]
        types = facilities[i]["type"]
        address = facilities[i]["address"] + ", " + facilities[i]["city"] + ", " + facilities[i]["state"] + ", "+ facilities[i]["postal_code"]
        phone = facilities[i]["phone"]
        latitude = facilities[i]["latitude"]
        longitude = facilities[i]["longitude"]
        description = facilities[i]["description"]
        url = facilities[i]["url"]
        dicts={"name":name, "types":types,"address":address,"phone":phone,"latitude":latitude,"longitude":longitude,"description":description,"url":url}
        facilities_update.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))
facilities_update.close()

with open('raw_jobs.json','r') as data_file3:
    jobs = json.load(data_file3)
jobs_update = open("jobs.json", "a")


for i in xrange(len(jobs)):
    if (jobs[i]["title"] != ""):
        office = jobs[i]["office"]
        posted_dt= jobs[i]["posted_dt"]
        FBO_OFFAD= jobs[i]["FBO_OFFAD"]
        zipcode= jobs[i]["zipcode"]
        description= jobs[i]["description"]
        listing_url= jobs[i]["listing_url"]

        dicts={"office":office,"posted_dt":posted_dt,"FBO_OFFAD":FBO_OFFAD, "zipcode":zipcode, "description":description, "listing_url":listing_url}
        jobs_update.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))
jobs_update.close()
