
if __name__ == '__main__':
    score_list = []
    record = []
    score_list_sorted = []
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
        score_list.append(score)

    score_list = sorted(score_list)
    for element in score_list:
        if element not in score_list_sorted:
            score_list_sorted.append(element)

    for i in record:
        if i[1] == score_list_sorted[1]:
            names.append(i[0])

    names = sorted(names)

    for name in names:
        print(name)
