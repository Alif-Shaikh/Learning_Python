#tuples are immutable and used to store as seq of objs
numbers=(1,2,3,3,3,3)
#numbers[0]=10 #TypeError: 'tuple' object does not support item assignment

print(numbers.count(3))
print(numbers.index(3))