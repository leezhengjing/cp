import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))
    A.sort()
    res = []
    prefix_sum = [0]
    for num in A:
        prefix_sum.append(prefix_sum[-1] + num)
    for b in B:
        print(prefix_sum[b])
if __name__ == "__main__":
    main()