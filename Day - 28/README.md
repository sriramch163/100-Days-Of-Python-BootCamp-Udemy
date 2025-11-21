# Day 28 - Pomodoro Timer 🍅

## Project Overview
Built a fully functional Pomodoro Timer desktop application using Tkinter GUI framework. This productivity tool implements the Pomodoro Technique with work sessions, breaks, visual feedback, and audio notifications for enhanced focus management.

## What I Learned
- **Tkinter GUI Development**: Creating desktop applications with widgets
- **Timer Mechanisms**: Implementing countdown functionality with threading
- **Event-Driven Programming**: Button callbacks and user interactions
- **Canvas Graphics**: Working with images and dynamic text updates
- **Audio Integration**: Sound notifications using winsound module
- **State Management**: Tracking timer states and session progress

## Key Features
- ✅ 25-minute work sessions with 5-minute short breaks
- ✅ 20-minute long break after every 4 work sessions
- ✅ Visual timer display with tomato image background
- ✅ Dynamic title updates (WORK/SHORT BREAK/LONG BREAK)
- ✅ Progress tracking with checkmark indicators
- ✅ Audio notifications when sessions complete
- ✅ Start/Reset functionality with button state management
- ✅ Color-coded interface for different session types

## Technical Implementation

### Pomodoro Technique Logic
- **Work Session**: 25 minutes (green indicator)
- **Short Break**: 5 minutes (pink indicator) after work sessions
- **Long Break**: 20 minutes (red indicator) after every 4th work session
- **Progress Tracking**: Checkmarks for completed work sessions

### GUI Components
- **Canvas**: Tomato image with overlay timer text
- **Labels**: Dynamic title and progress indicators
- **Buttons**: Start/Reset controls with state management
- **Timer Display**: MM:SS format with real-time updates

### Code Structure
```
Day - 28/
├── main.py     # Main application with GUI and timer logic
├── tomato.png  # Tomato image for visual design
└── README.md   # Project documentation
```

### Key Technical Concepts
- **Threading**: `window.after()` for non-blocking countdown
- **State Management**: Global variables for timer state tracking
- **Canvas Operations**: `itemconfig()` for dynamic text updates
- **Button States**: Disabling/enabling to prevent multiple timers
- **Audio Feedback**: `winsound.Beep()` for session completion alerts

## Color Scheme
- **Background**: Light yellow (#f7f5dd)
- **Work Sessions**: Green (#9bdeac)
- **Short Breaks**: Pink (#e2979c)
- **Long Breaks**: Red (#e7305b)

## Session Flow
1. Start timer → 25min work session
2. Automatic transition → 5min short break
3. Repeat cycle 4 times
4. After 4th work session → 20min long break
5. Reset cycle and continue

## How to Run
```bash
python main.py
```

**Requirements**: 
- Python with tkinter (usually included)
- tomato.png image file in same directory

**Concepts Mastered**: Tkinter GUI, Desktop Applications, Timer Mechanisms, Event Handling, Canvas Graphics