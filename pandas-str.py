import pandas as pd

data = pd.read_csv("datasets/nba.csv")

data.dropna(inplace=True)

# data["player_name"] = data["player_name"].str.upper()
# data["player_name"] = data["player_name"].str.lower()
# data["index"] = data["player_name"].str.find("a") 
# index kolonu oluşturuldu ve o satrda çıkan ilk 'a' nın indexsi o kolon aeklendi.
# data = data[data.player_name.str.contains("dennis rodman")]
# data = data.player_name.str.replace(" ", "-")
data[["First_Nama","Last_Name"]] = (data["player_name"].loc[data["player_name"].str.split().str.len()==2].str.split(expand=True))
data = data[["player_name","First_Nama","Last_Name","team_abbreviation"]]

print(data.head(55))