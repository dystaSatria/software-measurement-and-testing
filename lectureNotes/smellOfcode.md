# Smell of Code


* DRY Prensibi

Önce tekrarlanan bir kod örneği: 

```python
def hesapla_dikdortgen_alan(uzunluk, genislik):
    alan = uzunluk * genislik
    return alan

def hesapla_dikdortgen_cevre(uzunluk, genislik):
    cevre = 2 * (uzunluk + genislik)
    return cevre

def hesapla_kare_alan(kenar):
    alan = kenar * kenar
    return alan

def hesapla_kare_cevre(kenar):
    cevre = 4 * kenar
    return cevre
```

DRY prensibine uygun olarak, bu tekrarı kaldıralım ve ortak bir fonksiyon kullanalım: 


```python
def hesapla_alan(uzunluk, genislik=None, kenar=None):
    if kenar is not None:
        return kenar * kenar  # kare alanı
    elif uzunluk is not None and genislik is not None:
        return uzunluk * genislik  # dikdörtgen alanı
    else:
        raise ValueError("Geçersiz argümanlar")

def hesapla_cevre(uzunluk, genislik=None, kenar=None):
    if kenar is not None:
        return 4 * kenar  # kare çevresi
    elif uzunluk is not None and genislik is not None:
        return 2 * (uzunluk + genislik)  # dikdörtgen çevresi
    else:
        raise ValueError("Geçersiz argümanlar")

```

* Tek Sorumluluk İlkesi

Önce tekrarlanan bir kod örneği: 

```python
class VeritabaniYonetimi:
    def baglan(self):
        # Veritabanına bağlanma işlemleri...

    def veri_al(self, sorgu):
        # Veri alım işlemleri...

    def veri_guncelle(self, sorgu, veri):
        # Veri güncelleme işlemleri...

    def baglantiyi_kapat(self):
        # Bağlantıyı kapatma işlemleri...

```

Değiştirilecek kullanalım: 


```python
def hesapla_alan(uzunluk, genislik=None, kenar=None):
    if kenar is not None:
        return kenar * kenar  # kare alanı
    elif uzunluk is not None and genislik is not None:
        return uzunluk * genislik  # dikdörtgen alanı
    else:
        raise ValueError("Geçersiz argümanlar")

def hesapla_cevre(uzunluk, genislik=None, kenar=None):
    if kenar is not None:
        return 4 * kenar  # kare çevresi
    elif uzunluk is not None and genislik is not None:
        return 2 * (uzunluk + genislik)  # dikdörtgen çevresi
    else:
        raise ValueError("Geçersiz argümanlar")

```
