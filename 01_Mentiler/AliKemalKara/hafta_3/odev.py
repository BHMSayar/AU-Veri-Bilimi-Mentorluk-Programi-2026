import time
import numpy as np

elementCount = 1_000_000
print(f"{elementCount} adet harcama tutarı üretiliyor...")

tutarDizisi = np.random.uniform(10.0, 5000.0, elementCount)  # NumPy dizisi
tutarListesi = tutarDizisi.tolist()                         # Python listesi

print("\n=== 1. TOPLAM HESAPLAMA KARŞILAŞTIRMASI ===")

# for dongusu
startTime = time.time()
loopSum = 0.0
for tutar in tutarListesi:
    loopSum += tutar
loopTime = time.time() - startTime
print(f"A) Python 'for' döngüsü süresi: {loopTime:.5f} saniye")

# sum() fonksiyonu
startTime = time.time()
builtinSum = sum(tutarListesi)
builtinTime = time.time() - startTime
print(f"B) Python yerleşik sum() süresi: {builtinTime:.5f} saniye")

# numpy toplam
startTime = time.time()
numpySum = np.sum(tutarDizisi)
numpyTime = time.time() - startTime
print(f"C) NumPy np.sum() süresi: {numpyTime:.5f} saniye")

print(f"--> NumPy, klasik döngüye göre {loopTime / numpyTime:.1f} kat daha hızlı!")
print(f"--> NumPy, yerleşik sum() fonksiyonuna göre {builtinTime / numpyTime:.1f} kat daha hızlı!")

print("\n=== 2. KDV EKLEME (%20) KARŞILAŞTIRMASI ===")

# list comp
startTime = time.time()
pythonKdvli = [tutar * 1.20 for tutar in tutarListesi]
pythonKdvSure = time.time() - startTime
print(f"A) Python List Comprehension süresi: {pythonKdvSure:.5f} saniye")

# numpy carpim
startTime = time.time()
numpyKdvli = tutarDizisi * 1.20
numpyKdvSure = time.time() - startTime
print(f"B) NumPy Vektörel Çarpım süresi: {numpyKdvSure:.5f} saniye")

print(f"--> NumPy, KDV ekleme işleminde {pythonKdvSure / numpyKdvSure:.1f} kat daha hızlı!")

print("\n=== 3. MATRİS İNDEKSLEME VE OPERASYONLAR ===")

matris = tutarDizisi.reshape(1000, 1000)
print(f"Matris boyutu (Shape): {matris.shape}")

# elemana erisim
cellValue = matris[5, 10]
print(f"-> matris[5, 10] konumundaki harcama: {cellValue:.2f} TL")

# slicing
ilkUcMusteri = matris[:3, :]
print(f"-> İlk 3 müşterinin harcama verisi boyutu: {ilkUcMusteri.shape}")

# ortalama
globalMean = matris.mean()
print(f"-> Genel Harcama Ortalaması: {globalMean:.2f} TL")

# musteri ortalamalari
musteriOrtalamalari = matris.mean(axis=1)
print(f"-> İlk 5 müşterinin ortalamaları: {np.round(musteriOrtalamalari[:5], 2)} TL")
