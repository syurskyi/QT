import xml.etree.ElementTree as ET

p = '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
    '004_Text data formats/example1.xml'

tree = ET.parse(p)
root = tree.getroot()
elem = root.find('element')
elem.tag
# print(elem.attrib)
# print(elem.text)
#
# root = ET.Element('root2')
# elem = ET.SubElement(root, 'elem2')
# elem.set('name', 'Max')
# elem.text = 'SOME TEXT'
#
# tree = ET.ElementTree(root)
# p2 = '/Users/sergejyurskyj/.nuke/example/PYTHON_EXAMPLE/Python_Example_All_Tutorials/VIDEO/Advanced Python Scripting/' \
#     '004_Text data formats/example2.xml'
#
# tree.write(p2)
#
# from xml.dom import minidom
# xml = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
#
# f = open(p2, 'w')
# f.write(xml)
# f.close()

