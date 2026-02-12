import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s1)
print(s2)

marks=pd.Series([85, 90, 75], index=['Math', 'Physics', 'Chemistry'])
print(marks['Math'])
print(marks[['Math','Chemistry']])

scores=pd.Series([45,67,89,34,90])
passed=scores[scores>60]
print(passed)

#handling missing values
data=pd.Series([10,None,30,None])
print(data.isnull())
print(data.fillna(0))

names=pd.Series(['Alice','bob','CHARLIE'])
print(names.str.lower())
print(names.str.contains('a'))

