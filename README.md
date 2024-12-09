
# Snake Game

This is a classic **Snake Game** built using Python's Turtle graphics library. The player controls a snake that moves around the screen, eating food to grow longer while avoiding collisions with walls and its own body. The game ends when the snake hits a wall or itself.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Example Output](#example-output)
- [Technologies Used](#technologies-used)
- [License](#license)

---

## Features
- **Snake Movement**: Move the snake up, down, left, or right using the arrow keys.
- **Food System**: The snake eats food to grow longer.
- **Score Tracking**: The score increases every time the snake eats food.
- **Game Over Screen**: Displays "GAME OVER" when the player loses.
- **Dynamic Gameplay**: The game becomes progressively harder as the snake grows longer.

---

## Project Structure
```
📦 Snake Game
├── 📄 food.py             # Handles the creation and movement of food on the screen
├── 📄 main.py             # Main entry point of the game
├── 📄 scoreboard.py       # Handles the scoreboard logic (score, game over message)
├── 📄 snake.py            # Handles the snake's movement, collision logic, and growth
└── 📜 README.md           # Documentation for the Snake Game
```

---

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/snake-game.git
    cd snake-game
    ```

2. **Install Python** (if not installed):
    - Download and install Python from [python.org](https://www.python.org/).

3. **Run the Application**:
    ```bash
    python main.py
    ```

---

## How to Run

1. Run the following command in your terminal:
    ```bash
    python main.py
    ```

2. The game window will appear. Use the **Up, Down, Left, Right** arrow keys to control the snake.

3. Try to eat as much food as possible to increase your score.

4. The game ends if the snake hits the wall or itself.

---

## Usage
1. Use the arrow keys to control the movement of the snake.
2. Eat the food to grow the snake and increase your score.
3. Avoid collisions with the walls or the snake's own body.
4. When the game ends, the "GAME OVER" message will be displayed.

---

## Example Output
```
🐍 Snake Game 🐍
- The snake moves around the screen.
- Eat food to grow and increase your score.
- Avoid collisions with the wall or your own body.
- View your score on the top of the screen.
```

---

## Technologies Used
- **Python**: Core programming language used for logic and game flow.
- **Turtle**: Used for graphics and visualization of the game.

---

## Code Breakdown

### `food.py`
- Handles the creation of the food object.
- Randomly places food at different coordinates on the screen.

```python
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
```

### `snake.py`
- Handles the creation, movement, and growth of the snake.
- Contains logic for user input to control the snake's direction.

```python
class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake (self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range (len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
```

### `scoreboard.py`
- Displays the player's current score on the screen.
- Updates the score as the snake eats food.

```python
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
```

### `main.py`
- The main entry point of the game.
- Initializes the screen, snake, food, and scoreboard objects.
- Contains the game loop to update the screen and handle snake movement and collisions.

```python
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 
        or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
```

---

## Possible Improvements
- **Add Levels**: Increase speed as the player scores more points.
- **High Score Tracker**: Store and display the highest score.
- **Sound Effects**: Add sound for food collection or game-over events.
- **Mobile Version**: Create a touch-friendly version for mobile devices.

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

---

**Enjoy the Game!**
