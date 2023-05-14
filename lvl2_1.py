def minimum(arr):
    minnum = arr[0]
    for num in arr:
        if num < minnum:
            minnum = num
    return minnum



def maximum(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
        
print(minimum([4,6,2,1,9,63,-134,566])) # -134
print(maximum([4,6,2,1,9,63,-134,566])) # 566

print(minimum([-52, 56, 30, 29, -54, 0, -110])) # -110
print(maximum([-52, 56, 30, 29, -54, 0, -110])) # 56

print(minimum([42, 54, 65, 87, 0])) # 0
print(maximum([42, 54, 65, 87, 0])) # 87

print(minimum([5])) # 5
print(maximum([5])) # 5
