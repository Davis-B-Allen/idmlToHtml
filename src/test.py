import os
import xml.etree.ElementTree as ET

# directory_in_str = "/Users/davisallen/Projects/Python/idmlToHtml/assets/Example_IDML_File/"
# directory = os.fsencode(directory_in_str)
directory = "/Users/davisallen/Projects/Python/idmlToHtml/assets/Example_IDML_File/"
output_html_file = "/Users/davisallen/Projects/Python/idmlToHtml/output/testoutput/index.html"

design_map = ""
spreads = []
master_spreads = []
stories = []

for item in os.listdir(directory):
    if item == "designmap.xml":
        print(item)
        design_map = item
    elif item == "Spreads":
        print(item)
        subdir = directory + item
        subitems = os.listdir(subdir)
        for subitem in subitems:
            print("    " + subitem)
        spreads = subitems
    elif item == "MasterSpreads":
        print(item)
        subdir = directory + item
        subitems = os.listdir(subdir)
        for subitem in subitems:
            print("    " + subitem)
            master_spreads = subitems
    elif item == "Stories":
        print(item)
        subdir = directory + item
        subitems = os.listdir(subdir)
        for subitem in subitems:
            print("    " + subitem)
        stories = subitems

print("************************")

spread_xml_trees = dict()
spread_xml_roots = dict()

master_spread_xml_trees = dict()
master_spread_xml_roots = dict()

story_xml_trees = dict()
story_xml_roots = dict()

if design_map:
    design_map_xml_tree = ET.parse(directory + design_map)
    design_map_xml_root = design_map_xml_tree.getroot()

for item in spreads:
    tree = ET.parse(directory + "Spreads/" + item)
    root = tree.getroot()
    spread_xml_trees[item] = tree
    spread_xml_roots[item] = root

print("************************")

for item in stories:
    tree = ET.parse(directory + "Stories/" + item)
    root = tree.getroot()
    story_xml_trees[item] = tree
    story_xml_roots[item] = root


fout = open(output_html_file, 'w')
html_template_start = """<HTML>
<HEAD>
    <title>Test Generated from IDML</title>
    <meta charset="utf-8">
</HEAD>
<BODY>
"""
fout.write(html_template_start)


# walk through story_xml_roots and findall / search for appropriate children (or maybe iter for them)
for key, value in story_xml_trees.items():
    root = value
    contents = root.iter('Content')
    for content in contents:
        fout.write("    <p>" + content.text + "</p>\n")
        print(content.text)

html_template_end = """</BODY>
</HTML>"""
fout.write(html_template_end)


# for item in master_spreads:
#     print(item)
#
# for item in stories:
#     print(item)
