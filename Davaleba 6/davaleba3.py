def fibonachi(n):
    fibonachis_mimdevroba = [0, 1]

    while len(fibonachis_mimdevroba) < n:
        momdevno_ricxvi = fibonachis_mimdevroba[-1] + fibonachis_mimdevroba[-2]
        fibonachis_mimdevroba.append(momdevno_ricxvi)

    return fibonachis_mimdevroba[:n]

n = 12
mimdevroba = fibonachi(n)
print(f"ფიბონაჩის მიმდევრობა იქნება: {mimdevroba}")
