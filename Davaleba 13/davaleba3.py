def combine_files(file1, file2, combined_file):
    with open(file1, 'r') as file1_text, open(file2, 'r') as file2_text:
        combined_text = file1_text.read() + '\n' + file2_text.read()

    with open(combined_file, 'w') as file:
        file.write(combined_text)

    print(f"გაერთიანებული ფაილი ჩაწერილია {combined_file}-ზე. გაერთიანებული ტექსტია: \n{combined_text}")

# პროგრამის მარტივად გასატესტად file1.txt და file2.txt უკვე შექმნილია საქაღალდეში
file1 = "file1.txt"
file2 = "file2.txt"
file3 = "file3.txt"

combine_files(file1, file2, file3)
