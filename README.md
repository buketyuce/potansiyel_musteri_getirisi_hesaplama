# potansiyel_musteri_getirisi_hesaplama

## Veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. ##

# Veriye göz atalım.

![1](https://user-images.githubusercontent.com/101973346/163861803-2f918aa8-aa38-47e5-922b-ffaeb2a844b9.png)
![2](https://user-images.githubusercontent.com/101973346/163861828-93438d23-7169-4084-8d63-b21d1ff51788.png)


# Kaç unique SOURCE olduğunu ve Frekanslarını gözlemledim

![3](https://user-images.githubusercontent.com/101973346/163861969-809e9ee9-5927-4c2f-bc3d-ae62e735170a.png)


# Kaç unique PRICE olduğunu gözlemledim.

![4](https://user-images.githubusercontent.com/101973346/163862062-bdb14caa-8fc7-46cf-8d47-4bb3f3220d5b.png)


# Hangi ülkeden kaç tane satış olduğuna baktım.

![5](https://user-images.githubusercontent.com/101973346/163862208-547b2141-7f90-44f7-993e-973b44881b9f.png)


# Ülkelere göre satışlardan toplam ne kadar kazanıldığına baktım.

![f](https://user-images.githubusercontent.com/101973346/163862356-8c51915a-9918-4e8d-b57e-1395e55e46da.png)


# SOURCE türlerine göre satış sayılarına baktım.

![y](https://user-images.githubusercontent.com/101973346/163862442-33eb582f-a393-490b-a215-df259cb78c5c.png)


# Ülkelere göre PRICE ortalamalarını gözlemledim.

![yy](https://user-images.githubusercontent.com/101973346/163862523-099f1037-8548-4d2a-81df-7e0f1cb8f7ef.png)


# SOURCE'lara göre ortalamalarını gözlemledim.

![bb](https://user-images.githubusercontent.com/101973346/163862645-e26e34bd-2710-4847-a03b-6269ca17a79b.png)


# COUNTRY-SOURCE kırılımında PRICE ortalamalarını gözlemledim.

![55](https://user-images.githubusercontent.com/101973346/163862744-c287cdd1-0e0c-4826-842f-4519f889598f.png)


# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançları gözlemledim

![yyy](https://user-images.githubusercontent.com/101973346/163862839-b7c1f4fa-61b9-4fd6-aff3-22bd09afb5ec.png)


# Çıktıyı daha iyi görebilmek için çıktıyı PRICE’a göre sıraladım ve kaydettim.

![vvvv](https://user-images.githubusercontent.com/101973346/163862956-e02a295d-65bb-48af-9afc-e44b5ac85069.png)


# Indekste yer alan isimleri değişken ismine çevirdim.

![888](https://user-images.githubusercontent.com/101973346/163863069-8130a00a-8a7d-4a1a-b247-a436b3f6d314.png)


# Age değişkenini kategorik değişkene çevirdim ve agg_df’e ekledim.

![bbb](https://user-images.githubusercontent.com/101973346/163863191-bb17992b-489b-4a1a-8252-a93b89bb912f.png)


# Yeni seviye tabanlı müşterileri tanımladım ve veri setine değişken olarak ekledim.

![ggg](https://user-images.githubusercontent.com/101973346/163863811-7c6f8e26-3eaf-4ca8-9a06-010859d6f149.png)


# Birçok aynı sayıda segment olduğu için segmentleri tekilleştirdim.

![999](https://user-images.githubusercontent.com/101973346/163863943-140e5aac-b41b-4f39-a902-8052f6849666.png)


# Yeni müşterileri segmentlere ayırdım.

![656](https://user-images.githubusercontent.com/101973346/163864027-acb359cb-a112-4bf1-ab0e-bfebad687fb3.png)


## Yeni gelen müşterileri sınıflandırdım ve ne kadar gelir getirebileceklerini tahmin ettim. ##

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

![nnn](https://user-images.githubusercontent.com/101973346/163864131-9985afed-fa02-4865-89a9-419da6814de2.png)


# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

![Ekran görüntüsü 2022-04-18 222616](https://user-images.githubusercontent.com/101973346/163864711-81143da2-450e-415a-8a92-5e64e84d96c8.png)













