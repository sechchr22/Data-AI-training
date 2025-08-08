"""
  Module for data cleaner
"""
import pandas as pd

class DataCleaner():
  @staticmethod
  def clean(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df.columns = df.columns.str.lower()
    return df