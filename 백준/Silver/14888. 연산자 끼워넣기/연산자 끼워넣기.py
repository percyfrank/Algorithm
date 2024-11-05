n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_res = -float('inf')
min_res = float('inf')


def backtracking(idx, res, add, sub, mul, div):
    global max_res, min_res

    if idx == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    if add:
        backtracking(idx + 1, res + nums[idx], add - 1, sub, mul, div)
    if sub:
        backtracking(idx + 1, res - nums[idx], add, sub - 1, mul, div)
    if mul:
        backtracking(idx + 1, res * nums[idx], add, sub, mul - 1, div)
    if div:
        backtracking(idx + 1, int(res / nums[idx]), add, sub, mul, div - 1)

backtracking(1, nums[0], add, sub, mul, div)
print(max_res)
print(min_res)