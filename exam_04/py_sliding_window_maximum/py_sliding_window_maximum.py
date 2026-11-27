from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    dq = deque()  # indices, front holds the max of the current window

    for i, value in enumerate(nums):
        # Drop indices that have fallen out of the window.
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Drop indices whose value is smaller than the current one.
        while dq and nums[dq[-1]] <= value:
            dq.pop()

        dq.append(i)

        # The window is full from index k - 1 onward.
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
