# list=[1,2 ,2,2 ,2,2,2,2,2,2,2,2,2,2,2,2,2,2 ]
# print(list,end=" ")



a = [1, 2, 2, 3, 4]

# MEAN
sum = 0
for x in a:
    sum = sum + x
mean = sum / len(a)

# MEDIAN
a.sort()
n = len(a)

if n % 2 != 0:
    median = a[n // 2]
else:
    median = (a[n // 2 - 1] + a[n // 2]) / 2

# MODE
mode = a[0]
max_count = 0

for i in a:
    count = 0
    for j in a:
        if i == j:
            count = count + 1
    if count > max_count:
        max_count = count
        mode = i

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
