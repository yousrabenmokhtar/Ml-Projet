import pandas as pd

def drop_duplicates(df):
  count_duplicates  = df.duplicated().sum()
  print(f"We found {count_duplicates} duplicates in our dataset")
  if count_duplicates > 0 :
    df.drop_duplicates(inplace=True)

def drop_columns_with_high_missing_values(df,threshold=0.7):
  null_percentage = df.isnull().mean()
  columns_to_drop = null_percentage[null_percentage > threshold].index
  df.drop(columns=columns_to_drop,inplace=True)

def one_hot_encoder(df):
  pass
def ordinal_encoder(df):
  pass
def normalize(df):
  pass
def standarlize(df):
  pass