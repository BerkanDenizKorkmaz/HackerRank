if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for i in student_marks[query_name]:
        total += i

    avg = total / len(student_marks[query_name])

    print(format(avg, ".2f"))
