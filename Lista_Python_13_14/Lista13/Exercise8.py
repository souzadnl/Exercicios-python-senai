import xml.etree.ElementTree as ET

tree = ET.parse("elementos.xml")
root = tree.getroot()
elemento = root.findall("Elemento")

for element in elemento:
    print(element.text)