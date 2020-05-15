# Reading in Data

Though we can create dataframes from scratch, usually we don't. Most of the time in this class, we'll be reading in data from `.csv` (comma-separated values) files which we can think of as tablular data in Excel. If you've ever worked with Excel, you would definitely have worked with `.csv` files. To start off, we first need to import `pandas` to use build-in functions that will allow us to read in these `.csv` files.

import pandas as pd

Now we have to find what the path to our `csv` file is. This will depend on where you put your files. For instance, if we have the data file in a higher level we would need to use `..` to access it. If the data file is in a lower level, we would need to traverse the filetree using `/` to get to it.

```{note}
The default syntax for reading `.csv` files in is `pd.read_csv("{filepath}")`

```

## Example 0

```
|-- notebooks
|       |--reading-data.ipynb
|       |-- data.csv
|
```

To read the file `data.csv`, we can just read it in with its filename.

```
df = pd.read_csv('data.csv')
```

## Example 1

```
|-- notebooks 
|       |--reading-data.ipynb
|
|-- data.csv
|
```

To read the file `data.csv`, we would need to use `..` to go up a directory.

```
df = pd.read_csv('../data.csv')
```

## Example 2

```
|-- notebooks
|       |--reading-data.ipynb
|       |--data-files
|              |--data.csv
|
```

To read the file `data.csv`, we would need to use `/` to go down a directory.

```
df = pd.read_csv('data-files/data.csv')
```

## Example 3 (my preferred way of structuring my file)

```
|-- notebooks
|       |--reading-data.ipynb
|
|-- data-files
|       |--data.csv
|
```

To read the file `data.csv`, we would need to use `..` to go up a directory and `/` to go down a directory.

```
df = pd.read_csv('../data-files/data.csv')
```

```{tip}
If you're not sure about the path of some file, you can drag the file into terminal/command prompt which will give you its exact path.

```