# dsprojects
in this repository i keep all of my data science projects that i've been working on along with documentation i also have created a class for handling pandas simple data analysis tasks , the following is the documentation of class which is used for all of my ds projects


# DataFrameHandler Documentation

The `DataFrameHandler` class provides a set of static methods for working with CSV files and analyzing the data in a pandas DataFrame.

## Methods

### `read_csv_file(file_path)`

Reads a CSV file and returns a pandas DataFrame.

**Parameters:**
- `file_path (str)`: The path to the CSV file.

**Returns:**
- `pd.DataFrame`: The DataFrame containing the CSV data.

**Exceptions:**
- `FileNotFoundError`: Raised if the specified file is not found.
- `pd.errors.EmptyDataError`: Raised if the file is empty.
- `Exception`: Raised if any other error occurs while reading the CSV file.

### `describe_data(df)`

Describes the data in the DataFrame using `df.info()`, `len(df)`, `df.shape[1]`, `df.describe()`, and prints the sum of null values in each column.

**Parameters:**
- `df (pd.DataFrame)`: The DataFrame to describe.

**Returns:**
- `None`

### `convertToOrdinalEncoder(uniquecolumnCats, orderedList)`

Initializes an `OrdinalEncoder` with the specified ordered categories.

**Parameters:**
- `uniquecolumnCats (list)`: Unique categories in the column.
- `orderedList (list)`: Ordered list of categories.

**Raises:**
- `AssertionError`: Raised if the unique categories don't match the ordered categories.

### `encode_ordinal_columns(df, columns, encodedcolumns, categories_list)`

Encodes specified columns in the DataFrame using an `OrdinalEncoder`.

**Parameters:**
- `df (pd.DataFrame)`: The DataFrame containing the data.
- `columns (list)`: List of column names to encode.
- `encodedcolumns (list)`: List of new column names for the encoded data.
- `categories_list (list of lists)`: List of categories for each column.

**Returns:**
- `pd.DataFrame`: The DataFrame with encoded columns.

**Raises:**
- `ValueError`: Raised if the number of columns and the number of category lists are not the same.

### `check_correlation(df, columns)`

Checks the correlation between specified columns in the DataFrame.

**Parameters:**
- `df (pd.DataFrame)`: The DataFrame containing the data.
- `columns (list)`: List of column names to check correlation.

**Returns:**
- `pd.DataFrame`: The correlation matrix for the specified columns.

**Raises:**
- `ValueError`: Raised if any of the specified columns are not present in the DataFrame.

## Usage

Here's an example of how to use the `DataFrameHandler` class:

```python
# Read a CSV file
df = DataFrameHandler.read_csv_file('data.csv')

# Describe the data
DataFrameHandler.describe_data(df)

# Encode ordinal columns
columns = ['column1', 'column2']
encodedcolumns = ['encoded_column1', 'encoded_column2']
categories_list = [['A', 'B', 'C'], ['X', 'Y', 'Z']]
df = DataFrameHandler.encode_ordinal_columns(df, columns, encodedcolumns, categories_list)

# Check correlation
correlation_matrix = DataFrameHandler.check_correlation(df, ['column1', 'column2', 'encoded_column1', 'encoded_column2'])
print(correlation_matrix)
