# Program to convert an xml 
# file to json file
# source https://www.geeksforgeeks.org/python-xml-to-json/
# and
# https://stackoverflow.com/questions/57422734/how-to-merge-multiple-json-files-into-one-file-in-python/57422761
 
import json
import xmltodict
 
ad_files = ["EAD_AD_AFR", "EAD_AD_ASIA", "EAD_AD_EUR", "EAD_AD_PANAM"]
navaid_files = ["EAD_NAV_DME", "EAD_NAV_TACAN", "EAD_NAV_VOR"]
categories = [
    [ad_files, "EAD_AD_ALL"],
    [navaid_files, "EAD_NAV_ALL"]
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

def mergeJSON(json_files, name):
    counter = 0
    result = list()
    print(f"Start merging {len(json_files)} JSON files")
    for file in json_files:
        print(f"Processing {file}.json")
        with open(f"{file}.json", 'r') as infile:
            result.append(json.load(infile))
            counter+= 1
            
    with open(f"{name}.json", 'w') as output_file:
        json.dump([result], output_file)
    print(f"Successfully merged {counter} JSON files into {name}.json")

for category in categories:
    parseXML(category[0])
    mergeJSON(category[0], category[1])

input("ENTER to exit")
