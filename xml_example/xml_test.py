#import xml.etree.ElementTree as etree
from lxml import etree

doc = etree.parse("nxos_show_version.xml")
my_xml = doc.getroot()

#cpu_name = my_xml.find(".//{http://www.cisco.com/nxos:1.0:sysmgrcli}cpu_name")
cpu_name = my_xml.find(".//{*}cpu_name")
print(cpu_name.text)
