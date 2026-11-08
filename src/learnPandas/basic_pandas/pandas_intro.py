"""Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data."""

import pandas as pd
print(pd.__version__) #print the version of pandas

mydataset = {
  'cars': ["BMW", "McLaren", "Mercedes"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(type(myvar))
print(myvar) #the result is a table