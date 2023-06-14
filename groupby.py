import pandas as pd
import numpy as np

df = pd.read_json('datasets/personel.json', encoding='UTF-8')
result = df
result = result.sum()["Maaş"] # maaş toplamı yazırılmış olur.
result = df.groupby("Departman") # departman altında bir guruplandırma işlemi yapar.
result = df.groupby("Departman").groups # oluşturulan gurupları .groups metodu ile görebiliriz.

# semtler = df.groupby("Semt") # semtlerine göre guruplandırma yaptık

# for name,group in semtler:
#     print(name)
#     print(group) 
#     # yaptığımız gruplandırmayı ekrana aldık. 
#     # ekrana öncelikle semtin adı gelir.
#     # sonra grup bilgisini alırız.

# deparman = df.groupby("Departman")

# for name,group in deparman:
#     print(name)
#     print(group) 
#     # yaptığımız gruplandırmayı ekrana aldık. 
#     # ekrana öncelikle departman adı gelir.
#     # sonra grup bilgisini alırız.

result = df.groupby("Departman").get_group("Bilgi İşlem") # burada departman altında toplanan guruplardan bilgi işlemi alıp yazdırdık.
result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").sum() # dersek eğer yaş, maaşların toplamına erişebiliriz. bunlara ek olarak çalışan adaları ve departmanları da ekrana yazdırılır.
result = df.groupby("Departman")[["Yaş","Maaş"]].sum() # sadece yaş ve maaş bilgilerinin toplamı yazdırılır.
result = df.groupby("Departman")[["Yaş","Maaş"]].mean() # .mean ile bunların ortalamasını almış oluruz.
result = df.groupby("Semt")["Çalışan"].count() # semtlere göre çalışan sayısını yazdırır.
result = df.groupby("Departman")["Yaş"].max() # her departmandaki max yaşı ekrana yazdırır.
result = df.groupby("Departman")["Maaş"].max()
result = df.groupby("Departman")["Maaş"].max()["İnsan Kaynakları"] # insan kaynaklarında çalışan kişilerin en yüksek maaş alanını yazdırır.
result = df.groupby("Departman")[["Yaş","Maaş"]].agg(np.mean) # departman altındaki gurubun yaş ortalaması ekrana yazdırlır. (numpy ile)
result = df.groupby("Departman")[["Yaş","Maaş"]].agg([np.max,np.min,np.mean,np.sum]) # .agg metodu ile tek satırda sınırsız bir şekilde ortalama, toplam gibi bir çok veriye aynı anda erişebiliriz.
result = df.groupby("Departman")[["Yaş","Maaş"]].agg([np.max,np.min,np.mean,np.sum]).loc["Muhasebe"] # loc metodu ile istediğmiz alanı seçebiliriz.

print(result)