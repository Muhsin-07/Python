import pandas as pd

df = pd.read_csv("datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz
result = df.head(10)

# # 2- Toplam kaç kayıt vardır
result = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir
result = df["player_height"].mean()

# # # 4- En yüksek maaşı ne kadardır
result = df["player_height"].max()

# # # 5- En yüksek maaşı alan oyuncu kimdir 
result = df[df["player_height"]==df["player_height"].max()]["player_name"].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["age"] >= 20) & (df["age"] < 25)][["player_name","team_abbreviation","age"]].sort_values("age", ascending = False)

# # # 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir
result = df[df["player_name"] == "Emanual Davis"]["team_abbreviation"].iloc[0]

# # # 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir
result = df.groupby("team_abbreviation").mean()["player_height"]

# # 9- Kaç farklı takım mevcut ?
result = len(df.groupby("team_abbreviation"))
result = df["team_abbreviation"].nunique()

# # 10- Her takımda kaç oyuncu oynamaktadır
result = df["team_abbreviation"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz
df.dropna(inplace = True)
result = df[df["player_name"].str.contains("and")]

def str_find(player_name):
    if "and" in player_name.lower():
        return True
        return False

result = df[df["player_name"].apply(str_find)]

print(result)