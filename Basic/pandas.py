# useful pages
# https://sacko.tistory.com/18
# https://riptutorial.com/ko/pandas/
#
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
df.drop(['row'], inplace=True) # 실행한 객체의 값을 변경
df = df.dropna(axis = 0) # np.NaN (결측값) 있는 행 Drop

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

A = series > 0 # A is also series with boolean values which meet the condition
series[series > 0] # series의 배열 값으로 Index는 Column명, Value는 boolean를 가진 series를 넣으면 True인 Column만 모아서 시리즈를 만듦
                   # 그냥 위와 같은 표현은 씨리즈 중 조건을 만족하는 컬럼만 추출. 로 기억 하면 될듯
series.sum() # series의 모든 value를 더한 단일 값을 출력. DataFrame.sum()과는 다르다.(DataFrame.sum()은 Series를 만든다.)



## Save to CSV from Pandas Data Frame
# Save predictions in format used for competition scoring
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': preds_test})
output.to_csv('submission.csv', index=False)

