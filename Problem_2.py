dic = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
s = input()
print(sum(dic.get(c.lower(), 0) * (2 if c.isupper() else 1) for c in s if c.lower() in dic))
