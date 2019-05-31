import pandas as pd
from matplotlib import pyplot as plt
exc_file='VISA.xlsx'
visa=pd.read_excel(exc_file)
byLocation = visa.groupby(by="Visa Type")
df = visa["Waiting Day(s)"]
print(df.describe())
print (df.mode()[0])
for i in [30,60,90,180]:
    print (((df[df < i].size/df.size))*100)
H1 = visa[visa['Visa Type'] == 'H1']["Waiting Day(s)"]
print(H1.describe())
print(H1.mode()[0])
for i in [30, 60, 90, 180]:
    print(((H1[H1 < i].size/H1.size))*100)
    
plt.subplot(2, 1, 1)
plt.hist(df, bins=60, range=[0, 260])
plt.subplot(2, 1, 2)
df.plot.kde()
plt.show()