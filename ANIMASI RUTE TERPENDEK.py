import turtle
import time

# Koordinat titik untuk simpul
nodes = {
    "U": (0, 200),
    "V": (-200, 100),
    "W": (200, 100),
    "X": (-200, -100),
    "Y": (200, -100),
    "Z": (0, -200)
}

# Rute terpendek
shortest_path = ["U", "Z", "W", "V", "X", "Y", "U"]

# Fungsi menggambar simpul
def draw_node(t, name, x, y):
    t.penup()
    t.goto(x, y - 10)  # Sesuaikan posisi teks
    t.write(name, align="center", font=("Arial", 12, "bold"))
    t.goto(x, y)
    t.pendown()
    t.dot(20, "blue")  # Lingkaran simpul

# Fungsi menggambar garis antar simpul
def draw_edge(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

# Menggambar graf
def draw_graph(t):
    # Gambar simpul
    for name, (x, y) in nodes.items():
        draw_node(t, name, x, y)
    # Gambar sisi awal (semua sisi dengan warna abu-abu)
    edges = [
        ("U", "Z"),
        ("Z", "W"),
        ("W", "V"),
        ("V", "X"),
        ("X", "Y"),
        ("Y", "U")
    ]
    t.pencolor("gray")
    for start, end in edges:
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        draw_edge(t, x1, y1, x2, y2)

# Animasi TSP
def animate_tsp(t, path):
    t.pencolor("blue")
    t.pensize(3)
    for i in range(len(path) - 1):
        start, end = path[i], path[i + 1]
        x1, y1 = nodes[start]
        x2, y2 = nodes[end]
        draw_edge(t, x1, y1, x2, y2)
        time.sleep(1)  # Tunggu 1 detik sebelum menggambar sisi berikutnya

# Main Program
def main():
    screen = turtle.Screen()
    screen.title("Traveling Salesman Problem - Turtle Animation")
    screen.setup(width=800, height=600)

    t = turtle.Turtle()
    t.speed(0)  # Set kecepatan maksimal untuk menggambar graf awal
    t.hideturtle()

    # Gambar graf awal
    draw_graph(t)

    # Animasi rute terpendek
    animate_tsp(t, shortest_path)

    # Menjaga jendela tetap terbuka
    screen.mainloop()

if __name__ == "__main__":
    main()
