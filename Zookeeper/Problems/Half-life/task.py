days = 0
start_atom = int(input())
finish_atom = int(input())
if finish_atom > start_atom:
    print(days)

while start_atom > finish_atom:
    start_atom /= 2
    days += 12
print(days)