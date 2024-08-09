import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from IPython.display import display
import io

class DataFrameHandler:
    @staticmethod
    def read_csv_file(file_path):
        """
        Reads a CSV file and returns a pandas DataFrame.

        Parameters:
        file_path (str): The path to the CSV file.

        Returns:
        pd.DataFrame: The DataFrame containing the CSV data.
        """
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError as e:
            print(f"File not found: {file_path}")
            raise e
        except pd.errors.EmptyDataError as e:
            print("No data in the file.")
            raise e
        except Exception as e:
            print("An error occurred while reading the CSV file.")
            raise e

    @staticmethod
    def describe_data(df):
        """
        Describes the data in the DataFrame using df.info(), len(df), df.shape[1],
        df.describe(), and prints the sum of null values in each column.

        Parameters:
        df (pd.DataFrame): The DataFrame to describe.

        Returns:
        None
        """
        # Capture the output of df.info() to a string
        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        
        # Parsing info_str to create a DataFrame
        info_lines = info_str.split('\n')
        info_data = []
        for line in info_lines[3:-2]:  # Skip the header and footer lines
            parts = line.split()
            if len(parts) >= 5:
                info_data.append(parts[:5])
            elif len(parts) == 4:
                info_data.append(parts + [""])
                
        info_df = pd.DataFrame(info_data, columns=["# Column", "Column name", "Non-Null Count", "Missing", "Dtype"])

        # Displaying DataFrame information as a styled table
        display(info_df.style.set_caption("DataFrame Info").set_table_styles([{
            'selector': 'table',
            'props': [('border', '1px solid black'), ('border-collapse', 'collapse')]
        }, {
            'selector': 'th, td',
            'props': [('border', '1px solid black'), ('padding', '8px')]
        }]))

        print("\nNumber of rows and columns:")
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {df.shape[1]}")

        
        display(df.describe().style.set_caption("Data Description").set_table_styles([{
            'selector': 'table',
            'props': [('border', '1px solid black'), ('border-collapse', 'collapse')]
        }, {
            'selector': 'th, td',
            'props': [('border', '1px solid black'), ('padding', '8px')]
        }]))

        print("\nSum of null values in each column:")
        display(df.isnull().sum().to_frame('Null Counts').style.set_caption("Null Counts").set_table_styles([{
            'selector': 'table',
            'props': [('border', '1px solid black'), ('border-collapse', 'collapse')]
        }, {
            'selector': 'th, td',
            'props': [('border', '1px solid black'), ('padding', '8px')]
        }]))

    @staticmethod
    def convertToOrdinalEncoder(uniquecolumnCats, orderedList):
        """
        Initializes an OrdinalEncoder with the specified ordered categories.

        Parameters:
        uniquecolumnCats (list): Unique categories in the column.
        orderedList (list): Ordered list of categories.

        Returns:
        None
        """
        assert set(orderedList) == set(uniquecolumnCats), "Unique categories don't match ordered categories."
        oe = OrdinalEncoder(categories=[orderedList])

    @staticmethod
    def encode_ordinal_columns(df, columns, encodedcolumns, categories_list):
        """
        Encodes specified columns in the DataFrame using an OrdinalEncoder.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to encode.
        encodedcolumns (list): List of new column names for the encoded data.
        categories_list (list of lists): List of categories for each column.

        Returns:
        pd.DataFrame: The DataFrame with encoded columns.
        """
        if len(columns) != len(categories_list):
            raise ValueError("The number of columns and the number of category lists must be the same.")

        oe = OrdinalEncoder(categories=categories_list)
        df[encodedcolumns] = oe.fit_transform(df[columns])

        return df

    @staticmethod
    def check_correlation(df, columns):
        """
        Checks the correlation between specified columns in the DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        columns (list): List of column names to check correlation.

        Returns:
        pd.DataFrame: The correlation matrix for the specified columns.
        """
        # Debugging: Print column names in the DataFrame
        print("Columns in DataFrame:", df.columns.tolist())

        # Debugging: Check if all specified columns are in the DataFrame
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

        # Debugging: Check data types of specified columns
        for col in columns:
            print(f"Data type of column '{col}': {df[col].dtype}")

        # Calculate the correlation matrix for the specified columns
        correlation_matrix = df[columns].corr()

        return correlation_matrix

