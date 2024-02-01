#range function is used to generate sequence of numbers
numbers=range(5)   #this will return range object which stores seq of num
print(numbers)   #o/p range(0, 5)
for number in numbers:
    print(number)  #0 1 2 3 4

for n in range(3):
    print(n)  # 0 1 2

num=range(5,10)
for i in num:
    print(i)     # 5 6 7 8 9


for i in range(5,10,2):
    print(i)     # 5 7 9