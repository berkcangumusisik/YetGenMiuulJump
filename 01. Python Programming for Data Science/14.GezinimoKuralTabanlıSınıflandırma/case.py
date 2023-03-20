"""
Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

# İş Problemi
Gezinomi yaptığı satışların bazı özelliklerini kullanarak seviye tabanlı
(level based) yeni satış tanımları oluşturmak ve bu yeni satış
tanımlarına göre segmentler oluşturup bu segmentlere göre yeni
gelebilecek müşterilerin şirkete ortalama ne kadar kazandırabileceğini
tahmin etmek istemektedir.
Örneğin:
Antalya’dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen
bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek
isteniyor.


Veri Seti Hikayesi
gezinomi_miuul.xlsx veri seti Gezinomi şirketinin yaptığı satışların fiyatlarını ve bu
satışlara ait bilgiler içermektedir. Veri seti her satış işleminde oluşan kayıtlardan
meydana gelmektedir. Bunun anlamı tablo tekilleştirilmemiştir. Diğer bir ifade ile
müşteri birden fazla alışverişyapmış olabilir.


miuul_gezinomi.xlsx

SaleDate : Satış Tarihi
Price: Satış için ödenen fiyat
ConceptName:Otel konsept bilgisi
SaleCityName: Otelin bulunduğu şehir bilgisi
CheckInDate:Müşterinin otelegirişitarihi
CInDay:Müşterinin otele giriş günü
SaleCheckInDayDiff: Check in ile giriş tarihi gün farkı
Season:Otele giriş tarihindeki sezon bilgisi

"""


# GÖREV 1: Aşağıdaki soruları yanıtlayınız.

# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
df = pd.read_excel("01. Python Programming for Data Science/14.GezinimoKuralTabanlıSınıflandırma/miuul_gezinomi.xlsx")
df.head()
print("-----------------------")
df.shape
print("-----------------------")
df.info()


# Soru 2: Kaç unique şehir vardır? Frekansları nedir?

df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()



# Soru 3: Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru 4: Hangi Concept'dan kaçar tane satış gerçekleşmiş?k
df["ConceptName"].value_counts()

# Soru 5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price":"sum"})
# Soru 6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price":"sum"})
# Soru 7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby(by = "SaleCityName").agg({"Price":"mean"})
# Soru 8: Conceptlere  göre PRICE ortalamaları nedir?
df.groupby(by = "ConceptName").agg({"Price":"mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(by= ["SaleCityName","ConceptName"]).agg({"Price":"mean"})


# GÖREV 2: satis_checkin_day_diff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.
bins = [-1, 7, 30, 90 , df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters","Potantial Planners","Planners","Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels = labels)
df.head(50).to_excel("eb_score.xlsx", index=False)
# GÖREV 3: Şehir,Concept, [EB_Score,Sezon,CInday] kırılımında ücret ortalamalarına ve frekanslarına bakınız

# Şehir-Concept-EB Score kırılımında ücret ortalamaları
df.groupby(by= ["SaleCityName","ConceptName","EB_Score"]).agg({"Price":["mean","count"]})
# Şehir-Concept-Sezon kırılımında ücret ortalamaları
df.groupby(by= ["SaleCityName","ConceptName","Seasons"]).agg({"Price":["mean","count"]})
# Şehir-Concept-CInday kırılımında ücret ortalamaları
df.groupby(by= ["SaleCityName","ConceptName","CInDay"]).agg({"Price":["mean","count"]})

# GÖREV 4: City-Concept-Season kırılımın çıktısını PRICE'a göre sıralayınız.

# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.
agg_df = df.groupby(by= ["SaleCityName","ConceptName","Seasons"]).agg({"Price":"mean"}).sort_values("Price", ascending=False)
agg_df.head(50)


# GÖREV 5: Indekste yer alan isimleri değişken ismine çeviriniz.

# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
agg_df = agg_df.reset_index()
agg_df.head(50)

# GÖREV 6: Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# sales_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)


# GÖREV 7: Personaları segmentlere ayırınız.

# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz
# segmentleri betimleyiniz

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# GÖREV 8: Oluşan son df'i price değişkenine göre sıralayınız.
# "ANTALYA_HERŞEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir?
agg_df.sort_values(by="Price")


new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]