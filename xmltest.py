import xml.etree.ElementTree as ET

 
tree = ET.parse(r'C:\Users\Sgavari\Desktop\one Button upgrade\WINInstaller\Data\ReleaseInfo.xml')
root = tree.getroot()
 
for node in tree.findall('.//Name'):
    print (node.text)