def split_and_join(line):
    words = line.split(" ")
    output = ""
    for element in words:
        if output == "":
            output = element
        else:
            output = output + "-" + element
    return output


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)