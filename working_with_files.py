### Reading data from CSV
import pandas as pd
from PIL._imaging import display

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)

# adding column name to the dataframe
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print(df)

### Writing JSON to a file
import json

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# json.dump() method can be used for writing to JSON file
with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# json.dumps() that helps in converting a dictionary to a JSON object
# Serializing json
json_object = json.dumps(person, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)


### reading JSON to a file
import json

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))


### Reading data from XLSX file
import pandas as pd
import urllib.request

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
df = pd.read_excel("sample.xlsx")
print(df)


### Writing with xml.etree.ElementTree
import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)


### Reading with xml.etree.ElementTree
import pandas as pd

import xml.etree.ElementTree as etree

tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building", "room"]

datatframe = pd.DataFrame(columns=columns)

for node in root:
    firstname = node.find("firstname").text

    lastname = node.find("lastname").text

    title = node.find("title").text

    division = node.find("division").text

    building = node.find("building").text

    room = node.find("room").text

    datatframe = datatframe.append(pd.Series([firstname, lastname, title, division, building, room], index=columns),
                                   ignore_index=True)


print(datatframe)

# save data to csv
datatframe.to_csv("employee.csv", index=False)


### Reading Image file
# importing PIL
# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.
from PIL import Image
import urllib.request

# Downloading dataset
urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

# Read image
img = Image.open('dog.jpg')

# Output Images
display(img)