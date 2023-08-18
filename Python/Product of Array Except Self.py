nums = []

n = int(input("Enter the number of elements: "))
for i in n:
    nums[i] = int(input("Enter: "))

answer = [1] * n
left_product=1
for i in range(n):
    answer[i] = left_product
    left_product *= nums[i]

right_product = 1
for i in range(n-1,-1,-1):
    answer[i] = right_product
    right_product *= nums[i]