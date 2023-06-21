import pandas as pd

df = pd.read_csv("datasets/GBvideos.csv")

# 1) lk 10 kayıt
result = df.head(10)

# 2) kinci 5 kayıt
result = df[5:].head(5)

# 3) Dataset' de bulunan kolon isimleri ve sayısı
result = df.columns
result = len(df.columns)

# 4) kolon silme ve geriye kalanları yazdırma
df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"], axis=1)
result = df.columns

# 5) like ve dislike''ların ortlaması 
result = df["likes"].mean()
result = df["dislikes"].mean()

# 6) ilk 50 videonun like ve dislike kolonlarının ortalamaları
result = df["likes"].head(20).mean()
result = df["dislikes"].head(20).mean()

# 7) En çok görüntülenen video
result = df.loc[df['views'].idxmax()]

# 8) En düşük görüntülenen video
result = df.loc[df['views'].idxmin()]

# 9) En fazla görüntülenen ilk 10 video
result = df.sort_values("views", ascending = False).head(10)

# 10) Kategoriye göre beğeni ortalamaları ıralı şekilde
result = df.groupby("category_id").mean("likes").sort_values(["likes"])["likes"].head(5)

# 11) Kategoriye göre yorum sayıları yukarıdan aşağıya
result = df.groupby("category_id").mean("comment_count").sort_values("comment_count", ascending = False)["comment_count"].head(5)

# 12)* Her kategoride kaç video var
result = df.groupby("category_id").value_counts()

# 13) Her videonun title uzunluk bilgisi
df["text_length"] = df.title.str.len()
result = df[["title","text_length"]]

# 14) Her video için kullanılan tag sayısı yen ibir kolon oluşturularak yapıldı
result = df["tags"].str.split("|").apply(len)

# 15)  En popüler videoları listeleme (like ve dislike oranına göre)
def likedislikeoranhesapla(dataset):
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike  in liste: 
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))

    return oranListesi

df["beğeni_orani"] = likedislikeoranhesapla(df)

result = df[["channel_title","likes","dislikes","beğeni_orani"]].head(5)

print(result)