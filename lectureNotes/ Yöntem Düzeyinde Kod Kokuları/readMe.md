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

