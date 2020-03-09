###############################
##### Make Validation Set #####
###############################

# validation set
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)

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
my_imputer = SimpleImputer(strategy='median')
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
# what is different between fit_transform and transform?
# 알겠다. fit을 통해서 분포를 추정하고 transform을 통해 학습 데이터의 null값을 imputation 한다.
# 따라서 위 코드는 아래와 같다
my_imputer.fit(X_train)
imputed_X_train = pd.DataFrame(my_imputer.transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

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

