n = input()
for i in range(0, int(n)):
    rot_params_str = input()
    rot_params = rot_params_str.split(" ")
    arr_input_str = input()
    arr_input = arr_input_str.split(" ")

    new_arr = [val for val in arr_input]
    arr_length = int(rot_params[0])
    rot_index = int(rot_params[1])

    for j in range(0, arr_length):
        new_index = (j + rot_index) % arr_length
        new_arr[new_index] = arr_input[j]
    
    for j in range(0, len(new_arr)):
        if j == len(new_arr) - 1:
            print(new_arr[j])
        else:
            print(new_arr[j], end=" ")