def count_list(l: list[int|str]) -> list[int]:
    new = list()
    for x in l:
        n = len(str(x))
        new.append(n)
    return new


def main():
    l = ["abc", "apple", "orange"]
    print(count_list(l))

    l = [12, 456, 9000]
    print(count_list(l))

if __name__=="__main__":
    main()