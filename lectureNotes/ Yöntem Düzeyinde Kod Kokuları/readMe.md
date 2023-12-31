#  Yöntem Düzeyinde Kod Kokuları


* Ölü Kod (Dead Code):
Kode yang tidak pernah diakses atau dieksekusi dalam aplikasi. Contohnya:

```python

def example_function():
    # Kode yang tidak pernah dipanggil
    unused_variable = 10
    print("Hello, World!")

# Kode yang mengandung variabel tak terpakai (dead code)
```

* Uzun Parametre Listesi (Long Parameter List):
Fungsi atau metode dengan daftar parameter yang panjang. Contohnya:
```python

def example_function():
    # Kode yang tidak pernah dipanggil
    unused_variable = 10
    print("Hello, World!")

# Kode yang mengandung variabel tak terpakai (dead code)
```

* Kara koyun (Black Sheep)
  
  [Tekan ini](https://medium.com/thinkster-io/code-smell-black-sheep-method-9fc4a952cee6)

* Tanrı Yöntemi


 ```python 
  class Processor:
    def __init__(self):
        self.data = []

    # God Method: melakukan terlalu banyak hal
    def process_data(self, file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        # Melakukan banyak operasi terkait data
        for line in lines:
            if 'error' in line:
                self.data.append(line)

        # Operasi lain yang tidak terkait dengan tugas utama metode ini
        self.analyze_data()
        self.generate_report()

    # Metode tambahan yang seharusnya dipisahkan
    def analyze_data(self):
        # Analisis data
        pass

    # Metode tambahan yang seharusnya dipisahkan
    def generate_report(self):
        # Menghasilkan laporan
        pass


```

*  Tuhah çözmesi "Oddball" 
"Oddball" solution adalah ketika sebuah masalah dipecahkan dengan cara yang tidak lazim atau berbeda dari solusi yang umumnya diterima. Berikut ini adalah contoh kode Python yang mengandung dua metode untuk memecahkan masalah matematika sederhana. Yang pertama mewakili solusi yang umum dan diharapkan, sedangkan yang kedua merupakan contoh "oddball" atau pendekatan yang berbeda:

```python
# Solusi Normal / Umum
def penjumlahan_1(n):
    # Menjumlahkan angka dari 1 hingga n
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Solusi "Oddball"
def penjumlahan_2(n):
    # Menggunakan rumus Gauss untuk menjumlahkan angka dari 1 hingga n
    total = (n * (n + 1)) // 2
    return total

# Penggunaan kedua fungsi
n = 100
print("Jumlah (Fungsi 1):", penjumlahan_1(n))
print("Jumlah (Fungsi 2):", penjumlahan_2(n))
```

Dalam contoh ini, fungsi `penjumlahan_1` menghitung jumlah angka dari 1 hingga n dengan menggunakan perulangan. Ini adalah metode yang umum dan dikenal luas untuk menyelesaikan masalah ini.

Di sisi lain, fungsi `penjumlahan_2` menghitung jumlah angka dari 1 hingga n dengan menggunakan rumus Gauss, yaitu (n * (n + 1)) // 2. Pendekatan ini lebih efisien dalam hal kinerja dan merupakan contoh dari "oddball" atau solusi yang berbeda untuk masalah yang sama. 

Kedua fungsi ini memberikan hasil yang sama namun menggunakan pendekatan yang berbeda. "Oddball" solution sering kali merupakan pendekatan yang tak terduga tetapi efektif untuk menyelesaikan masalah.


* Girinti Kaybı

"Girinti hilang" tidak secara umum digunakan dalam konteks pemrograman. Namun, "girinti" dalam konteks pemrograman biasanya mengacu pada tata letak blok kode untuk meningkatkan kejelasan kode. Girinti biasanya digunakan untuk menunjukkan blok kode dalam bahasa pemrograman dan menandai awal dan akhir dari suatu blok.

Contoh kode Python di bawah ini adalah ilustrasi dari masalah "girinti hilang":

```python
def kontrol(a, b):
if a > 0:
print("a positif")
else:
print("a negatif")
if b > 0:
print("b positif")
else:
print("b negatif")
```

Dalam contoh di atas, terdapat dua pernyataan if-else di dalam fungsi. Namun, tata letak girintinya tidak konsisten. Kesalahan girinti terjadi ketika ada ketidaksesuaian tingkat girinti di antara awal dan akhir blok. Pada kode di atas, pernyataan "if a > 0:" dan blok yang mengikutinya tidak memiliki girinti yang tepat. Hal ini dapat menyebabkan Python menghasilkan kesalahan girinti saat menjalankan kode tersebut.

Untuk mengatasi kesalahan girinti, penting untuk memiliki girinti yang konsisten di antara blok-blok kode dalam Python. Dengan memperbaiki tata letak girinti, kode dapat dibaca dengan lebih mudah dan juga dapat dijalankan dengan benar.
