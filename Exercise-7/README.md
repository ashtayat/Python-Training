# Estarta Python Training-Day 7
User Guide
The User Guide covers all of pandas by topic area. Each of the subsections introduces a topic (such as “working with missing data”), and discusses how pandas approaches the problem, with many examples throughout.

Users brand-new to pandas should start with 10 minutes to pandas.

For a high level summary of the pandas fundamentals, see Intro to data structures and Essential basic functionality.

How to read these guides
In these guides you will see input code inside code blocks such as:

import pandas as pd
pd.DataFrame({'A': [1, 2, 3]})
or:

import pandas as pd

pd.DataFrame({'A': [1, 2, 3]})
Out[2]: 
   A
0  1
1  2
2  3

The first block is a standard python input, while in the second the In [1]: indicates the input is inside a notebook. In Jupyter Notebooks the last line is printed and plots are shown inline.

Basic data structures in pandas
Pandas provides two types of classes for handling data:

Series: a one-dimensional labeled array holding data of any type
such as integers, strings, Python objects etc.

DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.

Object creation
See the Intro to data structures section.

Creating a Series by passing a list of values, letting pandas create a default RangeIndex.

s = pd.Series([1, 3, 5, np.nan, 6, 8])

s
Out[4]: 
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
Creating a DataFrame by passing a NumPy array with a datetime index using date_range() and labeled columns:

dates = pd.date_range("20130101", periods=6)

dates
Out[6]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df
Out[8]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988

Merge, join, concatenate and compare
pandas provides various methods for combining and comparing Series or DataFrame.
concat(): Merge multiple Series or DataFrame objects along a shared index or column
DataFrame.join(): Merge multiple DataFrame objects along the columns
DataFrame.combine_first(): Update missing values with non-missing values in the same location
merge(): Combine two Series or DataFrame objects with SQL-style joining
merge_ordered(): Combine two Series or DataFrame objects along an ordered axis
merge_asof(): Combine two Series or DataFrame objects by near instead of exact matching keys
Series.compare() and DataFrame.compare(): Show differences in values between two Series or DataFrame objects

concat()
The concat() function concatenates an arbitrary amount of Series or DataFrame objects along an axis while performing optional set logic (union or intersection) of the indexes on the other axes. Like numpy.concatenate, concat() takes a list or dict of homogeneously-typed objects and concatenates them.
Joining logic of the resulting axis
The join keyword specifies how to handle axis values that don’t exist in the first DataFrame.

join='outer' takes the union of all axis values

refrence:https://pandas.pydata.org/docs/user_guide/merging.html