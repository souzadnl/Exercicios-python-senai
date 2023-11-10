import xml.etree.ElementTree as ET

elementos = ET.Element("elementos")
elemento = ET.SubElement(elementos, "Elemento")
elemento.text = "Hidrogênio"
elemento = ET.SubElement(elementos, "Elemento")
elemento.text = "Oxigênio"
tree = ET.ElementTree(elementos)

tree.write("elementos.xml", encoding="utf-8", xml_declaration=True)