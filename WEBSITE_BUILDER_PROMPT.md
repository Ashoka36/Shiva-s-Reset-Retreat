# 🌌 AI Website Builder Agent - Complete Prompt & Code

## Overview
This AI Agent can build websites exactly like Shiva's Reset Retreat with Aurora Borealis theme, using OpenRouter and Groq APIs.

## Agent Capabilities

### 1. **HTML Generation (Groq API)**
The agent generates semantic HTML5 with:
- Glass morphism navbar with logo
- Hero section with twin images (side by side)
- Multiple content sections with images
- WhatsApp CTA button
- Footer with contact info
- Mobile responsive meta tags

### 2. **CSS Generation (OpenRouter API)**
The agent creates Aurora Borealis themed CSS with:
- **Color Palette**:
  - Cyan: #7df9ff
  - Green: #00ff88
  - Purple: #ff00ff
  - Pink: #ff7fdb
  - Dark Background: #0a0e27
  - Golden Yellow: #FFD700

- **Features**:
  - Glass morphism navbar (backdrop-filter: blur)
  - Parallax scrolling effects
  - Twin image layout (280px x 350px)
  - Smooth animations (@keyframes)
  - Responsive breakpoints (1024px, 768px, 480px, 360px)
  - Mobile-first design
  - Floating elements with glow
  - Gradient backgrounds

### 3. **JavaScript Generation**
The agent creates interactive features:
- Mobile hamburger menu
- Smooth scroll detection
- Parallax effects
- Intersection Observer animations
- WhatsApp integration
- Performance optimization

## How the Agent Works

### Step 1: Configuration Input
```json
{
  "site_name": "Shiva's Reset Retreat",
  "location": "Palolem, Goa, India",
  "tagline": "Reset your Mind, Body & Soul",
  "sections": [
    {
      "title": "Section Title",
      "description": "Description",
      "image": "image.jpg"
    }
  ],
  "whatsapp": "+917676432449",
  "theme": "aurora_borealis"
}
```

### Step 2: HTML Generation with Groq
```python
groq_prompt = """
Create HTML5 website with:
1. Glass morphism navbar
2. Hero section with twin images
3. Multiple content sections
4. WhatsApp CTA button
5. Responsive design
"""
```

### Step 3: CSS Generation with OpenRouter
```python
openrouter_prompt = """
Create Aurora Borealis CSS with:
1. Color scheme (cyan, green, purple, pink)
2. Glass morphism effects
3. Parallax scrolling
4. Responsive breakpoints
5. Smooth animations
"""
```

### Step 4: JavaScript Generation
- Mobile menu toggle
- Scroll detection
- Parallax effects
- Intersection Observer
- WhatsApp integration

### Step 5: File Creation
- index.html
- styles.css
- script.js
- config.json
- README.md

## CSS Architecture

### Color Variables
```css
:root {
    --aurora-cyan: #7df9ff;
    --aurora-green: #00ff88;
    --aurora-purple: #ff00ff;
    --aurora-pink: #ff7fdb;
    --dark-bg: #0a0e27;
    --accent-gold: #FFD700;
}
```

### Key CSS Classes
- `.navbar` - Glass morphism navigation
- `.hero` - Hero section with twin images
- `.hero-twin-images` - Twin image container
- `.hero-twin-pic` - Individual image wrapper
- `.content-section` - Content sections
- `.cta-section` - Call-to-action section
- `.section-image` - Responsive images

### Responsive Breakpoints
```css
/* Desktop: 1024px+ */
/* Tablet: 768px - 1023px */
/* Mobile: 480px - 767px */
/* Ultra Small: Below 480px */
```

## HTML Structure

### Hero Section with Twin Images
```html
<section class="hero">
  <div class="hero-content">
    <h1 class="hero-title">SHIVA'S RESET RETREAT</h1>
    <div class="hero-twin-images">
      <div class="hero-twin-pic">
        <img src="images/palolem-beach.jpg" alt="Palolem Beach">
        <h3 class="twin-text">Palolem Beach</h3>
      </div>
      <div class="hero-twin-pic">
        <img src="images/1beach.jpg" alt="Retreat">
        <h3 class="twin-text">Shiva's Retreat</h3>
      </div>
    </div>
  </div>
</section>
```

### WhatsApp Integration
```html
<a href="https://wa.me/917676432449" class="cta-button" target="_blank">
  📱 Book via WhatsApp
</a>
```

## JavaScript Features

### Mobile Menu Toggle
```javascript
hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});
```

### Parallax Scrolling
```javascript
window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
    element.style.transform = `translateY(${scrollPosition * 0.5}px)`;
});
```

### Intersection Observer (Animations)
```javascript
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
});
```

## API Usage

### Groq API (HTML Generation)
```python
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "mixtral-8x7b-32768",
    "messages": [{"role": "user", "content": html_prompt}],
    "max_tokens": 2000
}

response = requests.post(groq_url, json=payload, headers=headers)
```

### OpenRouter API (CSS Generation)
```python
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": css_prompt}],
    "max_tokens": 3000
}

response = requests.post(openrouter_url, json=payload, headers=headers)
```

## Deployment Steps

### 1. GitHub Setup
```bash
git init
git add .
git commit -m "Initial website commit"
git remote add origin https://github.com/username/repo.git
git push origin master
```

### 2. GitHub Pages
- Enable in repository settings
- Select master branch as source
- Website goes live at: https://username.github.io/repo

### 3. Render Deployment
- Connect GitHub repository
- Set build command: `npm install` (if needed)
- Set publish directory: `/`
- Deploy

## Features Implemented

✅ Aurora Borealis theme (cyan, green, purple, pink)
✅ Glass morphism navbar with backdrop blur
✅ Hero section with twin images side by side
✅ Parallax scrolling effects
✅ Responsive design (mobile-first)
✅ Golden yellow headings
✅ WhatsApp integration (no phone numbers exposed)
✅ Smooth animations and transitions
✅ Floating elements with glow
✅ Touch-friendly mobile interface
✅ No external dependencies (pure HTML/CSS/JS)
✅ Semantic HTML5 structure
✅ CSS variables for easy customization
✅ Intersection Observer for animations
✅ Performance optimization

## Customization

### Change Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --aurora-cyan: #YOUR_COLOR;
    --aurora-green: #YOUR_COLOR;
    /* ... */
}
```

### Change Content
Edit `index.html`:
- Update site name
- Change section titles
- Modify descriptions
- Update WhatsApp number

### Add Images
Place images in `images/` folder and update paths in HTML.

## Credits Used
- **OpenRouter**: CSS generation (GPT-3.5-turbo)
- **Groq**: HTML generation (Mixtral-8x7b)

## No Dependencies
- Pure HTML5
- Pure CSS3
- Vanilla JavaScript (no frameworks)
- No npm packages required
- No build process needed

## Result
A complete, production-ready website that can be deployed to GitHub Pages or Render in minutes!
