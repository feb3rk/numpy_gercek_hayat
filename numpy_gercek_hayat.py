import numpy as np
import matplotlib.pyplot as plt

# BÖLÜM 1: Şirket Maaş Analizi
# Görev 1: Maaşları Simüle Etme
np.random.seed(42)
maaslar = np.random.randint(3000, 15001, 500)

ortalama_maas = np.mean(maaslar)
max_maas = np.max(maaslar)
min_maas = np.min(maaslar)

print(f"Ortalama Maaş: {ortalama_maas:.2f} TL")
print(f"Maksimum Maaş: {max_maas} TL")
print(f"Minimum Maaş: {min_maas} TL")

plt.hist(maaslar, bins=20, edgecolor='black')
plt.title('Maaş Dağılımı')
plt.xlabel('Maaş (TL)')
plt.ylabel('Çalışan Sayısı')
plt.show()

# Görev 2: Departmanlara Atama
departman_isimleri = {1: "Mühendislik", 2: "Muhasebe", 3: "Pazarlama"}
departmanlar = np.random.choice([1, 2, 3], size=500)

for dept in [1, 2, 3]:
    ortalama = np.mean(maaslar[departmanlar == dept])
    print(f"{departman_isimleri[dept]} - Ortalama Maaş: {ortalama:.2f} TL")

# BÖLÜM 2: Hava Durumu Verileri Üretme ve Analiz
# Görev 3: Günlük Sıcaklıkları Simüle Etme
temperatures = np.random.uniform(-10, 40, 365)
ortalama_sicaklik = np.mean(temperatures)
en_sicak_gun = np.max(temperatures)
en_soguk_gun = np.min(temperatures)

print(f"Ortalama Sıcaklık: {ortalama_sicaklik:.2f} °C")
print(f"En Sıcak Gün: {en_sicak_gun:.2f} °C")
print(f"En Soğuk Gün: {en_soguk_gun:.2f} °C")

plt.plot(temperatures, color='red')
plt.title('Yıllık Günlük Sıcaklık Değişimi')
plt.xlabel('Gün')
plt.ylabel('Sıcaklık (°C)')
plt.show()

# BÖLÜM 3: Ürün Satış Analizi
# Görev 4: Günlük Satışları Simüle Etme
urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
satislar = np.random.randint(10, 101, (5, 30))

urun_toplamlari = np.sum(satislar, axis=1)
urun_ortalamalari = np.mean(satislar, axis=1)

for i, urun in enumerate(urunler):
    print(f"{urun} - Toplam Satış: {urun_toplamlari[i]} Adet, Ortalama Günlük Satış: {urun_ortalamalari[i]:.2f} Adet")

plt.bar(urunler, urun_toplamlari, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Ürün Bazında Toplam Satış')
plt.xlabel('Ürünler')
plt.ylabel('Toplam Satış')
plt.show()