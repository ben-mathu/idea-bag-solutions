from datetime import datetime


n = input()
d = len(n)
k = int(input())

start = datetime.now()
temp = 0
for i in range(0, d):
    if i+k > d:
      new_index = i+k-d
      result = int(n[:new_index+1] + n[i:d])
    else:
      result = int(n[:i] + n[i+k:d])

    if temp < result:
        temp = result


print(temp)

# print(datetime.now() - start)f2