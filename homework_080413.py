#   ***Question 1 solution***
def reverse_number_in_list(number_list):
    reversed_list = []
    for number in number_list:
        # Remove trailing zeros
        number_str = str(number)
        while number_str.endswith("0"):
            number_str = number_str[:-1]

        # Reverse the number and append to the reversed list
        reversed_number_str = number_str[::-1]
        reversed_number = int(reversed_number_str)
        reversed_list.append(reversed_number)

    return reversed_list


number_list = [123, 456, 7890, 1000]
reversed_list = reverse_number_in_list(number_list)
print(reversed_list)  # ["321", "654", "987", "1"]


#   ***Question 2 solution***
def tails_same(number_list):
    if len(number_list) < 2:
        return "you should have up to two numbers in the list"
    else:
        return number_list[0] == number_list[-1]


number_list1 = [1, 10, 11, 4]
print(tails_same(number_list1))  # false


#   ***Question 3 solution***
def remove_char(str_list, char):
    return [s.replace(char, '') for s in str_list]


str_list = ["computer", "science", "student"]
char = 'e'
new_str_list = remove_char(str_list, char)
print(new_str_list)  # ["computr", "scinc", "studnt"]


#   ***Question 4 solution***
def return_growing_num_list(max):
    num_list = []
    for i in range(1, max+1):
        num_list.append(str(i) * i)
        if len(num_list) == max:
            break
    return [num_str.strip().replace('', ' ').strip() for num_str in num_list]


max = 5
num_list = return_growing_num_list(max)
print(num_list)  # ['1', '2 2', '3 3 3', '4 4 4 4', '5 5 5 5 5']


#   ***Question 5 solution***
def find_color(colors: set, values: list) -> list:
    result = []
    for color, number in values:
        if color in colors:
            result.append(number)
    return result


# Define the set of colors and the list of tuples
colors = {'red', 'green', 'blue'}
values = [('red', 1), ('green', 2), ('yellow', 3), ('blue', 4), ('green', 5)]

# Call the function and print the result
result = find_color(colors, values)
print(result)  # Output: [1, 2, 4, 5]


#   ***Question 6 solution***
def dict_contains_keys(items: set, example_dict: dict) -> bool:
    for key in example_dict.keys():
        if key in items:
            return True
    return False


print(dict_contains_keys({2, 4, 6}, {1: 'a', 2: 'b', 4: 'c'}))  # True


#   ***Question 7 solution***
def concatenate_dict(dict_list: list) -> dict:
    result_dict = {}
    for d in dict_list:
        for k, v in d.items():
            if k not in result_dict:
                result_dict[k] = v
    return result_dict


dict_list = [
    {'a': 1, 'b': 2, 'c': 3},
    {'d': 4, 'e': 5, 'a': 6},
    {'f': 7, 'g': 8, 'b': 9}
]
concatenated_dict = concatenate_dict(dict_list)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 7, 'g': 8}
print(concatenated_dict)


#   ***Question 8 solution***
def unique_values(a_dict: dict) -> dict:
    to_ret = {}
    value_count = {}
    # count the occurrence of each value in the input dictionary
    for v in a_dict.values():
        if v in value_count:
            value_count[v] += 1
        else:
            value_count[v] = 1
    # add unique values to the output dictionary
    for k, v in a_dict.items():
        if value_count[v] == 1:
            to_ret[v] = k
    return to_ret


a_dict = {'X': 2, 'Y': 5, 'N': 2, 'L': 2, 'W': 1, 'G': 0, 'R': 1}
to_ret = unique_values(a_dict)
print(to_ret)  # {5: 'Y', 0: 'G'}


#   ***Question 9 solution***
def dict_from_string(dict_str: str) -> dict:
    # Remove curly braces and whitespace from the string
    dict_str = dict_str.replace("{", "").replace("}", "").replace(" ", "")

    # Split the string into a list of key-value pairs
    pairs = dict_str.split(",")

    # Create an empty dictionary to store the key-value pairs
    result_dict = {}

    # Iterate over the list of key-value pairs and add them to the dictionary
    for pair in pairs:
        # Split each pair into a key and a value
        key, value = pair.split(":")
        # Convert the key to a string and the value to an integer (if possible)
        try:
            value = int(value)
        except ValueError:
            pass
        # Add the key-value pair to the dictionary
        result_dict[str(key)] = value

    return result_dict


dict_str = "{a:1, b:2, c:3}"
print(dict_from_string(dict_str))  # {'a': 1, 'b': 2, 'c': 3}


#   ***Question 10 solution***
def flip_matrix(mat: list) -> list:
    return mat[::-1]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flipped = flip_matrix(matrix)
print('\n'.join([''.join(['{:4}'.format(item)
      for item in row]) for row in flipped]))
