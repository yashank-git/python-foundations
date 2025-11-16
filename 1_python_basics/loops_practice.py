for i in range(1, 11):
    print(i)
for i in range(2, 21, 2):
    print(i)
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)
for i in range(10, 0, -1):
    print(i)
for _ in range(5):
    print("Krish")
count = 5
while count > 0:
    print(count)
    count -= 1
for i in range(1, 11):
    if i == 7:
        print("Found 7! Breaking...")
        break
    print(i)
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i},{j}", end=" ")
    print()
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"5! = {fact}")
