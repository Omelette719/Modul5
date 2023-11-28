def maksimal(a, b):
    return max(a, b)

def minimal(a, b):
    return min(a, b)

bilangan = int(input())
nilai = list(map(int, input().split()))

maks = float('-inf')
minim = float('inf')

for nilai_saat_ini in nilai:
    maks = maksimal(maks, nilai_saat_ini)
    minim = minimal(minim, nilai_saat_ini)

print(f"{maks} {minim}")
