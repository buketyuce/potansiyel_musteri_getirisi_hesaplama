#Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

#Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve
#bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır.

import numpy as np
import pandas as pd

pd.set_option("display.max_rows", None)
df = pd.read_csv("persona.csv")

#Veriye göz attım.
df.head()
df.tail()
df.shape
df.info()

#Kaç unique SOURCE olduğunu ve Frekanslarını gözlemledim.
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

#Kaç unique PRICE olduğunu gözlemledim.
df["PRICE"].nunique()

#Hangi ülkeden kaç tane satış olduğuna baktım.
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()

#Ülkelere göre satışlardan toplam ne kadar kazanıldığına baktım.
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

#SOURCE türlerine göre satış sayılarına baktım.
df["SOURCE"].value_counts()

#Ülkelere göre PRICE ortalamalarını gözlemledim.
df.groupby(by=["COUNTRY"]).agg({"PRICE": "mean"})

#SOURCE'lara göre ortalamalarını gözlemledim.
df.groupby(by=["SOURCE"]).agg({"PRICE": "mean"})

# COUNTRY-SOURCE kırılımında PRICE ortalamalarını gözlemledim.
df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

## COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançları gözlemledim
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()

#Çıktıyı daha iyi görebilmek için çıktıyı PRICE’a göre sıraladım ve kaydettim.
agg_df = df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

#Indekste yer alan isimleri değişken ismine çevirdim.
agg_df = agg_df.reset_index()
agg_df.head()

#Age değişkenini kategorik değişkene çevirdim ve agg_df’e ekledim.
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
mylabels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

#Yeni seviye tabanlı müşterileri tanımladım ve veri setine değişken olarak ekledim.
agg_df.columns

for row in agg_df.values:
    print(row)

agg_df["customers_level_based"] =[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]

agg_df = agg_df[["customers_level_based", "PRICE"]] #gereksiz değişkenleri çıkardım.

for i in agg_df["customers_level_based"].values:
    print(i.split("_"))

#Birçok aynı sayıda segment olduğu için segmentleri tekilleştirdim.
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()
agg_df["customers_level_based"].value_counts()

#Yeni müşterileri segmentlere ayırdım.
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})


#Yeni gelen müşterileri sınıflandırdım ve ne kadar gelir getirebileceklerini tahmin ettim.

#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
#35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]