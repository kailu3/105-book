# Conditional Selection on Arrays

import numpy as np
import pandas as pd

Often when dealing with arrays, we sometimes want to select elements from them based on a condition. For instance, suppose we only wanted to select elements that were larger than a number or some criterion. We can do this utilizing comparison operators or in other words Booleans. We can start with an example:

Suppose that we had daily temperature data for Vancouver and wanted to look at the **maximum** temperatures for each day. We first load the data in using `Pandas` (another library that we'll cover in the next section).

# 2019 daily max temperatures
url = "https://raw.githubusercontent.com/kailu3/105-book/master/data/vancouver-2019-max-temp.csv"
daily_max = pd.read_csv(url)['degC'].values

Our first step is to look at some basic summary statistics using what we learned from the last section.

print("Minimum temp:", np.min(daily_max))
print("Maximum temp:", np.max(daily_max))
print("Mean temp:", np.mean(daily_max))
print("Median temp:", np.mean(daily_max))
print("Variance:", np.var(daily_max))
print("Standard deviation:", np.std(daily_max))

```{note}
The summary statistics we compute are for the **maximum** daily temperatures in Vancouver in 2019

```

Now suppose we had a question, say: **How many times in 2019 was the maximum temperature below 20 degrees Celsius?**

We can first apply a boolean operator (`< 20`) to our entire array. For each element in the array, it will compute whether it is less than 20 (`True` or `False`). We can use `==`, `!=`, `<`, `>`. `<=`. `>=` (equals, not equals, less than, greater than, less than or equal to, greater than or equal to) depending on the type of question we have.

daily_max < 20

Since `True` is equivalent to 1 and `False` is equal to 0, we can sum up `daily_max < 20` to get the total number of days the maximum temperature was less than 20 degress Celsius.

np.sum(daily_max < 20)

Alternatively, say we were interested in the temperatures at which the maximum temperature was less than 20 degrees Celsius. We can use the syntax `array[boolean array]` to select from our `daily_max` array.

daily_max[daily_max < 20]

We can also combine boolean statements to use multiple conditions! Say we wanted the temperatures between 20 *and* 30 degrees Celsius.

daily_max[(daily_max >= 20) & (daily_max <= 30)]

```{note}
`|` represents "or"

`&` represents "and"
```

Alternatively, say we wanted the temperatures greater than 20 degrees Celsius *or* less than 10 degrees Celsius.

daily_max[(daily_max > 20) | (daily_max < 10)]

