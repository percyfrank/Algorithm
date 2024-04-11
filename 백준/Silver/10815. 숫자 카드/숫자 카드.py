import sys
input = sys.stdin.readline

def find_number(num,arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

    return False

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
cards = list(map(int,input().split()))

print(" ".join(["1" if find_number(card,arr) else "0" for card in cards]))
