# -*- coding: utf-8 -*-
"""
Created on Tue May 03 12:56:27 2016

@author: lalit
"""
#from plotting import *

#barchart([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5)
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Bar(
        x=['giraffes', 'orangutans', 'monkeys'],
        y=[20, 14, 23]
    )
]
py.plot(data)


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#g1=35,g2=45,g3=25,g4=20
mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()