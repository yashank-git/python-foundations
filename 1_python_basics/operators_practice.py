a, b = 10, 3
print("Add:", a + b)
print("Floor Div:", a // b)
print("Mod:", a % b)
print("Power:", a ** b)
print("a > b:", a > b)
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
score = 85
score += 15
print("New score:", score)
num = 24
print("Even?" if num % 2 == 0 else "Odd")
marks = 92
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")
weight = 70
height = 1.75
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")
p, q = 5, 10
p, q = q, p
print("After swap:", p, q)
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Leap Year?" if is_leap else "Not Leap")
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print("Simple Interest:", si)
