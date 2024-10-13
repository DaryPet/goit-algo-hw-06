# goit-algo-hw-06

# Висновки для алгоритмів DFS і BFS

## Опис графа

Граф представляє соціальну мережу, де вузли — це люди, а ребра — це їхні зв'язки. Кожен зв'язок має свою "вагу", яка показує, наскільки сильний зв'язок між двома людьми.

### Кількість людей (вузлів):

7

### Кількість зв'язків (ребер):

8

### Люди:

- Alice, Bob, Charlie, David, Eve, Frank, Grace

### Зв'язки між людьми:

- Alice ↔ Bob: 1
- Alice ↔ Charlie: 4
- Bob ↔ David: 2
- Charlie ↔ Eve: 5
- David ↔ Eve: 1
- Eve ↔ Frank: 3
- Frank ↔ Grace: 2
- Grace ↔ Alice: 8

---

## Алгоритм DFS (Пошук в глибину)

### Шлях, знайдений DFS (від Alice до Frank):

`['Alice', 'Bob', 'David', 'Eve', 'Frank']`

- **Як працює DFS**:

  - DFS спочатку йде якомога глибше по одному шляху, і тільки потім повертається назад, щоб дослідити інші варіанти. У нашому випадку він спочатку проходить через **Bob** та **David**, а потім через **Eve** до **Frank**.
  - Оскільки DFS шукає в глибину, він не завжди знаходить найкоротший шлях.

- **Чому цей шлях**:
  - DFS просто йшов глибоко по одному шляху і не перевіряв, чи є інші, коротші шляхи. Тому він прийшов до **Frank** через **Bob**, **David** і **Eve**.

---

## Алгоритм BFS (Пошук в ширину)

### Шлях, знайдений BFS (від Alice до Frank):

`['Alice', 'Grace', 'Frank']`

- **Як працює BFS**:

  - BFS спочатку перевіряє всі найближчі вершини (сусіди) перед тим, як йти глибше. Тому він завжди знаходить найкоротший шлях за кількістю кроків.
  - У нашому випадку BFS знайшов шлях через **Grace** і відразу до **Frank**, оскільки це найкоротший маршрут.

- **Чому цей шлях**:
  - BFS спочатку перевірив сусідів **Alice** і знайшов **Grace** як кращий варіант для досягнення **Frank** з меншою кількістю кроків. Тому шлях через **Grace** був вибраний швидше, ніж шлях через інші вузли.

---

## Порівняння алгоритмів DFS і BFS

### Різниця в знайдених шляхах:

- **DFS Шлях**:
  - DFS пройшов через **Bob**, **David** та **Eve**, щоб дістатися до **Frank**.
  - Шлях: `['Alice', 'Bob', 'David', 'Eve', 'Frank']`
- **BFS Шлях**:
  - BFS знайшов коротший шлях через **Grace** до **Frank**.
  - Шлях: `['Alice', 'Grace', 'Frank']`

### Чому вони різні:

- **DFS** йде глибоко по одному шляху і може пропустити більш короткі шляхи, оскільки він повертається до інших варіантів тільки після того, як завершить один напрямок.
- **BFS** навпаки, спочатку перевіряє всі сусіди і знаходить найкоротший шлях за кількістю кроків. Тому він знайшов шлях через **Grace**, який був коротшим.

---

## Висновок

- **DFS** пройшов довший шлях, оскільки досліджує глибину, а не завжди шукає найкоротший шлях.
- **BFS** знайшов найкоротший шлях за кількістю кроків, що робить його більш ефективним для пошуку в невагових графах або там, де важливі кількість кроків.
- У деяких випадках **DFS** може бути корисним, але для знаходження найкоротшого шляху за кількістю кроків **BFS** є надійнішим вибором.

# Conclusions for DFS and BFS Algorithms

## Graph Description

The graph represents a social network where nodes are people and edges are relationships between them. Each edge has a weight that represents the strength of the connection between two people.

### Number of Nodes (People):

7

### Number of Edges (Relationships):

8

### Nodes:

- Alice, Bob, Charlie, David, Eve, Frank, Grace

### Edges (Relationships with weights):

- Alice ↔ Bob: 1
- Alice ↔ Charlie: 4
- Bob ↔ David: 2
- Charlie ↔ Eve: 5
- David ↔ Eve: 1
- Eve ↔ Frank: 3
- Frank ↔ Grace: 2
- Grace ↔ Alice: 8

---

## DFS (Depth-First Search)

### Path Found by DFS (Alice to Frank):

`['Alice', 'Bob', 'David', 'Eve', 'Frank']`

- **How DFS Works**:

  - DFS explores one branch of the graph deeply before backtracking to explore other branches. In this case, it explores the path through **Bob** and **David** to reach **Eve** and then **Frank**.
  - DFS does not always guarantee the shortest path because it goes deep into one branch before exploring alternatives.

- **Explanation**:
  - DFS visits each node connected to **Alice** in a deep manner, starting with **Bob** and continuing until it reaches **Frank**. It finds **Frank** through **Eve**, as it follows one deep branch without considering weights or shorter alternatives.

---

## BFS (Breadth-First Search)

### Path Found by BFS (Alice to Frank):

`['Alice', 'Grace', 'Frank']`

- **How BFS Works**:

  - BFS explores the graph level by level, ensuring that the shortest path in terms of the number of edges is found. It checks all immediate neighbors before going deeper.
  - In this case, BFS finds the path through **Grace** and then directly to **Frank** because it's the shorter path in terms of edge count.

- **Explanation**:
  - BFS looks at all immediate neighbors of **Alice** first, so it finds **Grace** as a better option to reach **Frank** in fewer steps. Since BFS examines all neighbors at the current level before moving deeper, it finds the shortest path based on the number of hops (edges).

---

## Comparison of DFS and BFS

### Differences in the Found Paths:

- **DFS Path**:
  - Goes through **Bob** and **David** to eventually reach **Frank**.
  - Path: `['Alice', 'Bob', 'David', 'Eve', 'Frank']`
- **BFS Path**:
  - Finds a direct path via **Grace** to reach **Frank** in fewer steps.
  - Path: `['Alice', 'Grace', 'Frank']`

### Explanation of Differences:

- **DFS** explores deeply, which can result in finding longer paths, especially in cases where shorter paths exist but are ignored during deep traversal. This is why DFS took a longer path, going through **Bob** and **David**.
- **BFS**, on the other hand, guarantees finding the shortest path in terms of the number of edges by exploring level by level. Since **Grace** was a direct neighbor of **Alice**, BFS identified it as the quicker route to **Frank**.

### Why the Paths Differ:

- DFS explores deeply and may miss shorter paths by focusing on one branch.
- BFS looks for the shortest path in terms of edge count by checking all immediate neighbors first, making it more effective for finding quick routes in graphs without considering weights.

---

## Conclusion

- **DFS** found a longer path because it explores deeply and does not always consider the shortest route.
- **BFS** found the shortest path in terms of edge count, making it more efficient for finding paths in unweighted graphs or graphs where edge count matters.
- Both algorithms are useful depending on the situation, but for finding the shortest path in terms of steps, BFS is generally more reliable.
