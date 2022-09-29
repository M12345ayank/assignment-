import xml.etree.ElementTree as Xet
import pandas as pd
file = pd.read_csv("output.csv")
print("\nOriginal file:")
print(file)
  
"""ADDING HEADER"""

headerList =  ['FinInstrmGnlAttrbts.Id','FinInstrmGnlAttrbts.FullNm','FinInstrmGnlAttrbts.ClssfctnTp','FinInstrmGnlAttrbts.CmmdtyDerivInd','FinInstrmGnlAttrbts.NtnlCcy','Issr']
  
"""CONVERTING DATAFRAME INTO CSV"""

file.to_csv("output1.csv", header=headerList, index=False)
  
"""DISPLAY MODIFIED CSV FILE"""

file2 = pd.read_csv("output1.csv")
print('\nModified file:')
print(file2)