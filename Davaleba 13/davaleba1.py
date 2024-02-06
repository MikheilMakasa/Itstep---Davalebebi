def create_file(text_file):
    with open(text_file, 'w') as file:
        for i in range(1, 1001):
            file.write(f"{i}. All work and no play makes Jack a dull boy.\n")

def read_file(text_file):
    xazebi = 0
    with open(text_file, 'r') as file:
        for line in file:
            if line.strip():  
                xazebi += 1

    print(f"შევსებულია {xazebi} ხაზი.")


test = "test1000.txt"

create_file(test)
read_file(test)
