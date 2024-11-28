def all_variants(text):
    for step in range(1, len(text) + 1):
        for index in range(0, len(text)):
            if index + step <= len(text):
                yield text[index:index + step]


a = all_variants("abc")
for i in a:
    print(i)
