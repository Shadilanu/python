#1.Create a list[1,2,3] and add 4 to the end using a list method.
a=[1,2,3]
a.append(4)
print(a)

#2. Given [10,20,30] , remove 20 using a list method.
a=[10,20,30]
a.remove(20)
print(a)

#3. From [5,3,9,1] , sort the list in ascending order using a list method.
a=[5,3,9,1]
a.sort()
print(a)

# #4.From [1,2,3,4,5] , extract [2,3,4] using slicing only.
a=[1,2,3,4,5]
b=a[1:4]
print(b)


# 5. Reverse the list [1,2,3,4] using slicing (no loops).
a=[1,2,3,4]
b=a[::-1]
print(b)

# 6. Combine [1,2] and [3,4] into one list using list operations.
a=[1,2]+[3,4]
print(a)


# 7. Convert [7,8] into [7,8,7,8] using list operations.
a=[7,8]*2
print(a)

# 8. Check if 3 exists in [1,2,3,4] using a list operator.
a= [1,2,3,4]
print(3 in a)

# 9. Count how many times 2 appears in [1,2,2,3,2] using a list method.
a = [1, 2, 2, 3, 2]
print(a.count(2))

# 10. Remove the last element from ["a","b","c","d"] using a list method.
a=["a","b","c","d"]
print(a.pop())
# 11. Insert "x" at index 1 in ["a","b","c"] using a list method.
a=["a","b","c"]
print(a.insert(1,"x"))


# 12. Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
a=[10,20,30,40,50,60]
a[2]=99
print(a)
# 13. Convert range(5) into a list using list functions.
a=list(range(5))
print(a)
# 14. Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6] .
a=[1,2,3,4,5,6]
b=a[1:2]
print(b)
# 15. Remove all elements from [1,2,3] using one list method.
a=[1,2,3]
a.clear()
print(a)
# 16. Copy a list [4,5,6] using only list tools (no modules).
a=[4,5,6]
b=a.copy()
print(a)
# 17. Convert [1,2,3] into a nested list [[1,2,3]] using list operations.
a=[1,2,3]
b=[a]
print(b)

# 18. Extend [1,2] with [3,4,5] using a list method.
a=[1,2]
b=a.extend([3,4,5])
print(a)

# 19. Using list repetition, create a list ["hello","hello","hello"] .
a=["hello"]*3
print(a)


# 20. Remove the element at index 2 from [10,20,30,40] using a list method
a=[10,20,30,40]
a.pop()
print(a)