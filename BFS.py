from collections import deque

#BFS: 큐 자료구조 이용 
def bfs(graph,start,visited):
  queue = deque([start])
  #현재 노드를 방문 처리 
  visited[start] = True

  while queue:
    #큐에서 하나의 원소를 뽑아 출력 
    v = queue.popleft()
    print(v, end=' ')
    #해당 원소와 연결된 
    for i in graph[v]:
      #아직 방문하지 않은 원소들을 큐에 삽입 
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],#0
  [2,3,8],#1
  [1,7],#2
  [1,4,5],#3
  [3,5],#4
  [3,4],#5
  [7],#6
  [2,6,8],#7
  [1,7]#8
  ]

visited = [False]*9

bfs(graph,1,visited)