import numpy as np
import matplotlib.pyplot as mpl 
from sklearn.preprocessing import scale
from TFANN import ANNR

stock_data = np.loadtxt('AAPL.csv', delimiter= ",", skiprows=1, usecols=(1,4))

stock_data = scale(stock_data)
prices = stock_data[:,1].reshape(-1,1)
dates = stock_data[:,0].reshape(-1,1)

input  = 1
output = 1
hidden = 10

layers = [('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'),('F', output)]

mlpr = ANNR([input], layers, batchSize = 256, maxIter = 10000, tol = 0.075, reg = 1e-4, verbose = True)

holdDays = 10
totalDays = len(dates)
#fit the model to the data "Learning"
mlpr.fit(dates[0:(totalDays-holdDays)], prices[0:(totalDays-holdDays)])

#Predict the stock price using the model
pricePredict = mlpr.predict(dates[totalDays-holdDays:])
#Display the predicted reuslts agains the actual data
mpl.plot(dates, prices)
mpl.plot(dates[totalDays-holdDays:], pricePredict, c='#5aa9ab')
mpl.show()




