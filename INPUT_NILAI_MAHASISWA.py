print("===PROGRAM INPUT NILAI MAHASISWA===") 
print("KELOMPOK 19 - SHIFT 3") 
print("Anggota:") 
print("1. BarBar") 
print("2. Bobi") 
print("3. DAFFA") 
print("4. FFAZ")
nama = ["Akbar Maulana", "Muhammad Habib", "Dafiq Mafaaza Mukti", "Fadhil Dzaki Faiz"] 
nim = ["21120125130076", "21120125130077", "21120125130078", "21120125130079"] 

nilai = []
print("=== INPUT NILAI MAHASISWA ===")
nilai1 = float(input(f"Masukkan nilai untuk {nama[0]} ({nim[0]}): "))
nilai.append(nilai1) 

nilai2 = float(input(f"Masukkan nilai untuk {nama[1]} ({nim[1]}): ")) 
nilai.append(nilai2) 

nilai3 = float(input(f"Masukkan nilai untuk {nama[2]} ({nim[2]}): ")) 
nilai.append(nilai3) 

nilai4 = float(input(f"Masukkan nilai untuk {nama[3]} ({nim[3]}): ")) 
nilai.append(nilai4) 
print("\n=== HASIL PERHITUNGAN ===") 
rata_rata = sum(nilai) / len(nilai) 
print(f"Rata-rata nilai: {rata_rata:.2f}") 



nilai_terurut = sorted(nilai) 
median = (nilai_terurut[1] + nilai_terurut[2]) / 2 
print(f"Median nilai: {median:.2f}") 

nilai_tertinggi = max(nilai) 
nilai_terendah = min(nilai) 

indeks_tertinggi = nilai.index(nilai_tertinggi)
mhs_tertinggi = nama[indeks_tertinggi]
nim_tertinggi = nim[indeks_tertinggi]
indeks_terendah = nilai.index(nilai_terendah)

mhs_terendah = nama[indeks_terendah]
nim_terendah = nim[indeks_terendah]

print(f"Nilai tertinggi: {nilai_tertinggi} - {mhs_tertinggi} ({nim_tertinggi})")
print(f"Nilai terendah: {nilai_terendah} - {mhs_terendah} ({nim_terendah})")
print("\n=== DAFTAR NILAI MAHASISWA ===")
print(f"{nama[0]} ({nim[0]}): {nilai[0]}")
print(f"{nama[1]} ({nim[1]}): {nilai[1]}")
print(f"{nama[2]} ({nim[2]}): {nilai[2]}")
print(f"{nama[3]} ({nim[3]}): {nilai[3]}")
print("\n=== PROGRAM SELESAI ===")
print("Terima kasih telah menggunakan program ini!")