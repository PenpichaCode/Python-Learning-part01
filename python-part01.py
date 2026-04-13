# Introduction to python programming
# Variable
# Data type
# Data type
# Data Structores
# Control Flow
# Function

# 🥑 Variable
print(1 + 1)
print(2 * 2)
print(100/5)
print(100/3)
print(100//3) #flor division คือการหารปัดเศษไปเลย
print(100%3) #modulo แสดงค่าเศษ
print(5**2)

# 🥑 Data type
x = 100
y = 2000
print(x + y)

## expens
income = 50000
expense = 36000
saving = income - expense
print(saving)

## remove variable
del saving

# 🥑 Data type
# int
# float
# string
# bool

name = "am ruby am"
text = "im love beers"
age = 27

print(name, text)
print(name + text)
print(name, "i'm " ,age , "years old")
print(f"Hello ! {name}")

## check data type with type()
## dynamic type
print(type(age))
print(type(name))

# type hint
name : str = "am"
age : int = 28
score : float = True

# convert data type
str(100)
int(True)

# str() int() float() bool() ใช้ได้ตรงๆตัวเลข
bool(1) # true = 1, fals = 0

# f - string template
name = "penpicha"
age = 28
lang = "R"

print(f"Hello my name is {name}. i'm {age} years old. My faverite lang is {lang}")

# 🥑 Data Structures
# List
# Tupel
# Dictionary
# Set

# List
Shoping = ["egg", "milk", "bread", "banana", "rice"]

# check lenght of list
len(Shoping)

# index start with 0
Shoping[0]

# slicing item in the list
Shoping[0:2]

# slice from banana to rice (end)
Shoping[3:]

# list can contain multiple data types
# ทำได้ แต่ไม่ควรทำ
am = ["am", 27, "Bangkok", True]

# nasted list
# A simple 2D list (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# query number 6
matrix[1][2]

# query number 8
matrix[2][1]

# function vs Method.
# method คือ function ที่เกิดมาเพือ list เท่านั้น

len(Shoping)

# object ตามด้วย .(dot)
# Add carot to the end.
Shoping.append("carot")
print(Shoping)

# delete item from end.
Shoping.pop()

# insert item at the index we want.
# add carot to index 1 (ต่อจาก egg)
Shoping.insert(1, "carot")

# remove carot?
Shoping.remove("carot")

# ⌛ Mutable vs Immutable
# Mutable = Can Change/ Tranform e.g. list dict
# Immutable = Con not Change / Tranform e.g. str tuple

# Function vs Method.
# function คือคำสั่งที่เกิดมาเพื่อทำงานทั่วๆไป เช่น print() len() int() str() float()
# method คือคำสั่งที่เกิดมาเพือ list เท่านั้น เช่น append() pop()

## string method. (immutable)
text = "a duck walk to the bar"
text.upper()
text = text.lower()

## list method (mutable)
friends = ["am", "ping", "tan"]
friends.append("lisa")

## new varible change `str` on word
# we can not change or tranform str but we can create new variable to store the new value.
lang = "python"

# must to create new varible (c can not replace p directoryd)
new_lang = 'C' + lang[1:]
print(new_lang)

# mutable example
# update shoping
Shoping.append("orange")

## change item
Shoping[0] = "duck egg"
Shoping[1] = "oat milk"
Shoping[2] = "black tea"

print(Shoping)

## string method
text = "a duck walk to the bar"
# change duck to chicken
text = text.replace("duck", "chicken")
print(text)

# count text
text.count("chicken")

# strip text
text_str = "..................hello.."
text_str = text_str.strip(".") # # Reassign the new version to the variable

print(text_str)

# split word on sentens with whithe space.
# split text into list.
text_spl = "i love to eat pizza."
text_spl = text_spl.split(" ")

# back to text

print("-".join(text_spl))
print(" ".join(text_spl))

# ⛳ tuple is immutable
# ประกาศแล้วจะไม่สามารถอัปเดตค่าข้างในได้ แต่สามารถดึงข้อมูลได้เหมือน list เลย

# Packing
person = ("Data Analyst", 200000, "MacBook")

# Unpacking
role, salary, tool = person

print(role)   # Output: Data Analyst
print(salary) # Output: 200000

# ⚽ Dictionary is Mutable
# ประกาศด้วย {} และมี key กับ value
# key ต้องไม่ซ้ำกัน และไม่สามารถเปลี่ยนแปลงได้ เช่น str int float bool tuple
# value สามารถเป็นอะไรก็ได้ และสามารถเปลี่ยนแปลงได้
# query value ด้วย key
# เพิ่ม ลบ แก้ไข key กับ value ได้

# dictionary_name = { key: value }
user_profile = {
    "role": "Data Analyst",
    "salary_goal": 200000,
    "device": "MacBook",
    "skills": ["Python", "SQL", "AI"]
}

## add location.
user_profile["location"] = "Bangkok"
user_profile

# remove key and value.
del user_profile["location"]
user_profile

# check if key exists
# return true
"role" in user_profile

## dictionary method.
# keys,item, values
user_profile.keys()
user_profile.values()
user_profile.items()

user = list(user_profile.keys())
type(user)

# convert data structures
# list(), tuble(), dict(), set()

list_a = [100, 200, 300]
tuple_a = tuple(list_a)
print(tuple_a)

# update value on dictionary
user_profile['skills'][2] = "AI engineering"
user_profile

# ⛵ Set is Mutable
# unique value in a set.
# unordered, unchangeable, and unindexed.
colors = ["Red", "Blue", "Red", "Green", "Red", "Blue"]

# convert to set
# they will delete duplicate
colors = set(colors)

type(colors)

# add item to set
colors.add("salmon")
colors.add("yellow")

# remove
colors.remove("salmon")

# can create set like this also
colors_set = {"Red", "Blue", "Red", "Green", "Red", "Blue"}
type(colors_set)

# Check existence (return True)
"Red" in colors_set

# Unions and Intersections.

skills_a = {"Python", "SQL", "Excel"}
skills_b = {"Python", "Tableau", "AI"}

# 1. Intersection (What do both have?)
print(skills_a & skills_b)
# Output: {'Python'}

# 2. Union (Combine both, no duplicates)
print(skills_a | skills_b)
# Output: {'Python', 'SQL', 'Excel', 'Tableau', 'AI'}

# 3. Difference (What is in A but NOT in B?)
print(skills_a - skills_b)
# Output: {'SQL', 'Excel'}

# 😀 Control Flow
# If
# For
# While

# Conditional Statements (If-Else)
score = 56

if score >= 80:
    print("pass")
else:
    print("fail")

## Mutiple Grade
user_custumer = 100

if user_custumer >= 10000:
    print("good")
elif user_custumer >= 8000:
    print("normal")
elif user_custumer >= 5000:
    print("bad")
else:
    print("so bad")

## Custumer purchase amount
# 1. Get the purchase amount
total_spent = 2990.50
# 2. Logic: High spenders get bigger discounts
if total_spent >= 1000:
    discount = 0.20  # 20% discount
    status = "Platinum"
elif total_spent >= 500:
    discount = 0.10  # 10% discount
    status = "Gold"
else:
    discount = 0.0   # No discount
    status = "Standard"

# 3. Calculation
final_price = total_spent * (1 - discount)

# 4. Results
print(f"Customer Status: {status}")
print(f"Discount applied: {discount * 100}%")
print(f"Final Price to pay: {final_price}")

# 1. Get the input and convert to float
try:
    score = 80

    # 2. Multiple Grade Logic
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # 3. Output the result
    print(f"The grade is: {grade}")

except ValueError:
    print("Error: Please enter a valid number, not text.")


# multiple condition 
has_id = True
age_over_18 = False
vip_custumer = False

if has_id and (age_over_18 or vip_custumer):
    print("Welcome to the club")
else:
    print("please come to next time.")

# 🏔 For
# Loop through a list of numbers and print each number
animals = ["Lion", "Tiger", "Elephant", "Giraffe"]
for animal in animals:
    if animal == "Lion":
        print("animal on Amazon!")
    else:
        print(animal)

# loop เข้าไปทุกตัว
for animal in animals:
    print(f"Current animal: {animal}")

# enumerate() 
# การวิ่งเข้าไปนับ index (กำหนด index start with 1)
for index, animal in enumerate(animals, start=1):
    print(f"Animal number {index} is {animal}")

zoo_data = {
    "Lion": "Carnivore",
    "Elephant": "Herbivore",
    "Zebra": "Herbivore"
}

for name, food_type in zoo_data.items():
    print(f"The {name} is a {food_type}.")

# List Comprehension
result = []
for animal in animals:
    result.append(animal.upper())

print(result)

# Pro way
# [ผลลัพธ์ที่ต้องการ  for  ตัวแปร  in  กลุ่มข้อมูล ]
[animal.upper() for animal in animals]


animals = ["Lion", "Tiger", "Cat", "Dog", "Panda"]
# เลือกเฉพาะสัตว์ที่มีตัว 'a' ตัวเล็ก
a_animals = [animal for animal in animals if "a" in animal.lower()]

print(a_animals)


numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number**2)

print(squares)

nums = [1, 2, 3, 4, 5]
squares = [num**2 for num in nums]

# for & if else condition.
scores = [90, 45, 88, 70]
results = ["Pass" if s >= 80 else "Fail" for s in scores]

print(results)


# While loop
# นับจาก 0 ถึง 4 และพิมพ์ "hi!" ทุกครั้งที่นับ
count = 0
while count < 5:
    print("hi!")
    count += 1

# ข้อมูลจำลอง (Mock Data) เป็นรหัส ID ของสัตว์ในฐานข้อมูล
data_queue = ["ID_01", "ID_02", "ID_03", "ID_04", "ID_05", "ID_06"]
processed_count = 0

print(f"เริ่มประมวลผล... จำนวนข้อมูลตั้งต้น: {len(data_queue)} รายการ")

# วนลูปตราบใดที่ข้อมูลใน List ยังมากกว่า 2 รายการ
while len(data_queue) > 2:
    # ดึงข้อมูลตัวสุดท้ายออก (pop)
    item = data_queue.pop()
    processed_count += 1
    print(f"กำลังประมวลผล {item}... (เหลือในคิว: {len(data_queue)})")

print("--- จบการทำงาน ---")
print(f"สรุป: ประมวลผลไปทั้งหมด {processed_count} รายการ")
print(f"ข้อมูลที่เหลือในคิวสำรอง: {data_queue}")

current_savings = 50000  # เงินต้น
target = 100000         # เป้าหมาย
interest_rate = 0.07    # ดอกเบี้ย 7% ต่อปี
year = 0 # ทุก loop: years += 1 เสมอ

while current_savings < target:
    year += 1
    current_savings += current_savings * interest_rate
    print(f"ปีที่ {year}: เงินสะสมคือ {current_savings:.2f} บาท")

print(f"\nสรุป: ต้องใช้เวลา {year} ปี ถึงจะมีเงินเกิน {target} บาท")

# ระบบเติมอาหารสัตว์อัตโนมัติ
water_level = 100

while True:
    print(f"กำลังจ่ายน้ำ -> ระดับน้ำคงเหลือ: {water_level}%")
    water_level -= 10  # ลดลงทีละ 10%
    
    if water_level <= 0:
        print("น้ำหมดถัง! หยุดการทำงาน")
        break  # ออกจากลูปทันที

# Function
# ฟังก์ชันคือกลุ่มของคำสั่งที่ทำงานร่วมกันเพื่อทำงานเฉพาะอย่าง
# ช่วยให้โค้ดของเราสะอาดและนำกลับมาใช้ใหม่ได้
# ประกาศด้วย def ชื่อฟังก์ชัน(พารามิเตอร์):
#     คำสั่งต่างๆ
#     return ค่าที่ต้องการส่งกลับ (ถ้ามี)

def say_hello(name):
    """
    say hello to my friend
    """
    print(f" hello {name}! welcome to ruby duckie")

say_hello("am")

## function cube
def cub(base, power):
    return base**power
result = cub(3, 3)
print(result)

## function can return multiple value
# using tuble unpaking
def random_fun(base):
    return base**2, base**3, base**4
square, cube, power4 = random_fun(2)
print(f"Square: {square}, Cube: {cube}, Power4: {power4}")

x, y, z = random_fun(5)
print(x, y, z, x+y, x+y+z)
