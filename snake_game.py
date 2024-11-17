import tkinter as tk
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SNAKE_SIZE = 20
FOOD_SIZE = 20
SPEED = 100  
BG_COLOR = "white"
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"

DIRECTIONS = {
    "Up": (0, -SNAKE_SIZE),
    "Down": (0, SNAKE_SIZE),
    "Left": (-SNAKE_SIZE, 0),
    "Right": (SNAKE_SIZE, 0)
}

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Prem's Snake Game")
        self.canvas = tk.Canvas(self.window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BG_COLOR)
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)] 
        self.food = None
        self.direction = "Right"
        self.score = 0
        self.running = True

        self.window.bind("<KeyPress>", self.change_direction)

        self.create_food()
        self.update()
        self.window.mainloop()

    def create_food(self):
        x = random.randint(0, (GAME_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
        y = random.randint(0, (GAME_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
        self.food = (x, y)
        self.canvas.create_rectangle(x, y, x + FOOD_SIZE, y + FOOD_SIZE, fill=FOOD_COLOR, tag="food")

    def move_snake(self):
        head_x, head_y = self.snake[0]
        move_x, move_y = DIRECTIONS[self.direction]
        new_head = (head_x + move_x, head_y + move_y)

        if (
            new_head in self.snake  
            or new_head[0] < 0  
            or new_head[1] < 0 
            or new_head[0] >= GAME_WIDTH  
            or new_head[1] >= GAME_HEIGHT  
        ):
            self.running = False
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.canvas.delete("food")
            self.create_food()
        else:
            self.snake.pop()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )

    def change_direction(self, event):
        new_direction = event.keysym
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction in DIRECTIONS and new_direction != opposites[self.direction]:
            self.direction = new_direction

    def update(self):
        if self.running:
            self.move_snake()
            self.draw_snake()
            self.window.after(SPEED, self.update)
        else:
            self.canvas.create_text(
                GAME_WIDTH // 2,
                GAME_HEIGHT // 2,
                fill="black",
                font="Arial 20 bold",
                text=f"Khatam! Score: {self.score}",
            )

if __name__ == "__main__":
    SnakeGame()
