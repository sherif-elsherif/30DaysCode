# Day 8 Dictionaries and Maps
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


# Reading dictionary input from console
names = {}
n = int(input())
for i in range(n):
    entry = input().split(' ')
    names[entry[0]] = entry[1]

# Reading search key words
searches = []
entry = input()
while entry is not None:
    searches.append(entry)
    try:
        entry = input()
    except EOFError:
        break

# now doing the search in dict
for item in searches:
    if item in names:
        print(item, "=", names[item], sep = '')
    else:
        print('Not found')
        