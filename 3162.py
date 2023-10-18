import math

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        minimum = min(dist(m[i], m[j]) for j in range(n) if i != j)
        if minimum < 20:
            print('A')
        elif minimum < 50:
            print('M')
        else:
            print('B')

if __name__ == "__main__":
    main()
