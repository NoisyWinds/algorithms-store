graph = {
    "a": ["b"],
    "b": ["a"],
}

def TopologicalSort(graph):
  degrees = dict((u, 0) for u in graph)
  for u in graph:
      for v in graph[u]:
          degrees[v] += 1
  #入度为0的插入队列
  queue = [u for u in graph if degrees[u] == 0]
  res = []
  print(degrees)
  while queue:
      u = queue.pop()
      res.append(u)
      for v in graph[u]:
      	  # 移除边，即将当前元素相关元素的入度-1
          degrees[v] -= 1
          if degrees[v] == 0:
              queue.append(v)
  return res

print(TopologicalSort(graph)) # ['a', 'd', 'e', 'b', 'c']
