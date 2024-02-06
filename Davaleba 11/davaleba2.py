def combine_intersect_tuples(tuple1, tuple2):
    combined_tuple = tuple(set(tuple1) | set(tuple2))
    duplicated_values = list(set(tuple1) & set(tuple2))
    
    print(f"tuple-ების გაერთიანება: {combined_tuple}")
    print(f"tuple-ების დუბლიკატები: {duplicated_values}")


tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combine_intersect_tuples(tuple1, tuple2)
