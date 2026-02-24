import pandas as pd
from pandas import read_csv

with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as squirrel_data:
    sq_data = read_csv(squirrel_data)
gray = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
print(sq_data[sq_data["Primary Fur Color"] == "Gray"])
red = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black = len(sq_data[sq_data["Primary Fur Color"] == "Black"])

with open("squirrel_count.csv", mode="w") as squirrel_count:
    data = {
        "Fur Color": ["gray", "red", "black"],
        "Count": [gray, red, black],
    }

    df = pd.DataFrame(data)
    df.to_csv("squirrel_count.csv")