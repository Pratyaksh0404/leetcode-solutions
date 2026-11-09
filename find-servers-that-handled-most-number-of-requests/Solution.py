class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = [0] * k
        busy = []
        free = []
        i = 0

        if not arrival or not load or not k:
            return []

        while i < k and i < len(load):
            heapq.heappush(busy, (arrival[i] + load[i], i % k))
            servers[i % k] += 1 
            i += 1

        while i < len(load):
            while busy and busy[0][0] <= arrival[i]:
                _, server_id = heapq.heappop(busy)
                heapq.heappush(free, i + (server_id - i) % k)
            
            if free:
                busy_id = heapq.heappop(free) % k
                heapq.heappush(busy, (arrival[i] + load[i], busy_id))
                servers[busy_id] += 1
            i += 1

        maxi = max(servers) 
        return [i for i, n in enumerate(servers) if n == maxi]