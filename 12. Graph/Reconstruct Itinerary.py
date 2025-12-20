class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        sort_tickets = sorted(tickets,reverse = True)

        for departure, arrival in sort_tickets:
            adj[departure].append(arrival)

        res = []
        # stack = ["JFK"]

        # while stack:
        #     if adj[stack[-1]]:
        #         stack.append(adj[stack[-1]].pop())
        #     else:
        #         res.append(stack.pop())

        def dfs(departure):
            while adj[departure]:
                arrival = adj[departure].pop()
                dfs(arrival)
            res.append(departure)

        dfs("JFK")

        return res[::-1]