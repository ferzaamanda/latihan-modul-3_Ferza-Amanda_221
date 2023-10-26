data_list = [3.1, 5.5, 2.7, 'hello', 105, 'Python', 737, 'world', 412, 'AI']

# Filter untuk memisahkan nilai float, int, dan string
float_data = list(filter(lambda x: isinstance(x, float), data_list)) # digunakan untuk memeriksa tipe data dari setiap elemen dalam list
int_data = list(filter(lambda x: isinstance(x, int), data_list))
str_data = list(filter(lambda x: isinstance(x, str), data_list))

# Map untuk mengubah nilai int menjadi satuan, puluhan, dan ratusan
def mapping(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}
#membuat koleksi baru dengan cara mengaplikasikan sebuah fungsi pada setiap elemen yang ada pada iterable object
int_mapped = list(map(mapping, int_data))

# Output
print("Data Float:", float_data)
print("Data Int:")
for item in int_mapped:
    print(item)
print("Data String:", str_data)