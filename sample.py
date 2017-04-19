filename = 'campbell_mapzen.osm'
sample = 'campbell_map_sample2.osm'

k = 100 # Parameter: take every k-th top level element

#  Top level tags were identifed by looking at the file on Sublime text
# Not all OSM files have only one kind of top level tag, so tags is a tuple (data structure similar to a list)
def get_element(filename, tags = ('bounds', 'node', 'way', 'relation')): #row
    context = iter(ET.iterparse(filename, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()

with open(sample, 'wb') as output:
    output.write('<?osm version="1.0" encoding="UTF-8"?>\n') # xml declaration
    output.write('<osm>\n  ') # this is the root element (opening tag for the whole document) 
    # Write every kth element
    for i, element in enumerate(get_element(filename)):
        if i % k == 0:
            output.write(ET.tostring(element, encoding='utf-8'))
    output.write('</osm>') # closing tag for the whole document #response