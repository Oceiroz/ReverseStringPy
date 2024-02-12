
def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input")
    return user_input

name_list = []

for x in range(0, 5, 1):
    name = get_input(f"{x+1} out of 5, please input a first name:", str)
    name_list.append(name)
#::-1 = start from other end
for x, name in enumerate(name_list):
    name_list[x] = name[::-1]
    print(name_list[x])