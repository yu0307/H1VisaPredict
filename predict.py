import numpy as np
import pandas as pd
from matplotlib import pyplot
from sklearn import linear_model

exc_file = 'export_dataframe.csv'
# base = pd.read_csv(exc_file)
data = np.array(pd.read_csv(exc_file))
y = data[:, 0]
ET = data[:, 1]
MJ = data[:, 2]
VT = data[:, 3]
USC = data[:, 4]
# X = [list(ET), list(MJ), list(VT), list(USC)]
X = [list(ET), list(MJ), list(VT)]

regr = linear_model.LinearRegression()
regr.fit(np.array(X).transpose(), y)

# Deng = [[1, 44, 5, 4]]
Deng = [[1, 44, 5]]
Predict = regr.predict(Deng)

test = 'Test.csv'
data2 = np.array(pd.read_csv(test))
p_id = data2[:, 0]
ET = data2[:, 1]
MJ = data2[:, 2]
VT = data2[:, 3]
USC = data2[:, 4]
X_new = [list(ET), list(MJ), list(VT), list(USC)]
Y_new = regr.predict(np.array(X_new).transpose())

a = np.array(p_id)
b = np.array(np.round(Y_new))
p = [a, b]
pd.DataFrame(p).transpose().to_csv("my_solution.csv", index=0)


