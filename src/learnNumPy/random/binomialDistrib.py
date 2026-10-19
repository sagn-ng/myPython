#Binomial Distribution is a Discrete Distribution.
#It describes the outcome of binary scenario, e.g: toss of a coin
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#syntax: numpy.random.binomial(n=..., p=..., size=...)
#where: n       : the number of trials
#       p       : probability of success in each trial
#       size    : size of the returned array
x = random.binomial(n=10, p=0.5, size=10)
print(x)
#visualization:
sns.displot(x)
plt.show()

print("#####")
#note: Normal distribution is continous whereas binomial is discrete,
#but if there are enough data points it will be quite similar to normal
#distribution with certain loc and scale.
data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data)
plt.show()