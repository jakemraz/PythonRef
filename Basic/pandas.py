
import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns
y = home_data.SalePrice

# Create DataFrame using necessary columns
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
X.describe()

# Basic command
df.shape
df.info()
df.columns
df.dtypes
df.head()
df.tail()

df.isnull().sum() # count the number of null for each columns
df.isnull().sum() / df.shape[0] # portion of null for each columns
df['column_name'].unique() # check unique values
df['A'] = df['B'].str[:5]  # make a new column
df['A'] = df['B'].str[-5:]

df = df.drop(['column'], axis=1)
df = df.drop(['row'])

df= df.rename(columns={'A' : 'B'}) # change column name
df= pd.DataFrame(df, columns=['A', 'C', 'B']) # change column order
result = pd.concat([df1, df2], ignore_index=True) # concat two columns
df.duplicated() # check duplicate
df.drop_duplicates() # drop duplicate


# Series and DataFrame
a = X_train['LotFrontage'] # can not put multiple item
type(a)
# >> pandas.core.series.Series

a = X_train[['LotFrontage']]
type(a)
# >> pandas.core.frame.DataFrame


## pandas series
series_var.isnull()
# >> return Series with values replaced to boolean
series_var.any()
# >> return True:numpy.bool_ if there is True at least



## Save to CSV from Pandas Data Frame
# Save predictions in format used for competition scoring
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': preds_test})
output.to_csv('submission.csv', index=False)


##########################
##### Missing Values #####
##########################

## Drop
# Get names of columns with missing values
cols_with_missing = [col for col in X_train.columns
                     if X_train[col].isnull().any()] 
# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis=1) # axis=0:row/1:colume

## Imputation
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
# what is different between fit_transform and transform?

# Imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

## An Extention to Imputation
# Make copy to avoid changing original data (when imputing)
X_train_plus = X_train.copy()
X_valid_plus = X_valid.copy()

# Make new columns indicating what will be imputed
for col in cols_with_missing:
    X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
    X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

