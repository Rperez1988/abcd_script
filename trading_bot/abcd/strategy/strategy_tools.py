# def assign_numbers(original_lists):
#     uf = UnionFind()

#     for i, lst in enumerate(original_lists):
#         uf.parent[i] = i
#         uf.rank[i] = 0

#     for i in range(len(original_lists)):
#         for j in range(i + 1, len(original_lists)):
#             if any(string in original_lists[j]['list'] for string in original_lists[i]['list']):
#                 uf.union(i, j)

#     groups = {}
#     for i in range(len(original_lists)):
#         root = uf.find(i)
#         if root not in groups:
#             groups[root] = len(groups) + 1

#     result = []
#     for i, lst in enumerate(original_lists):
#         root = uf.find(i)
#         result.append({'id': lst['id'], 'number': groups[root], 'list': lst['list']})

#     return result

# class UnionFind:
#     def __init__(self):
#         self.parent = {}
#         self.rank = {}

#     def find(self, x):
#         if x != self.parent[x]:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         x_root = self.find(x)
#         y_root = self.find(y)

#         if x_root != y_root:
#             if self.rank[x_root] < self.rank[y_root]:
#                 self.parent[x_root] = y_root
#             elif self.rank[x_root] > self.rank[y_root]:
#                 self.parent[y_root] = x_root
#             else:
#                 self.parent[y_root] = x_root
#                 self.rank[x_root] += 1

# def assign_numbers(original_lists):
#     uf = UnionFind()

#     for i, lst in enumerate(original_lists):
#         uf.parent[i] = i
#         uf.rank[i] = 0

#     for i in range(len(original_lists)):
#         for j in range(i + 1, len(original_lists)):
#             if any(string in original_lists[j]['list'] for string in original_lists[i]['list']):
#                 uf.union(i, j)

#     groups = {}
#     for i in range(len(original_lists)):
#         root = uf.find(i)
#         if root not in groups:
#             groups[root] = len(groups) + 1

#     result = []
#     for i, lst in enumerate(original_lists):
#         root = uf.find(i)
#         result.append({'id': lst['id'], 'number': groups[root], 'list': lst['list']})

#     return result

# new_list = []

# for each in allTrades:
#     new_list.append(
#     {
#         'id': each.tradeInfo['id'],
#         'number': None,
#         'list': [
#             each.pivotInfo['pivotA']['date'],
#             each.pivotInfo['pivotB']['date'],
#             each.pivotInfo['pivotC']['date'],
#             each.pivotInfo['pivotD']['date']
#             ]
#     })

# result = assign_numbers(new_list)

# def check_failed_pivot_trios(failedTrios, aDate, bDate):

#             for each in failedTrios:
                
#                 if str(each.pivot_A.pivotInfo['pivotDate'] ) == aDate:
#                     if str(each.pivot_B.pivotInfo['pivotDate'] ) == bDate:
#                          print(each.pivot_A.pivotInfo['pivotDate'],each.pivot_B.pivotInfo['pivotDate'],each.pivot_C.pivotInfo['pivotDate'], each.failPoint)

        