import heapq


def solution(operations):
    minHeap = []
    maxHeap = []

    for op in operations:
        command, value = tuple(op.split())
        value = int(value)
        if command == 'I':
            heapq.heappush(minHeap, value)
            heapq.heappush(maxHeap, value*-1)
        elif command == 'D' and value == 1:
            if len(maxHeap) > 0:
                x = heapq.heappop(maxHeap) * -1
                minHeap.remove(x)
        elif command == 'D' and value == -1:
            if len(minHeap) > 0:
                x = heapq.heappop(minHeap)
                maxHeap.remove(x * -1)
    if len(minHeap) > 0:
        answer = [heapq.heappop(maxHeap)*-1, heapq.heappop(minHeap)]
    else:
        answer = [0, 0]
    return answer
