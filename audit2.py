import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Campbell", "Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Way", "Terrace", "Highway", "Circle", "Corte", 'de', 
            'Madrid', 'Portal', 'Plaza', 'Via', 'Sorrento', 'Calle', 'de', 'Barcelona'
            
           ]

# UPDATE THIS VARIABLE
mapping = { "campbell": "Campbell",
            "St": "Street",
            "St.": "Street",
            "Ave" : "Avenue",
            "Dr" : "Drive",
            "Boulvevard" : "Boulevard",
            "Ln": "Lane", "Rd" : "Road",
            "Blvd" : "Boulevard"
             }

# for each street, check if the type is one we expect
# if not, add it to the street_types defaultdict
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name) #regular expression see above
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

# check if something is a street name, return True or False
def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

# open the file and get a dictionary with all the street types and the corresponding street names
def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)): #'start' means start tags

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag): #call formula, which checks if its street name see above. Formula is not necessary
                    audit_street_type(street_types, tag.attrib['v']) #calls formula
    osm_file.close()
    return street_types

def update_name(name, mapping):
    n = name.split()
    if len(n) > 0:
        if n[-1] in mapping:
            n[-1] = mapping[n[-1]]
        name = ' '.join(n)
    return name




if __name__ == '__main__':
    # first let's see what we're working with
    if False:
        print audit(full_filename)
        zipcodes = audit_zipcodes(full_filename)
        for zipcode in zipcodes:
            print zipcode, zipcodes[zipcode]    
# now update mapping to include what we need to fix
# and we can run the rest of the code to fix the street names
    if :
        st_types = audit(full_filename)
        for st_type, ways in st_types.iteritems():
            for name in ways:
                better_name = update_name(name, mapping)
                print name, "=>", better_name