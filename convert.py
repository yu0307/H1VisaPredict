import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt

exc_file = 'Analysis.xlsx'
df = pd.read_excel(exc_file)

VisaType=['N/A']
Major = ['N/A']
Consulate = ['N/A']

for index, row in df.iterrows():
    row=row.replace(np.nan, '', regex=True)
    if (not(row['Visa Type'].upper() in VisaType)):
        VisaType.append(row['Visa Type'].upper())
    if (not(row['US Consulate'] in Consulate)):
        Consulate.append(row['US Consulate'].upper())
    if (not(row['Major'] in Major)):
        Major.append(row['Major'].upper())

    df.at[index, 'VT'] = VisaType.index(row['Visa Type'].upper())
    df.at[index, 'USC'] = Consulate.index(row['US Consulate'].upper())
    df.at[index, 'MJ'] = Major.index(row['Major'].upper())
export = df[['Waiting Day(s)', 'ET', 'MJ', 'VT', 'USC']]

export.to_csv(r'.\export_dataframe.csv', index=None, header=True)
