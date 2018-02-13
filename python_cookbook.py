"""
Un-packing the elements from the sequence. discarding the special value from the sequence.
"""

p = (1, 2, 3, 4)
v, x, y, z = p
print(p)
print(v, x, y, z)


l = ['f', 'e', 'l', 'i', 'x']
s, t, r, i, n = l
print(l)
print(s, t, r, i, n)


pack = [1, 2, 3, 4, ("text", "text_1")]
a, _, c, _, d = pack
print(pack)
print(a, c, d)


discard = (1, 2, 3, 4, 5, 6)
_, a, b, c, _, _ = discard
print(discard)
print(a, b, c)


"""
unpacking the vlaue using *

"""

user_detail = ["felix", "stephen", "felsen", 987654321, 987654321, 8765432239]
username, username1, username2, *phone_number = user_detail
print(user_detail)
print(username, username1, username2, phone_number)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, home_dir, sh = line.split(":")
print(line)
print(uname, home_dir, sh)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(record)
print(name, year)


item = [1, 11, 23, 34, 45, 2, 3, 4, 5]
head, *_, tail = item
print(item)
print(head, tail)



