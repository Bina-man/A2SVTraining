if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b, c = map(int, input().split())

        if a == b+c:
            print("YES")
        elif b == a+c:
            print("YES")
        elif c == a+b:
            print("YES")
        else:
            print("NO")