# Day 43 - Spanish Colors Learning Website 🎨

## Project Overview
Interactive Spanish color learning website combining HTML structure with CSS styling. Features color-coded text, uniform image sizing, and organized asset management for an educational web experience.

## What I Learned
- **CSS Fundamentals**: External stylesheet linking and basic CSS syntax
- **CSS Selectors**: ID selectors (#), class selectors (.), and element selectors
- **Color Properties**: Using CSS color property with named colors
- **Font Styling**: Controlling font-weight for text appearance
- **Image Styling**: CSS properties for image dimensions and object-fit
- **File Organization**: Structured asset management with folders
- **CSS Linking**: Connecting external CSS files to HTML documents

## Key Features
- **Color-Coded Learning**: Each Spanish color name displayed in its corresponding color
- **Uniform Image Display**: All color images sized consistently as 200x200px squares
- **Educational Content**: Spanish color vocabulary with visual associations
- **Clean Styling**: Non-bold color titles for better readability
- **Organized Assets**: Proper folder structure for images and stylesheets
- **Responsive Images**: Object-fit property for proper image scaling

## How to Run
Open the HTML file in any web browser:
```bash
# Double-click index.html or
# Right-click and select "Open with Browser"
```

## Files & Directory Structure
```
Day - 43/
├── index.html
├── style.css
├── assets/
│   └── images/
│       ├── red.png
│       ├── blue.png
│       ├── orange.png
│       ├── green.png
│       └── yellow.png
└── README.md
```

## CSS Concepts Used

### 1. ID Selectors
```css
#red { color: red; }
#blue { color: blue; }
```

### 2. Class Selectors
```css
.color-title { font-weight: normal; }
```

### 3. Element Selectors
```css
img {
    width: 200px;
    height: 200px;
    object-fit: cover;
}
```

## HTML-CSS Integration
- **External Stylesheet**: `<link rel="stylesheet" href="style.css">`
- **ID Attributes**: Unique identifiers for specific styling
- **Class Attributes**: Shared styling across multiple elements
- **Semantic Structure**: Meaningful HTML with enhanced CSS presentation

## Spanish Colors Featured
- **Rojo** (Red) - Displayed in red color
- **Azul** (Blue) - Displayed in blue color
- **Anaranjado** (Orange) - Displayed in orange color
- **Verde** (Green) - Displayed in green color
- **Amarillo** (Yellow) - Displayed in goldenrod color

## CSS Properties Demonstrated
- **color**: Text color styling
- **font-weight**: Text boldness control
- **width/height**: Element dimensions
- **object-fit**: Image scaling behavior

## Web Development Concepts
- **Separation of Concerns**: HTML for structure, CSS for presentation
- **Asset Organization**: Logical folder structure for project files
- **Visual Consistency**: Uniform styling across similar elements
- **Educational Design**: Color association for learning enhancement
- **Responsive Images**: Proper image handling with object-fit

## Educational Applications
- Language learning websites
- Visual vocabulary builders
- Interactive educational content
- Color theory demonstrations
- Multilingual learning tools

---
*Day 43 of 100 Days of Python Challenge - Introduction to CSS*