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
