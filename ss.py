import xml.etree.ElementTree as Xet
import pandas as pd
  
cols = ["1", "2", "3", "4", "5"]
rows = []
"""PARSING THE XML FILE"""
xmlparse = Xet.parse('result.xml')
root = xmlparse.getroot()

  
df = pd.DataFrame(rows, columns=cols)


  
"""WRITING THE DATAFRAME INTO CSV"""
df.to_csv('output.csv')