f = open('pi.txt', 'r')
pi = ''.join(f.read()[2:].split('\n'))
str2find = input()
index = 0
co = 0
while (id := pi.find(str2find, index)) != -1:
    index = id + 1
    print(index - 1)
    co += 1
print(co)