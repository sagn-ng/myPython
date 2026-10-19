from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#syntax: numpy.random.normal(loc=..., scale=..., size=...)
#where: loc     : the mean value    (default value is 0)
#       scale   : standard deviation    (default value is 1)
#       size    : size of the returned array

data=random.normal(loc=1, size=1500)
#these 2 lines below are used to visualize the distribution
sns.displot(data)
plt.show()