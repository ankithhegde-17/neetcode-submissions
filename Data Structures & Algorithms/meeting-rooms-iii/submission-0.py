class Solution:
    def mostBooked(self, n, meetings):
        import heapq

        free = list(range(n))
        busy = []
        count = [0] * n

        for start, end in sorted(meetings):
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                room = heapq.heappop(free)
                finish = end
            else:
                time, room = heapq.heappop(busy)
                finish = time + end - start

            count[room] += 1
            heapq.heappush(busy, (finish, room))

        return max(range(n), key=lambda i: (count[i], -i))