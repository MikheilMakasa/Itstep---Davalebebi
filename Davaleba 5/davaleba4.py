a = [[10, 7, 3],[4, 8, 6],[16, 5, 21]]
b = [[12, 8, 7],[9, 14, 4],[3, 5, 1]]


if len(a) != len(b) or len(a[0]) != len(b[0]):
    print("მატრიცების განზომილებები უნდა იყოს ერთი და იგივე!")
else:
    jamuri_matrica = [
        [a[row][col] + b[row][col] for col in range(len(a[0]))]
        for row in range(len(a))
    ]

    print("მატრიცების ჯამია:")
    for row in jamuri_matrica:
        print(row)