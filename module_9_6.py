def all_variants(text):
    for index_text in range(len(text)):             # index_text = 0, 1, 2
        for ind in range(len(text) - index_text):   # ind = 0, 1, 2(index_text=0, range=3); ind = 0, 1(index_text=1, range=2); ind = 0(index_text=2, range=1)
            yield text[ind:ind + 1 + index_text]    # (index_text=0)- [0:1], [1:2], [2:3]; (index_text=1)- [0:2], [1:3]; (index_text=2)- [0:3]


# Проверка кода:
a = all_variants('abc')

for i in a:
    print(i)
