# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:43:38 2020

@author: Shalini
"""

import os
import xml.etree.ElementTree as ET

xml_file = "physsim-network.xml"
csv_file_output = '{}_out.csv'.format(os.path.splitext(xml_file)[0])

tree = ET.parse(xml_file)
xml_root = tree.getroot()

with open(csv_file_output, 'w') as fout:
    fout.write("id,From,to,length,freespeed,capacity,permlanes,oneway,modes")
    for link in xml_root.iter("link"):
        id = link.get("id")
        From = link.get("from")
        to= link.get("to")
        length= link.get("length")
        freespeed = link.get("freespeed")
        capacity = link.get("capacity")
        permlanes = link.get("permlanes")
        oneway = link.get("oneway")
        modes=link.get("modes")
        fout.write('\n{0},{1},{2},{3},{4},{5},{6},{7},"{8}"'.format(id, From, to, length, freespeed, capacity, permlanes,oneway,modes))
import pandas as pd
dataset = pd.read_csv('physsim-network_out.csv')