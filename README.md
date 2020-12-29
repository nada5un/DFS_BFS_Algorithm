# DFS_BFS_Algorithm

- DFS : 깊이 우선 탐색. 재귀 함수, 인접 행렬 이용 

- BFS : 너비 우선 탐색. 가까운 노드부터 탐색, 큐 자료구조 이용 

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

출처: https://www.acmicpc.net/problem/1260
 
### 예제 입력 1

4 5 1

1 2

1 3

1 4

2 4

3 4

### 예제 출력 1

1 2 4 3

1 2 3 4



### 예제 입력 2

5 5 3

5 4

5 2

1 2

3 4

3 1

### 예제 출력 2

3 1 2 5 4

3 1 4 2 5
