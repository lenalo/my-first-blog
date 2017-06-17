# a = 1+2
# print(a)
# l = [a,4,5,6,"letters"]
# a = 1
# print(l)
# l1 = [1,2]
# comp = len(l) > len(l1)
# print(comp)
# if len(l) == (len(l1) / 2):
#     print("true")
# else:
#     a = 2
# print(a)

def incr(a):
    a = a + 1
    return a

b = 5

b = incr(b)

print(b)

a = 1+2

l = [a,4,1,2,"letters"]

for items in range(len(l)-1):
    print("items:",items)
    print("listitems:",l[items])
    if type(l[items]) == int:
        l[items] = incr(l[items])

print(l)
