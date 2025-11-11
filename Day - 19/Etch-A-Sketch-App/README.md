# Etch-A-Sketch App 🎨

A digital recreation of the classic Etch-A-Sketch toy using Python's Turtle graphics.

## 🎮 How to Play

**Controls:**
- **W** - Move forward (hold for continuous movement)
- **S** - Move backward (hold for continuous movement)  
- **A** - Turn left (hold for continuous turning)
- **D** - Turn right (hold for continuous turning)
- **C** - Clear screen and reset turtle to center

## 🚀 Features

- Smooth continuous movement with key press/release detection
- Real-time drawing as you move
- Clear function to start fresh
- Responsive controls with 100ms update intervals

## 🛠️ Technical Implementation

- **Event Handling**: Uses `onkeypress` and `onkeyrelease` for smooth control
- **Continuous Movement**: Timer-based movement loop for fluid motion
- **Global State**: Flags to track which keys are currently pressed
- **Screen Management**: Automatic clearing and turtle repositioning

## 📚 Concepts Learned

- Advanced event handling in Turtle graphics
- Global variables and state management
- Timer-based animation loops
- Key press vs key release events
- Coordinate system and turtle positioning

## 🎯 Usage

```bash
python main.py
```

Click anywhere on the screen to exit the application.