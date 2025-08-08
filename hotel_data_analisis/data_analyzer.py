"""
  Module for data analyzer
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataAnalyzer():
  @staticmethod
  def analyze(df):
    # Finding average price per city
    avg_price_per_night = df.groupby('city')['price per night'].mean()
    avg_price_per_night = avg_price_per_night.sort_values()

    # Standarize price and ratings
    numerical_cols = ['price per night', 'rating']
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Finding correlations
    price_rating_corr = df['price per night'].corr(df['rating'])
    encoded_df = pd.get_dummies(df['room type'], prefix='room')
    df = pd.concat([df, encoded_df], axis=1)
    room_type_price_corr = df[encoded_df.columns].corrwith(df['price per night'])

    return {
      'avg_price_per_night': avg_price_per_night,
      'price_rating_corr': price_rating_corr,
      'room_type_price_corr': room_type_price_corr
    }