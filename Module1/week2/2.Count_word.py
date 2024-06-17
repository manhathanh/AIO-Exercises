def count_word(name):
    letter = []
    letter_count = []
    for i in name:
        if i not in letter:
            letter.append(i)
            check = name.count(i)
            letter_count.append(check)
    final = {}
    
    for v1, v2 in zip(letter, letter_count):
        count_chart = {v1: v2}
        final.update(count_chart)
    return final
assert count_word("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
result = count_word("smiles")
print(result)