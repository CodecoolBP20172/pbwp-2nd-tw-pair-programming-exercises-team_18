import random

def listoverlap(list1, list2):
    return list(set(list1) & set(list2))

def random_length(list_input):
        N = random.randint(10, 20)
        for i in range(N):
            list_input.append(random.randint(1, 50))
        return list_input

def main():
    list1 = []
    list2 = []
    random_length(list1)
    random_length(list2)
    print(sorted(list1))
    print(sorted(list2))
    print(listoverlap(list1,list2))
    return


if __name__ == '__main__':
    main()
