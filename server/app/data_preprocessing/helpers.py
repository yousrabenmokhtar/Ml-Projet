import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from scipy.stats import spearmanr

def drop_duplicates(df):
  count_duplicates  = df.duplicated().sum()
  print(f"We found {count_duplicates} duplicates in our dataset")
  if count_duplicates > 0 :
    df.drop_duplicates(inplace=True)
  return df

def drop_columns_with_high_missing_values(df,threshold=0.85):
  null_percentage = df.isnull().mean()
  columns_to_drop = null_percentage[null_percentage > threshold].index
  df.drop(columns=columns_to_drop,inplace=True)
  return df

def replace_null_values(df,col,strategy,value=None):
  # strategy = 'mean' | 'median' | 'most_frequent' | 'constant'
  imputer = SimpleImputer(strategy=strategy,fill_value=value)
  df[col] = imputer.fit_transform(df[[col]]).T[0] # [1,2,3]
  return df

def encode(df,col,target,corr_threshold=0.5,high_cardinality_threshold=12):
    # check if the type of col is boolean
    if df[col].dtypes == 'bool':
      print("Hello")
      df[col] = df[col].apply(lambda val : int(val))
      df['sex'] = df['sex'].astype(int)
      return df
    oe = OrdinalEncoder()
    encoded_col = oe.fit_transform(df[[col]])
    # Step 2: Compute Spearman correlation
    coor,_ = spearmanr(encoded_col.flatten(),df[target])
    if abs(coor) > corr_threshold:
        df[col] = encoded_col
    elif df[col].nunique() < high_cardinality_threshold:
        df = pd.get_dummies(df,columns=[col],drop_first=True,dtype='int')
    else:
        freqs = df[col].value_counts(normalize=True)
        df[col] = df[col].map(freqs)
    return df

def normalize(df):
  pass
def standarlize(df):
  pass