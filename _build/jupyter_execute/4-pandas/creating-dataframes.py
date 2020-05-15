# Creating Dataframes

import pandas as pd

Suppose we had some data on the number of pandas living in the wild over the past few years. We stored this data in lists and want to convert it into a dataframe.

panda_list = [1864, 1956, 2041]
year_list = [2014, 2015, 2016]

There are a few ways to create a `DataFrame`. One of the ways is to use a **dictionary** which is a data structure that stores a mapping from keys to values. In our `DataFrame` context, we want to store a mapping from *column names* to *the list containing the data*. The syntax is as follows:

df = pd.DataFrame({'year': year_list,
                   'panda_count': panda_list,})
df

```{note}
To create a dataframe this way, the list lengths must match. Also notice that each entry in the dictionary of the form `key : [values]` represents a column in the DataFrame where the `key` is the name of the column.
```

Alternatively, we also could create dataframes using other methods. For instance, if we are given row-wise data instead of columns, it would probably better to use another method to create our dataframe. For instance, we could use a nested list (lists inside a list):

df = pd.DataFrame([[2014, 1864], [2015, 1956], [2016, 2041]], 
                  columns=['year', 'panda_count'])
df

For other ways, check out [https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/](https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/)