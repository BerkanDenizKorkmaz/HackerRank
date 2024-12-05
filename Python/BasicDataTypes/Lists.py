if __name__ == '__main__':
    N = int(input())
    counter = 0
    list = []
    while counter < N:
        query = input()
        query_list = query.split()

        if query_list[0] == "insert":
            list.insert(int(query_list[1]), int(query_list[2]))

        elif query_list[0] == "print":
            print(list)

        elif query_list[0] == "remove":
            list.remove(int(query_list[1]))

        elif query_list[0] == "append":
            list.append(int(query_list[1]))

        elif query_list[0] == "sort":
            list = sorted(list)

        elif query_list[0] == "pop":
            list.pop()

        elif query_list[0] == "reverse":
            list.reverse()

        counter += 1
