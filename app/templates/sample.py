#Find All Overlapping Intervals

arr1 = [[1,3], [2,4], [5,7], [11,12], [6,8], [14,19], [23,24], [18,22], [21,28]]
arr1 = sorted(arr1)
print(arr1)
ans = []
for i in range(len(arr1)-1):
    first_first = arr1[i][0]
    first_second =arr1[i][1]
    second_first = arr1[i+1][0]
    second_second = arr1[i+1][1]
    first_second_dec = first_second-1
    print(first_second,second_first,first_second_dec)
    if first_second > second_first and first_second_dec == second_first:
        ans.append([first_first,second_second])

print(ans)
