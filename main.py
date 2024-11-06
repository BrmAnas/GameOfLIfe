import tkinter as tk
import random
import time

# Création et variables pour la fenêtre principale
rows, cols = 20, 20
cell_size = 30
root = tk.Tk()
root.title("Jeu de la vie")
root.geometry(f"{cols * cell_size}x{rows * cell_size}")

#Création du canvas permettant de dessiner la grille
canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
canvas.pack()

# Initialisation de la grille aleatoirement
grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Comptage des voisins des cellules
def count_neighbors(row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_row = row + i
            neighbor_col = col + j
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                count += grid[neighbor_row][neighbor_col]
    return count

# Fonction pour mettre à jour la grille
def update_grid():
    global grid
    verif_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_neighbors(row, col)
            
            if grid[row][col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    verif_grid[row][col] = 0
                else:
                    verif_grid[row][col] = 1
            else:
                if live_neighbors == 3:
                    verif_grid[row][col] = 1
    grid = verif_grid

# Fonction pour mettre à jour l'ecran
def update_graph():
    update_grid()
    draw_grid()
    root.after(100, update_graph)  

# Fonction pour dessiner la grille
def draw_grid():
    canvas.delete("all")
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "black" if grid[row][col] == 1 else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")


draw_grid()
update_graph()
root.mainloop()
