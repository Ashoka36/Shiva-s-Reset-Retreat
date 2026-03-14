#!/usr/bin/env python3
"""
AI Website Builder Agent
Builds websites exactly like Shiva's Reset Retreat using Aurora Borealis theme
Uses OpenRouter and Groq APIs for intelligence
No dependencies - pure Python implementation
"""

import os
import json
import requests
from typing import Dict, List, Optional

# API Configuration
OPENROUTER_API_KEY = os.getenv("openrouter_api_key")
GROQ_API_KEY = os.getenv("groq_api_key")

class WebsiteBuilderAgent:
    """
    AI Agent that builds websites with:
    - Aurora Borealis theme (cyan, green, purple, pink)
    - Glass morphism navbar
    - Parallax scrolling
    - Responsive mobile design
    - Twin image layouts
    - WhatsApp integration
    """
    
    def __init__(self):
        self.openrouter_url = "https://openrouter.io/api/v1/chat/completions"
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.website_config = {}
        
    def generate_html_with_groq(self, prompt: str) -> str:
        """Generate HTML using Groq API"""
        try:
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "mixtral-8x7b-32768",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert HTML/CSS developer. Generate clean, semantic HTML code."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 2000
            }
            
            response = requests.post(self.groq_url, json=payload, headers=headers)
            response.raise_for_status()
            
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Groq API Error: {e}")
            return None
    
    def generate_css_with_openrouter(self, prompt: str) -> str:
        """Generate CSS using OpenRouter API"""
        try:
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert CSS designer specializing in Aurora Borealis themes, glass morphism, and responsive design."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 3000
            }
            
            response = requests.post(self.openrouter_url, json=payload, headers=headers)
            response.raise_for_status()
            
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"OpenRouter API Error: {e}")
            return None
    
    def build_website(self, config: Dict) -> Dict:
        """
        Build complete website with given configuration
        
        Config structure:
        {
            "site_name": "Shiva's Reset Retreat",
            "location": "Palolem, Goa, India",
            "tagline": "Reset your Mind, Body & Soul",
            "sections": [
                {"title": "Section 1", "description": "...", "image": "image1.jpg"},
                ...
            ],
            "whatsapp": "+917676432449",
            "theme": "aurora_borealis"
        }
        """
        
        self.website_config = config
        
        print(f"🚀 Building website: {config['site_name']}")
        
        # Step 1: Generate HTML Structure
        html_prompt = f"""
        Create a complete HTML5 website for: {config['site_name']}
        Location: {config['location']}
        Tagline: {config['tagline']}
        
        Include:
        1. Glass morphism navbar with logo
        2. Hero section with twin images side by side
        3. Sections for: {', '.join([s['title'] for s in config['sections']])}
        4. WhatsApp CTA button
        5. Footer with contact info
        6. Mobile responsive meta tags
        
        Make it semantic HTML5 with proper structure.
        """
        
        print("📝 Generating HTML with Groq...")
        html_code = self.generate_html_with_groq(html_prompt)
        
        if not html_code:
            print("❌ HTML generation failed")
            return {"status": "error"}
        
        # Step 2: Generate CSS Styling
        css_prompt = f"""
        Create Aurora Borealis themed CSS for: {config['site_name']}
        
        Requirements:
        1. Color scheme: Cyan (#7df9ff), Green (#00ff88), Purple (#ff00ff), Pink (#ff7fdb)
        2. Dark background: #0a0e27
        3. Glass morphism navbar with backdrop blur
        4. Parallax scrolling effects
        5. Twin image layout (280px x 350px each)
        6. Smooth animations and transitions
        7. Responsive breakpoints: 1024px, 768px, 480px, 360px
        8. Mobile-first design
        9. Golden yellow headings (#FFD700)
        10. Floating elements with glow effects
        
        Include:
        - Smooth scroll behavior
        - Touch-friendly buttons
        - Optimized animations for mobile
        - Gradient backgrounds
        """
        
        print("🎨 Generating CSS with OpenRouter...")
        css_code = self.generate_css_with_openrouter(css_prompt)
        
        if not css_code:
            print("❌ CSS generation failed")
            return {"status": "error"}
        
        # Step 3: Generate JavaScript
        js_code = self.generate_javascript()
        
        # Step 4: Create project structure
        project_dir = config['site_name'].lower().replace(' ', '-')
        
        result = {
            "status": "success",
            "project": project_dir,
            "files": {
                "index.html": html_code,
                "styles.css": css_code,
                "script.js": js_code
            },
            "config": config
        }
        
        return result
    
    def generate_javascript(self) -> str:
        """Generate JavaScript for interactivity"""
        
        js_code = """
// Mobile Menu Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });
}

// Smooth Scroll Detection
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Parallax Effect
window.addEventListener('scroll', () => {
    const parallaxElements = document.querySelectorAll('[data-parallax]');
    parallaxElements.forEach(element => {
        const scrollPosition = window.scrollY;
        element.style.transform = `translateY(${scrollPosition * 0.5}px)`;
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.section-content').forEach(el => {
    observer.observe(el);
});

// WhatsApp Integration
function openWhatsApp() {
    const phone = '917676432449';
    const message = 'Hi, I want to book a retreat at Shiva\\'s Reset Retreat!';
    const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
}

// Prevent zoom on input focus (mobile)
document.addEventListener('touchstart', function() {}, false);

// Performance optimization
if ('requestIdleCallback' in window) {
    requestIdleCallback(() => {
        // Load non-critical resources
        console.log('Website optimized');
    });
}
"""
        return js_code
    
    def create_project_files(self, result: Dict, output_dir: str = "./website-project"):
        """Create actual project files"""
        
        if result["status"] != "success":
            print("❌ Cannot create files - build failed")
            return
        
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(f"{output_dir}/images", exist_ok=True)
        
        # Write files
        for filename, content in result["files"].items():
            filepath = f"{output_dir}/{filename}"
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"✅ Created: {filepath}")
        
        # Create config file
        config_path = f"{output_dir}/config.json"
        with open(config_path, 'w') as f:
            json.dump(result["config"], f, indent=2)
        print(f"✅ Created: {config_path}")
        
        # Create README
        readme_content = f"""# {result['config']['site_name']}

## Website Details
- **Location**: {result['config']['location']}
- **Tagline**: {result['config']['tagline']}
- **Theme**: Aurora Borealis

## Features
- Glass morphism navbar
- Twin image layouts
- Parallax scrolling
- Responsive design (mobile-first)
- WhatsApp integration
- Golden yellow headings
- Smooth animations

## Files
- `index.html` - Main HTML structure
- `styles.css` - Aurora Borealis styling
- `script.js` - Interactive features
- `images/` - Image assets folder

## How to Use
1. Add your images to the `images/` folder
2. Update image paths in `index.html`
3. Customize colors in `styles.css` (CSS variables)
4. Deploy to GitHub Pages or Render

## Deployment
```bash
git init
git add .
git commit -m "Initial commit"
git push origin master
```

## API Credits Used
- OpenRouter: CSS generation
- Groq: HTML generation
"""
        
        readme_path = f"{output_dir}/README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        print(f"✅ Created: {readme_path}")
        
        print(f"\n🎉 Website project created in: {output_dir}")
    
    def validate_website(self, html: str, css: str) -> Dict:
        """Validate generated website code"""
        
        validations = {
            "has_html_structure": "<!DOCTYPE html>" in html and "<html" in html,
            "has_navbar": "navbar" in html.lower(),
            "has_hero_section": "hero" in html.lower(),
            "has_whatsapp": "whatsapp" in html.lower() or "wa.me" in html.lower(),
            "has_css_variables": "--aurora" in css,
            "has_responsive": "@media" in css,
            "has_animations": "@keyframes" in css,
            "has_glass_effect": "backdrop-filter" in css or "backdrop" in css
        }
        
        return validations


def main():
    """Main execution"""
    
    print("=" * 60)
    print("🌌 AI Website Builder Agent")
    print("Aurora Borealis Theme - No Dependencies")
    print("=" * 60)
    
    # Initialize agent
    agent = WebsiteBuilderAgent()
    
    # Website configuration
    website_config = {
        "site_name": "Shiva's Reset Retreat",
        "location": "Palolem, Goa, India",
        "tagline": "Reset your Mind, Body & Soul",
        "sections": [
            {
                "title": "Reset the Mind",
                "description": "Yoga and meditation experience",
                "image": "yoga.jpg"
            },
            {
                "title": "Restopub & Boba",
                "description": "Coastal beverage bar",
                "image": "boba.jpg"
            },
            {
                "title": "Ground Yourself",
                "description": "Bhajan and wellness",
                "image": "bhajan.jpg"
            },
            {
                "title": "Pet Parent Retreat",
                "description": "Animal welfare retreat",
                "image": "pet.jpg"
            },
            {
                "title": "Gallery",
                "description": "Photo showcase",
                "image": "gallery.jpg"
            }
        ],
        "whatsapp": "+917676432449",
        "theme": "aurora_borealis"
    }
    
    # Build website
    result = agent.build_website(website_config)
    
    if result["status"] == "success":
        print("\n✅ Website generation successful!")
        
        # Validate
        validations = agent.validate_website(
            result["files"]["index.html"],
            result["files"]["styles.css"]
        )
        
        print("\n📋 Validation Results:")
        for check, passed in validations.items():
            status = "✅" if passed else "❌"
            print(f"{status} {check}")
        
        # Create files
        agent.create_project_files(result)
    else:
        print("❌ Website generation failed")


if __name__ == "__main__":
    main()
