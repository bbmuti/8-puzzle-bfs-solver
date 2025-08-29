# 8-Puzzle Solver (BFS)

Bu proje, klasik **8-Puzzle problemine** yönelik bir çözüm algoritması içerir.  
Amaç, karışık haldeki puzzle’ı en kısa adım sayısı ile çözüm durumuna ulaştırmaktır.  

Çözüm için **Breadth-First Search (BFS)** algoritması kullanılmıştır.  

---

## Hedef Durum (Goal State)

> Burada `0` boş kutuyu temsil eder.

---

## ⚙️ Özellikler
- BFS ile **en kısa çözüm yolunu** bulur.  
- Her hamlede **geçerli durumları** sıraya ekler, tekrarları engeller.  
- `visited` kümesi sayesinde aynı duruma tekrar girmez.  
- Her adımı ekrana basarak çözüm yolunu gösterir.  

---

## 🚀 Çalıştırma

### Gereksinimler
- Python 3.x

### Kullanım
1. Depoyu klonla:
   ```bash
   git clone https://github.com/<kullanıcı-adın>/8-puzzle-bfs-solver.git
   cd 8-puzzle-bfs-solver
2. Programı çalıştır:
  python puzzle_solver.py

Örnek:
Çözüm 4 adımda bulundu:

Adım 0:
[1, 2, 3]
[0, 4, 6]
[7, 5, 8]
---------
Adım 1:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]
---------
...
Adım 4:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
---------

