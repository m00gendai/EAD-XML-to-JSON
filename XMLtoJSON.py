# Program to convert an xml
# file to json file
# source https://www.geeksforgeeks.org/python-xml-to-json/
# and
# https://stackoverflow.com/questions/57422734/how-to-merge-multiple-json-files-into-one-file-in-python/57422761
 
import json
import xmltodict
 
ad_files = ["EAD_AD_AFR", "EAD_AD_ASIA", "EAD_AD_EUR", "EAD_AD_PANAM"]
navaid_files = ["EAD_NAV_DME", "EAD_NAV_TACAN", "EAD_NAV_VOR"]
waypoint_files = ["EAD_WPT_NE", "EAD_WPT_NW", "EAD_WPT_SE"]
categories = [
    [ad_files, "EAD_AD_ALL", "airports"],
    [navaid_files, "EAD_NAV_ALL", "navaids"],
    [waypoint_files, "EAD_WPT_ALL", "waypoints"]
]


def parseXML(xml_files):
    counter = 0
    print(f"Start parsing {len(xml_files)} XML files")
    for xml in xml_files:
        with open(f"{xml}.xml") as xml_file:
            print(f"Parsing {xml}")
            data_dict = xmltodict.parse(xml_file.read())
            xml_file.close()
             
            json_data = json.dumps(data_dict)
             
            with open(f"{xml}.json", "w") as json_file:
                json_file.write(json_data)
                json_file.close()
                print(f"Converted {xml}")
                counter += 1
    print(f"Successfully converted {counter} XML files to JSON")


def mergeJSON(json_files, name, const):
    counter = 0
    result = list()
    print(f"Start merging {len(json_files)} JSON files")
    for file in json_files:
        print(f"Processing {file}.json")
        with open(f"{file}.json", 'r') as infile:
            json_data = json.load(infile)
            for record in json_data["SdoReportResponse"]["SdoReportResult"]["Record"]:
                if name == "EAD_WPT_ALL":
                    if record["codeType"] == "ICAO":
                        item = dict(codeId=record["codeId"], geoLat=record["geoLat"], geoLong=record["geoLong"])
                        result.append(item)
                if name == "EAD_NAV_ALL":
                    if "codeType" in record:
                        if "txtName" in record:
                            print(record["txtName"])
                            item = dict(codeId=record["codeId"], geoLat=record["geoLat"], geoLong=record["geoLong"], 
                                        txtName=record["txtName"], codeType=record["codeType"])
                            result.append(item)
                        else:
                            item = dict(codeId=record["codeId"], geoLat=record["geoLat"], geoLong=record["geoLong"], 
                                        txtName="", codeType=record["codeType"])
                            result.append(item)
                    else:
                        if "txtName" in record:
                            item = dict(codeId=record["codeId"], geoLat=record["geoLat"], geoLong=record["geoLong"], 
                                        txtName=record["txtName"], codeType="DME or TACAN")
                            result.append(item)
                        else:
                            item = dict(codeId=record["codeId"], geoLat=record["geoLat"], geoLong=record["geoLong"], 
                                        txtName="", codeType="DME or TACAN")
                            result.append(item)
                if name == "EAD_AD_ALL":
                    item = dict(codeId=record["codeId"], geoLat=record["geoLat"], geoLong=record["geoLong"], 
                                txtName=record["txtName"])
                    result.append(item)
        counter += 1
    with open(f"{name}.js", 'w') as output_file:
        output_file.write(f"const {const} = {result}")
        print(f"Successfully merged {counter} JSON files into {name}.js")


for category in categories:
    parseXML(category[0])
    mergeJSON(category[0], category[1], category[2])

input("ENTER to exit")
