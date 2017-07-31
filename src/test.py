import os
import xml.etree.ElementTree as ET

directory = "/Users/davisallen/Projects/Python/idmlToHtml/assets/Example_IDML_File/"
output_html_file = "/Users/davisallen/Projects/Python/idmlToHtml/output/index.html"

stories = []

for item in os.listdir(directory):
    if item == "Stories":
        print(item)
        subdir = directory + item
        subitems = os.listdir(subdir)
        for subitem in subitems:
            print("    " + subitem)
        stories = subitems

story_xml_trees = dict()
story_xml_roots = dict()

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
for key, value in story_xml_roots.items():
    contents = value.iter('Content')
    for content in contents:
        fout.write("    <p>" + content.text + "</p>\n")

html_template_end = """</BODY>
</HTML>"""
fout.write(html_template_end)

fout.close()