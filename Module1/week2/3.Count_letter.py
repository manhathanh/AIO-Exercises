def count_word(name):
    word = name.lower().split()
    letter = []
    letter_count = []
    for i in word:
        if i not in letter:
            letter.append(i)
            check = word.count(i)
            letter_count.append(check)
    final = {}
    print(type(final))
    for v1, v2 in zip(letter, letter_count):
        count_chart = {v1: v2}
        final.update(count_chart)
    return final


fill_path = "D://AIO//AIO_BaiTap//AIO-Exercises//Module1//week2//P1_data.txt"


def read_data(fill_path):
    with open(fill_path, "r") as file:
        data = file.read()
        file.close()
    return data


name = read_data(fill_path)
a = count_word(name)

assert a['who']==3
print(a['man'])
