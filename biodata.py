# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "nuri": {
        "nim": "SI19220014",
        "alamat": "lingkok bunut",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.9,
        "nilai_matakuliah": {
            "Pemrograman Dasar": 80,
            "Kalkulus": 85,
            "Fisika Dasar": 75
        }
    },
    "Reza Hardian": {
        "nim": "SI19220013",
        "alamat": "Braim",
        "prodi": "Sistem Informasi",
        "semester": 3,
        "ipk": 2.8,
        "nilai_matakuliah": {
            "Pemrograman Lanjut": 90,
            "Algoritma dan Struktur Data": 87,
            "Basis Data": 92
        }
    },
    "selpi": {
        "nim": "SI19220026",
        "alamat": "bogak",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.6,
        "nilai_matakuliah": {
            "Jaringan Komputer": 85,
            "Sistem Digital": 80,
            "Manajemen Basis Data": 90
        }
    },
    "ardian": {
        "nim": "SI19220021",
        "alamat": "Pegading",
        "prodi": "Teknik Informatika",
        "semester": 5,
        "ipk": 2.7,
        "nilai_matakuliah": {
            "Kimia Fisika": 88,
            "Rekayasa Proses Kimia": 85,
            "Termokimia": 92
        }
    },
    "ari": {
        "nim": "TI19220000",
        "alamat": "aik berik",
        "prodi": "Teknik Informatika",
        "semester": 4,
        "ipk": 2.9,
        "nilai_matakuliah": {
            "Jaringan Komputer": 95,
            "Aljabar Linier": 92,
            "Konstruksi Beton": 93
        }
    }
}

# Menampilkan biodata mahasiswa dan nilai akumulasi tiga matakuliah
for nama, data in mahasiswa.items()
    print("Biodata Mahasiswa")
    print("Nama          :", nama)
    print("NIM           :", data["nim"])
    print("Alamat        :", data["alamat"])
    print("Program Studi :", data["prodi"])
    print("Semester      :", data["semester"])
    print("IPK           :", data["ipk"])
    print("Nilai Akumulasi Matakuliah:")
    total_nilai = 0
    for matakuliah, nilai in data["nilai_matakuliah"].items():
        print("-", matakuliah, ":", nilai)
        total_nilai += nilai
    print("Total Nilai:", total_nilai)
    print("")
