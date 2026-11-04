# KELOMPOK C - INSTRUMENTASI
# MONITORING LEVEL TANGKI

data_level = [
    18, 25, 33, 41, 55,
    62, 76, 84, 91, 47,
    29, 38, 70, 82, 15,
    30, 80, 81, 10, 50
]

# Function menentukan status level
def status_level(level):
    if level < 30:
        return "LOW"
    elif level <= 80:
        return "NORMAL"
    else:
        return "HIGH"


# Function menghitung kategori
def hitung_kategori(data):
    low = 0
    normal = 0
    high = 0

    for level in data:
        if status_level(level) == "LOW":
            low += 1
        elif status_level(level) == "NORMAL":
            normal += 1
        else:
            high += 1

    return low, normal, high


# Function menghitung rata-rata
def rata_rata(data):
    return sum(data) / len(data)


# PROGRAM UTAMA
print("=" * 40)
print("       MONITORING LEVEL TANGKI")
print("            KELOMPOK C")
print("=" * 40)

print("\nDATA PENGUKURAN TANGKI")

for nomor, level in enumerate(data_level, 1):
    print(f"{nomor}. Level: {level}% | Status: {status_level(level)}")

low, normal, high = hitung_kategori(data_level)

print("\n" + "=" * 40)
print("             HASIL MONITORING")
print("=" * 40)

print("Total Data     :", len(data_level))
print("Status LOW     :", low, "data")
print("Status NORMAL  :", normal, "data")
print("Status HIGH    :", high, "data")
print("Rata-rata Level: {:.2f}%".format(rata_rata(data_level)))

print("=" * 40)
print("       MONITORING SELESAI")
print("=" * 40)