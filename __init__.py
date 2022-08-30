import json
import xml.etree.ElementTree


def addArray(a):
    parsedDict = "["

    for child in a:
        if child.tag == "array":
            parsedDict += addArray(child)
        elif child.tag == "dict":
            parsedDict += addDict(child)
        elif child.tag == "string" or child.tag == "date" or child.tag == "data":
            parsedDict += "\"" + str(child.text).replace('"', '\\"').replace('\n', '').replace('\r', '').replace('\t', '') + "\","
        elif child.tag == "true":
            parsedDict += "true,"
        elif child.tag == "false":
            parsedDict += "false,"
        else:
            parsedDict += child.text
            parsedDict += ","

    return parsedDict[:-1] + "],"

def addDict(d):
    parsedDict = "{"

    for child in d:
        if child.tag == "key":
            parsedDict += "\"" + child.text + "\": "
        elif child.tag == "array":
            parsedDict += addArray(child)
        elif child.tag == "dict":
            parsedDict += addDict(child)
        elif child.tag == "string" or child.tag == "date" or child.tag == "data":
            parsedDict += "\"" + child.text.replace('"', '\\"').replace('\n', '').replace('\r', '').replace('\t', '') + "\","
        elif child.tag == "true":
            parsedDict += "true,"
        elif child.tag == "false":
            parsedDict += "false,"
        else:
            parsedDict += child.text
            parsedDict += ","

    return parsedDict[:-1] + "},"

def readXML(file):
    tree = xml.etree.ElementTree.parse(file)
    root = tree.getroot()
    parsedFile = ""
    for child in root:
        if child.tag == "dict":
            parsedFile += addDict(child)
    return json.loads(parsedFile[:-1])
