def create_file(filename):
    with open(filename, 'w') as file:
        lines = [
            "",  # 1
            "2 - second",
            "",  # 3
            "",  # 4
            "",  # 5
            "",  # 6
            "",  # 7
            "8 - eighth",
            "",  # 9
            "10 -tenth",
            "",  # 11
            "",  # 12
            "13 - thirteenth",
            "",  # 14
            "",  # 15
            "",  # 16
            "17 - seventeenth",
        ]
        file.write('\n'.join(lines))


test = "test17.txt"

create_file(test)
