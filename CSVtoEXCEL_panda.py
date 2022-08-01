import pandas as pd
from openpyxl import Workbook

df=pd.read_csv("a.csv")

df.to_excel("ab.xlsx",sheet_name="Sheet1")
