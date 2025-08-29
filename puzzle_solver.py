from collections import deque
import copy

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def serialize(state):
    return str(state)

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_new_state(state, direction):
    x, y = find_zero(state)
    dx, dy = MOVES[direction]
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_state = copy.deepcopy(state)
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
    return None

def bfs(start_state):
    queue = deque()
    visited = set()
    queue.append((start_state, []))
    visited.add(serialize(start_state))

    while queue:
        current_state, path = queue.popleft()
        if current_state == GOAL_STATE:
            return path + [current_state]

        for move in MOVES:
            new_state = get_new_state(current_state, move)
            if new_state and serialize(new_state) not in visited:
                visited.add(serialize(new_state))
                queue.append((new_state, path + [current_state]))

    return None

start = [[1, 2, 3],
         [0, 4, 6],
         [7, 5, 8]]

solution = bfs(start)

if solution:
    print(f"Çözüm {len(solution)-1} adımda bulundu:\n")
    for i, state in enumerate(solution):
        print(f"Adım {i}:")
        for row in state:
            print(row)
        print("---------")
else:
    print("Çözüm bulunamadı.")
