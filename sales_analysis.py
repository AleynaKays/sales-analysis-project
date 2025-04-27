import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Veriyi oku
df = pd.read_csv('sales_data.csv')

# 2. İlk 5 satırı görüntüle
print("İlk 5 Satır:")
print(df.head())

# 3. Eksik verileri kontrol et
print("\nEksik Veri Kontrolü:")
print(df.isnull().sum())

# 4. Tarih sütununu datetime'a çevir
df['Tarih'] = pd.to_datetime(df['Tarih'])
df['Ay'] = df['Tarih'].dt.month

# 5. En çok satan ürünler
en_cok_satan_urunler = df.groupby('Urun_Adi')['Satis_Adedi'].sum().sort_values(ascending=False)
print("\nEn Çok Satan Ürünler:")
print(en_cok_satan_urunler)

# 6. Aylık ciro
aylik_satis = df.groupby('Ay')['Toplam_Tutar'].sum()
print("\nAylık Ciro:")
print(aylik_satis)

# 7. Grafik çiz
aylik_satis.plot(kind='bar')
plt.title('Aylık Satışlar')
plt.xlabel('Ay')
plt.ylabel('Toplam Ciro')
#plt.show()

# 8.En çok ciro yapan ürünler 
en_cok_ciro_urunler = df.groupby('Urun_Adi')['Toplam_Tutar'].sum().sort_values(ascending=False)
print("\nEn Çok Ciro Yapan Ürünler:")
print(en_cok_ciro_urunler)
 
# 9.grafik
en_cok_ciro_urunler.plot(kind='barh')
plt.title('Ürün Bazında Ciro')
plt.xlabel('Toplam Ciro')
plt.ylabel('Ürün')
#plt.show()

# 10. Müşteri Bazlı Ortalama Satış Tutarı Analizi
musteri_ortalama = df.groupby('Musteri_ID')['Toplam_Tutar'].mean().sort_values(ascending=False)
print("\nMüşteri Bazlı Ortalama Satış Tutarı:")
print(musteri_ortalama)

# 11. Müşteri Bazlı Ortalama Satış Tutarı Bar Chart
musteri_ortalama.plot(kind='bar')
plt.title('Müşteri Bazlı Ortalama Alışveriş Tutarı')
plt.xlabel('Müşteri ID')
plt.ylabel('Ortalama Tutar')
plt.xticks(rotation=45)  # Müşteri ID'leri eğik yazılsın diye
plt.show()

