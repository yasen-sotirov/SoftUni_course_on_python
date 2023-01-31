from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)

    while nums:
        kwargs["a"] += nums.popleft()
        if nums == 0:
            break

        kwargs["s"] -= nums.popleft()
        if nums == 0:
            break

        divider = nums.popleft()
        if divider != 0:
            kwargs["d"] /= divider
        else:
            continue

        kwargs["m"] *= nums.popleft()
        if nums == 0:
            break
    return nums


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))