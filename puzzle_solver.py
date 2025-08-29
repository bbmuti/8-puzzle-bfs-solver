from collections import deque  # Kuyruk veri yapısı için kullanılır (FIFO)
import copy  # Derin kopyalama için kullanılır (liste kopyaları için)

# Hedef durum (goal state) — çözüm olarak ulaşılması gereken puzzle dizilimi
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Puzzle'da yapılabilecek hareketler: yukarı, aşağı, sola, sağ
MOVES = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Verilen puzzle durumunu string formatına çevirir (visited kümesinde saklamak için)
def serialize(state):
    return str(state)

# Boş kutunun (0) bulunduğu konumu döndürür
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Belirli bir yönde hamle yapılırsa oluşacak yeni durumu üretir
def get_new_state(state, direction):
    x, y = find_zero(state)  # 0'ın yeri
    dx, dy = MOVES[direction]  # hareket yönü
    new_x, new_y = x + dx, y + dy  # yeni pozisyon
    if 0 <= new_x < 3 and 0 <= new_y < 3:  # sınır kontrolü
        new_state = copy.deepcopy(state)  # orijinal durumu bozmadan kopyala
        # 0 ile hedef kutunun yerini değiştir
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
    return None  # geçersiz hamle varsa None döndür

# Genişlik Öncelikli Arama (BFS) algoritması
def bfs(start_state):
    queue = deque()  # arama sırası için kuyruk
    visited = set()  # daha önce ziyaret edilen durumlar

    # Kuyruğa başlangıç durumu ve boş yol ile ekle
    queue.append((start_state, []))
    visited.add(serialize(start_state))

    # Kuyruk boşalana kadar devam et
    while queue:
        current_state, path = queue.popleft()  # sıradaki durumu al

        # Hedef duruma ulaşıldıysa çözüm yolunu döndür
        if current_state == GOAL_STATE:
            return path + [current_state]

        # Her yöndeki hamle için yeni durumları sıraya ekle
        for move in MOVES:
            new_state = get_new_state(current_state, move)
            if new_state and serialize(new_state) not in visited:
                visited.add(serialize(new_state))  # ziyaret edildi olarak işaretle
                queue.append((new_state, path + [current_state]))  # yeni durumu sıraya ekle

    return None  # çözüm yoksa None döndür

# Başlangıç durumu tanımlanıyor
start = [[1, 2, 3],
         [0, 4, 6],
         [7, 5, 8]]

# BFS algoritmasıyla çözüm aranıyor
solution = bfs(start)

# Eğer çözüm bulunduysa, her adımı sırayla yazdır
if solution:
    print(f"Çözüm {len(solution)-1} adımda bulundu:\n")
    for i, state in enumerate(solution):
        print(f"Adım {i}:")
        for row in state:
            print(row)
        print("---------")
else:
    print("Çözüm bulunamadı.")
