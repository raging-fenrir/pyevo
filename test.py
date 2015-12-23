import matplotlib.pyplot as plt
from scipy.stats import truncnorm
import numpy as np

fig, ax = plt.subplots(1,1)

dist = np.random.normal(loc=0.5,scale=0.01,size=100000)
#dist[dist>1]=1
#dist[dist<0]=0
ax.hist(dist,bins=100)
plt.show()
