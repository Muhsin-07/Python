import pandas as pd

# customers = {
#     "CustomerId": [1,2,3,4],
#     "FirstName": ["Muhsin","Halil","Şehmus","Elif"],
#     "LastName": ["Demir","Korkmaz","Erdoğan","Mercan"]
# }

# orders = {
#     "OrdersId": [12,13,14,15],
#     "CustomerId": [1,2,5,7],
#     "OrderData": ["2023-07-13","2023-09-17","2023-10-23","2023-12-03",]
# }

# df_customer = pd.DataFrame(customers, columns=["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns=["OrdersId","CustomerId","OrderData"])

# print(df_customer)
# print(df_orders)

# result = pd.merge(df_customer,df_orders,how="inner") # siparişi olan kullanıcılar gelir.
# result = pd.merge(df_customer,df_orders,how="left") # siparişi olsun olmasın hepsini alırız. sipariş bilgisi eksik olan yerlere Nan değeri yazdırılır.
# result = pd.merge(df_customer,df_orders,how="right") # tüm siparişler getirilir. kayıtlı olmayan kullanıcıların ad ve soyad ksımına Nan yazdırırlır.
# result = pd.merge(df_customer,df_orders,how="outer") # tüm kullanıcıları yazdırır. siparişi olan olmayan veya kayıtlı olan olmayan herkesi. Kolon bazında toplar.

customersA = {
    "CustomerId": [1,2,3,4],
    "FirstName": ["Muhsin","Halil","Şehmus","Elif"],
    "LastName": ["Demir","Korkmaz","Erdoğan","Mercan"]
}

customersB = {
    "CustomerId": [6,7,8,9],
    "FirstName": ["Yağmur","Çınar","Ali","Buse"],
    "LastName": ["Atasoy","Akyüz","Değer","Çelik"]
}

df_customerA = pd.DataFrame(customersA, columns=["CustomerId","FirstName","LastName"])
df_customerB = pd.DataFrame(customersB, columns=["CustomerId","FirstName","LastName"])


result = pd.concat([df_customerA,df_customerB]) # toplama işlemi yapar her iki datayı birleştirir. (varsayılan axis=0)
result = pd.concat([df_customerA,df_customerB],axis=1) # dataları yan yana getirir.

print(result)