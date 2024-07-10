def merge(num1, num2, m, n):
    temp = []
    for i in num1:
         if i != 0:
             temp.append(i)
    for i in num2:
         if i != 0:
             temp.append(i)
             temp.sort()

    return temp 

# def merge(nums1, m, nums2, n):
#     for j in range(n):
#         nums1[m+j] = nums2[j]
#     nums1.sort()
#     return nums1
               

num1 = [1,2,3,0,0,0]
m = 3

num2 = [2, 5, 6]
n = 3

output = merge(num1, num2, m, n)
print(output)