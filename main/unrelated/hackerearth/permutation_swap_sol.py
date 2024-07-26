n = int(input())
print()

for i in range(0, n):
    k = int(input())
    inputs = input()
    inputs = inputs.split(' ')
    val_inputs = []
    for j in range(0, len(inputs)):
      val_inputs.append(inputs[j])

    results = {}
    for j in range(0, k):
        if j+1 == k:
            break

        m = int(val_inputs[j])-1
        l = int(val_inputs[j+1])+1

        results[m] = m
        results[l] = l
    
    if len(results) == k:
        print('YES')
    else:
        print('NO')