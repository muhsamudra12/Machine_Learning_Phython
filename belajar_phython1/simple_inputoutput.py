# Masukkan nilai a dalam float
a = float(input("Masukkan nilai a: "))
# Masukkan nilai b dalam float
b = float(input("Masukkan nilai b: "))


# Hitung hasil penambahan
tambah = a + b
# Hitung hasil pengurangan
kurang = a - b
# Hitung hasil perkalian
kali = a * b
# Hitung hasil pembagian
bagi = a / b if b != 0 else "Tidak dapat dibagi oleh nol"

# Cetak hasil
print(f"Penambahan: {tambah}")
print(f"Pengurangan: {kurang}")
print(f"Perkalian: {kali}")
print(f"Pembagian: {bagi}")

print("\nYeahhhh")