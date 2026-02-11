if __name__ == '__main__':
    phone_numbers = {}
    n = int(input())

    for _ in range(n):
        name, number = input().split()
        phone_numbers[name] = number

    while True:
        try:
            query = input()
            if query in phone_numbers:
                print(f"{query}={phone_numbers[query]}")
            else:
                print("Not found")
        except EOFError:
            break
