def MaxBilangan(a, b, c, d):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    if d > m:
        m = d
    return m

if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    hasil = MaxBilangan(a, b, c, d)
    print(hasil)
