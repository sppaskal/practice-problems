import heapq


def min_rooms(intervals):
    if not intervals:
        return 0

    # sort the intervals based on start
    intervals.sort(key=lambda x: x[0])

    # min heap for end times
    heap = []
    max_rooms = 0

    for start, end in intervals:
        while heap and start >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, end)
        max_rooms = max(max_rooms, len(heap))

    return max_rooms


# TEST CODE
intervals = [(9, 13), (10, 11), (14, 17), (12, 13), (18, 19)]
print(min_rooms(intervals))
