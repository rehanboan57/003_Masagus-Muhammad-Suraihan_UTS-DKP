"""Program Monitoring Level Tangki - Kelompok C, Instrumentasi.

Aturan:
- level < 30%       -> LOW
- 30% <= level <=80% -> NORMAL
- level > 80%       -> HIGH
"""
from typing import Iterable

DATA_INTI = [18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15]
DATA_TAMBAHAN = [30, 80, 29.9, 80.1, 100]
DATA_LEVEL = DATA_INTI + DATA_TAMBAHAN

def validasi_level(level: float) -> None:
    """Pastikan pembacaan berupa angka dalam rentang fisik 0 sampai 100%."""
    if isinstance(level, bool) or not isinstance(level, (int, float)):
        raise TypeError("Level harus berupa angka (int/float).")
    if not 0 <= level <= 100:
        raise ValueError("Level harus berada pada rentang 0 sampai 100%.")

def status_level(level: float) -> str:
    """Mengembalikan status LOW, NORMAL, atau HIGH."""
    validasi_level(level)
    if level < 30:
        return "LOW"
    elif level <= 80:
        return "NORMAL"
    return "HIGH"

def hitung_kategori(data: Iterable[float]) -> dict:
    """Menghitung jumlah pembacaan pada setiap kategori."""
    hasil = {"LOW": 0, "NORMAL": 0, "HIGH": 0}
    for level in data:
        hasil[status_level(level)] += 1
    return hasil

def rata_rata(data: Iterable[float]) -> float:
    """Menghitung rata-rata; menghasilkan 0.0 jika data kosong."""
    nilai = list(data)
    if not nilai:
        return 0.0
    for level in nilai:
        validasi_level(level)
    return sum(nilai) / len(nilai)

def ringkasan(data: Iterable[float]) -> dict:
    """Menghasilkan statistik jumlah, kategori, rata-rata, minimum, maksimum."""
    nilai = list(data)
    if not nilai:
        return {"total": 0, "kategori": {"LOW": 0, "NORMAL": 0, "HIGH": 0},
                "rata_rata": 0.0, "minimum": None, "maksimum": None}
    return {"total": len(nilai), "kategori": hitung_kategori(nilai),
            "rata_rata": rata_rata(nilai), "minimum": min(nilai),
            "maksimum": max(nilai)}

def main() -> None:
    """Menjalankan validasi, menampilkan tabel, dan ringkasan monitoring."""
    assert len(DATA_INTI) == 15, "Data inti harus tepat 15 nilai."
    assert len(DATA_TAMBAHAN) == 5, "Data tambahan harus tepat 5 nilai."
    assert len(DATA_LEVEL) == 20, "Total data harus tepat 20 nilai."

    print("=" * 48)
    print("          MONITORING LEVEL TANGKI")
    print("=" * 48)
    print(f"{'No':<4}{'Level (%)':<13}{'Status':<10}Keterangan")
    print("-" * 48)
    for nomor, level in enumerate(DATA_LEVEL, start=1):
        status = status_level(level)
        keterangan = "inti" if nomor <= len(DATA_INTI) else "tambahan"
        print(f"{nomor:<4}{level:<13g}{status:<10}{keterangan}")

    semua = ringkasan(DATA_LEVEL)
    inti = ringkasan(DATA_INTI)
    print("-" * 48)
    print("Ringkasan seluruh data:")
    print(f"  Jumlah kategori : {semua['kategori']}")
    print(f"  Total data      : {semua['total']}")
    print(f"  Rata-rata       : {semua['rata_rata']:.2f}%")
    print(f"  Minimum         : {semua['minimum']}%")
    print(f"  Maksimum        : {semua['maksimum']}%")
    print("Ringkasan 15 data inti:")
    print(f"  Jumlah kategori : {inti['kategori']}")
    print(f"  Rata-rata       : {inti['rata_rata']:.2f}%")
    print(f"  Minimum         : {inti['minimum']}%")
    print(f"  Maksimum        : {inti['maksimum']}%")

if __name__ == "__main__":
    main()
