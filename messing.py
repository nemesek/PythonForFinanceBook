""" import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes
ax.plot([1,2,3,4], [1,4,2,3])
plt.show() """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'

data = pd.read_csv('tr_eikon_eod_data.csv', index_col=0,parse_dates=True)
data = pd.DataFrame(data['.SPX'])
data.dropna(inplace=True)
data.info()
data['rets'] = np.log(data/data.shift(1))
data['vola'] = data['rets'].rolling(252).std() * np.sqrt(252)
data[['.SPX', 'vola']].plot(subplots=True, figsize=(10,6))
plt.show()
