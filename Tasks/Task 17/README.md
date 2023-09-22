# Session 17 : 20/9/2023

## Importance of stack in pandas

This operation is essential for data manipulation and analysis tasks, and it serves several important purposes:

- Data Transformation
- Multi-level Indexing
- Reshaping Data
- Data Aggregation
- Data Cleaning

## How to read mongodb data (json) in pandas ?

### For MongoDB:

We can use pymongo library to connect to our MongoDB database

```python
import pymongo
import pandas as pd

# Connect to MongoDB (replace with MongoDB URI)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database and collection
db = client["mydatabase"]
collection = db["mycollection"]

# Retrieve the data from MongoDB
data = list(collection.find())

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Now, we can work with the data in the DataFrame
print(df.head())
```

### For Json:

We can use pandas read json method to read from json file

```python
import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json('data.json')

# Now, we can work with the data in the DataFrame
print(df)
```
