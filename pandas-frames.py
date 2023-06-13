import pandas as pd

# DataFrame, iki boyutlu veriler ve karşılık gelen etiketleri içeren bir yapıdır. 
# Veri bilimi, makine öğrenmesi, bilimsel hesaplar ve diğer birçok verinin yoğun olduğu alanlarda kullanılmaktadır.
# iki serinin birleşimidir.

df = pd.DataFrame() # boş bir dataFrame oluşturduk.
df = pd.DataFrame([10,25,57,39]) # tek boyutlu bir dataFream oluşturduk.

data = [['Muhsin',95],['Elif',100],['Şehri',96],['Halil',75]]

df = pd.DataFrame(data, index=[1,2,3,4], columns=['name','Grade'],dtype=object) # öğrencilerin adı ve aldığı notlardan oluşan bir daraFrame oluşturduk.
# "columns=['name','Grade']" oluşturduğumuz dataFrame 'name' ve 'Grade' denen iki kolondan oluşuyor. 
# "index=[1,2,3,4]" index numarası tanımlanmadan önce 0(sıfır) indexinden başlar. fakat biz birden başlamasını istediğimiz için ek olarak index numaralarını belirttik.
# "dtype=object" burada DataFrame yapıcısında "dtype" parametresini 'object' olarak ayarladık. Bu, DataFrame'de de dize değerlerine izin verir.

dic = {"Name":['Muhsin','Elif','Şehri','Halil'], "Grade": [95,100,96,75]} # dictionary yapısı oluşturduk
df = pd.DataFrame(dic, index=['346','217','156','181']) # bu dictionary yapısını datFrame'e çevirdik. 
# Bu durumda columns değerlerini belirmemize gerek kalmadı dictionary yapısının içinde zaten oluşturulmuş.
# burada index oalrak çğrenci numaralarını kullandık. her öğrenci numarasına karşılık onların bilgileri yer alıyor.

dic_list= [ 
    {"Name": 'Muhsin', "Grade": 95},
    {"Name": 'Elif', "Grade": 100},
    {"Name": 'Şehri', "Grade": 96},
    {"Name": 'Halil', "Grade": 75}
]
# bu şekilde de aynı sonuca varırız.

df = pd.DataFrame(dic_list, index=['346','217','156','181'])

print(df)

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2]) # birleştireceğimiz iki tane seri oluşturduk

data = dict(apples = s1, oranges = s2) # bu serileri bir dictionary yapısı içinde topladık.

df = pd.DataFrame(data) # topladığımız dictionary yapısını dataFrame'e çevirdik

print(df) # oluşturduğumuz dataFrame yazdırdık.