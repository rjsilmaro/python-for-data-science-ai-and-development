# Import pandas library
import pandas as pd

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
df.head(5)

# view the dimensions of the dataframe
df.shape

# Statistical Overview of dataset
df.info()

# prints information about a DataFrame including the index dtype and columns, non-null values and memory usage
df.describe()

# identify these missing values
missing_data = df.isnull()
missing_data.head(5)

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

# .dtype() to check the data type
# .astype() to change the data type
df.dtypes

## visualization
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()