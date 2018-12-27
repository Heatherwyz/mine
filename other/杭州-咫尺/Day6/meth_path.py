# -*- coding:utf-8 -*-
__author__ = "Heather"
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.cElementTree as ET

if __name__ == '__main__':
    print("Element Tree XPath特性支持示例")
    tree = ET.parse("data_demo.xml")
    root = tree.getroot()
    print("选择当前节点")
    data = root.findall(".")
    for d in data:
        print(d.tag)

    countrys = root.findall(".//country")
    for country in countrys:
        print(country.tag," ",country.attrib["name"])

    countrys = root.findall("country")
    for country in countrys:
        print (country.tag, " ", country.attrib["name"])

    countrys = root.findall (".//*[@name='Panama']")
    for country in countrys:
        print (country.tag, " ", country.attrib["name"])

    print ("name属性为Panama的country下的year节点")
    years = root.findall (".//country[@name='Panama']/year")
    for year in years:
        print (year.text)

    print ("通过索引来选择country节点，选择第一个country节点")
    country = root.findall (".//country[1]")
    for c in country:
        print (c.tag, " ", c.attrib["name"])

    print ("通过子节点的文本内容来选择节点")
    gdppc = root.findall (".//*[gdppc='59900']")
    for gd in gdppc:
        print (gd.tag)