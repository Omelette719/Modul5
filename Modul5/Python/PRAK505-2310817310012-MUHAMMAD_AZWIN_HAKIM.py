def biodata(tahun_lahir, namaku, asal):
    tahun_sekarang = 2023
    umur = tahun_sekarang - tahun_lahir

    print("\nPerkenalkan Nama Saya :", namaku)
    print("Umur Saya :", umur)
    print("Saya Adalah Angkatan :", tahun_sekarang)
    print("Asal Saya dari :", asal)

if __name__ == "__main__":
    tahun_lahir = int(input())
    namaku = input()
    asal = input()
    biodata(tahun_lahir, namaku, asal)
