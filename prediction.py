# page 29

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
data = pd.read_csv('tr_eikon_eod_data.csv', index_col=0, parse_dates=True)
data = pd.DataFrame(data['AAPL.O'])
data['Returns'] = np.log(data / data.shift())
data.dropna(inplace=True)
lags = 6
cols= []
for lag in range(1,lags + 1):
    col = 'lag_{}'.format(lag)
    data[col] = np.sign(data['Returns'].shift(lag))
    cols.append(col)
data.dropna(inplace=True)



from sklearn.svm import SVC
model = SVC(gamma='auto')
model.fit(data[cols],np.sign(data['Returns']))
SVC(C=1.0,cache_size=200,class_weight=None,coef0=0.0,decision_function_shape='ovr',degree=3,gamma='auto',kernel='rbf',max_iter=1,probability=False,random_state=None,shrinking=True,tol=0.001, verbose=False)
data['Prediction'] = model.predict(data[cols])
data['Strategy'] = data['Prediction'] * data['Returns']
data[['Returns','Strategy']].cumsum().apply(np.exp).plot(figsize=(10,6))
plt.show()
print('done')