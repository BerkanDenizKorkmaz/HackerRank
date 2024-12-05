def swap_case(s):
    output = ""
    for element in s:
        if element.islower():
            output += element.upper()

        else:
            output += element.lower()

    return output


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)