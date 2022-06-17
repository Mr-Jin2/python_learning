import xml.etree.ElementTree as ET

tree = ET.parse('anno1.xml')
print(type(tree),'tree is',tree)

root = tree.getroot()
print('root tag is :', root.tag)

element = root.findall('object')
print('element length is :', len(element))
print('element is',element)
print('element text is', element[1][0].text)