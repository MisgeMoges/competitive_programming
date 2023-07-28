def swap_case(s):
    swapped = s.swapcase()
    return swapped

    # swapped_str = ""

    # for char in s:
    #     if char.islower():
    #         swapped_str += char.upper()
    #     elif char.isupper():
    #         swapped_str += char.lower()
    #     else:
    #         swapped_str += char

    # return swapped_str



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
