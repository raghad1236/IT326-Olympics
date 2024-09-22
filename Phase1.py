import pandas as pd

# Load the dataset
df = pd.read_csv("dataset_olympics.csv")  

# Display the attribute (column) names
print("Attribute names:\n", df.columns)

# Display the data types of each column
print("\nData types:\n", df.dtypes)

# Display the number of attributes (columns) and objects (rows)
print("\nNumber of attributes:", len(df.columns))
print("Number of objects:", len(df))
Attribute names:
 Index(['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'NOC', 'Games',
       'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'],
      dtype='object')

  
