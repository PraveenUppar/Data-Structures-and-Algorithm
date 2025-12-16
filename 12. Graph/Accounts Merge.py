class UnionFind:
    def __init__(self, n):
        self.parent(i for i in range(n))
        self.rank = [1] * n

    def find(self,parent):
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
        return parent

    def union(self,parent1,parent2):
        parent1 = self.find(parent1)
        parent2 = self.find(parent2)

        if parent1 == parent2:
            return False
        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        acc_email_map = {}

        for id, acc in enumerate(accounts):
            for mail in acc[1:]:
                if mail in acc_email_map:
                    uf.union(id, acc_email_map[mail])
                else:
                    acc_email_map[mail] = id

        email_group = defaultdict(list)

        for mail, i in acc_email_map.items():
            leader = uf.find(i)
            email_group[leader].append(mail)

        res = []
        for i, mails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))
        return res

