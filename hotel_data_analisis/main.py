import pandas as pd
from data_cleaner import DataCleaner
from data_analyzer import DataAnalyzer

def main():
  # load dataset here
  df = pd.read_csv("data/hotel_data.csv")
  df = DataCleaner.clean(df)
  analysis = DataAnalyzer.analyze(df)
  return analysis

if __name__ == "__main__":
  analysis = main()
  result = """
    from the analisis: {}

    We have the following insights:
    1. The highest prices are located in Chichago and the lowest prices are in San Francisco
    2. There is almost a none relation between the price per night and the rating
    3. The Standard Rooms show the strongest positive correlation with price, possibly due to higher demand or better amenities
    4. Economy rooms are predictably the chepeast ones
  """.format(str(analysis))
  with open('conclusions.txt', 'w') as file:
    file.write(result)