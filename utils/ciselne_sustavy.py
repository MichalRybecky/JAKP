def convert_list(input):
    converted_list = []
    for i in input:
        if ord(i) > 57:
            converted_list.append(int(ord(i) - 55))
        else:
            converted_list.append(int(i))
    return converted_list

def is_valid(input, base):
    if max(convert_list([str(x) for x in str(input)])) >= base:
        return False
    else:
        return True

def convert_base(input, input_base, output_base):
    """
    Converts a number in chosen base into a number of chosen base
    """
    if not 1 < input_base < 17:
        raise ValueError("Only supports base 2 to base 16")
    if not is_valid(input, input_base):
        raise ValueError("Invalid input or input_base")
    list_input = [str(x) for x in str(input)]
    exponent = len(list_input) - 1
    base_ten_result = 0
    for i in convert_list(list_input):
        base_ten_result += i * input_base ** exponent
        exponent -= 1
    remainders = []
    while base_ten_result != 0:
        remainder = base_ten_result % output_base
        if remainder > 9:
            remainders.append(chr(55 + remainder))
        else:
            remainders.append(str(remainder))
        base_ten_result = base_ten_result // output_base
    return "".join(reversed(remainders))