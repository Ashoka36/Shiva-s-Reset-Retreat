# 📋 Installation & Deployment Guide

## Local Setup

### Prerequisites
- Git installed
- A text editor (VS Code, Sublime Text, etc.)
- A web browser

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ashoka36/aurora-retreat.git
cd aurora-retreat
```

### Step 2: Start Local Server
**Using Python 3:**
```bash
python3 -m http.server 8000
```

**Using Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

**Using Node.js (http-server):**
```bash
npx http-server
```

### Step 3: Open in Browser
Navigate to `http://localhost:8000`

---

## Customization Guide

### 1. Replace Logo

1. Prepare your logo image (recommended: 200x200px PNG or JPG)
2. Replace the `logo.jpg` file in the project root
3. Or update the src in `index.html`:
   ```html
   <img src="your-logo.png" alt="Logo">
   ```

### 2. Add Your Photos

#### Yoga/Meditation Section
Find this in `index.html`:
```html
<img src="https://via.placeholder.com/600x400/1a4d5c/7df9ff?text=Yoga+Session" 
     alt="Yoga Session" class="section-image">
```

Replace with:
```html
<img src="images/yoga.jpg" alt="Yoga Session" class="section-image">
```

#### Other Sections
- Restopub: `images/restopub.jpg`
- Bhajan: `images/bhajan.jpg`
- Pet Parents: `images/pets.jpg`
- Gallery: `images/gallery.jpg`

### 3. Update Text Content

Edit the text directly in `index.html`:
```html
<h2>Your New Title</h2>
<p>Your new description text</p>
```

### 4. Change Contact Information

Update the WhatsApp link:
```html
<a href="https://wa.me/YOUR_PHONE_NUMBER">Book Your Retreat</a>
```

Update phone number in footer:
```html
<p>or call YOUR_PHONE_NUMBER</p>
```

### 5. Customize Colors

Edit `:root` variables in `styles.css`:
```css
:root {
    --aurora-green: #00ff88;      /* Change green */
    --aurora-cyan: #7df9ff;       /* Change cyan */
    --aurora-purple: #ff00ff;     /* Change purple */
    --aurora-pink: #ff7fdb;       /* Change pink */
    --dark-bg: #0a0e27;           /* Change background */
}
```

---

## GitHub Pages Deployment

### Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name it: `aurora-retreat`
4. Choose "Private" for security
5. Click "Create repository"

### Step 2: Push Code to GitHub

```bash
cd aurora-retreat
git init
git add .
git commit -m "Initial commit: Aurora Borealis website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aurora-retreat.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to repository Settings
2. Scroll to "Pages" section
3. Under "Source", select "Deploy from a branch"
4. Select `main` branch
5. Click Save

### Step 4: Access Your Website

Your website will be live at:
```
https://YOUR_USERNAME.github.io/aurora-retreat/
```

---

## Custom Domain Setup (Optional)

### Step 1: Purchase Domain
- GoDaddy, Namecheap, or any domain registrar

### Step 2: Configure DNS

Add these DNS records:
```
Type: A
Name: @
Value: 185.199.108.153
       185.199.109.153
       185.199.110.153
       185.199.111.153
```

Or use CNAME:
```
Type: CNAME
Name: www
Value: YOUR_USERNAME.github.io
```

### Step 3: Add Domain to GitHub Pages

1. Go to repository Settings → Pages
2. Under "Custom domain", enter your domain
3. Click Save
4. Wait for DNS verification (5-15 minutes)

---

## File Organization

### Recommended Structure
```
aurora-retreat/
├── index.html
├── styles.css
├── script.js
├── logo.jpg
├── README.md
├── INSTALLATION.md
└── images/
    ├── yoga.jpg
    ├── restopub.jpg
    ├── bhajan.jpg
    ├── pets.jpg
    └── gallery.jpg
```

### Create Images Folder
```bash
mkdir images
# Copy your images here
```

---

## Troubleshooting

### Website Not Loading
- Check file paths are correct
- Ensure all files are in the same directory
- Clear browser cache (Ctrl+Shift+Delete)

### Images Not Showing
- Verify image file paths in HTML
- Check image file names match exactly
- Ensure images are in the correct folder

### Styles Not Applied
- Clear browser cache
- Check CSS file is in the same directory
- Verify `<link rel="stylesheet" href="styles.css">`

### Mobile Menu Not Working
- Check JavaScript file is loaded
- Open browser console (F12) for errors
- Verify `<script src="script.js"></script>` is at end of HTML

---

## Performance Optimization

### Image Optimization
1. Compress images before uploading
2. Use WebP format for better compression
3. Recommended sizes:
   - Logo: 200x200px
   - Section images: 600x400px
   - Gallery: 800x500px

### Lazy Loading (Optional)
Add to images:
```html
<img src="image.jpg" loading="lazy" alt="Description">
```

---

## SEO Optimization

### Update Meta Tags

In `index.html` `<head>`:
```html
<meta name="description" content="Your retreat description">
<meta name="keywords" content="yoga, retreat, wellness, goa">
<meta name="author" content="Shiva's Reset Retreat">
```

### Add Favicon
```html
<link rel="icon" type="image/x-icon" href="favicon.ico">
```

---

## Backup & Version Control

### Create Backup
```bash
git tag -a v1.0 -m "Version 1.0 - Initial release"
git push origin v1.0
```

### View History
```bash
git log --oneline
```

### Revert Changes
```bash
git revert COMMIT_HASH
```

---

## Support & Resources

- **GitHub Help**: https://docs.github.com/pages
- **HTML Reference**: https://developer.mozilla.org/en-US/docs/Web/HTML
- **CSS Reference**: https://developer.mozilla.org/en-US/docs/Web/CSS
- **JavaScript Guide**: https://developer.mozilla.org/en-US/docs/Web/JavaScript

---

## Next Steps

1. ✅ Customize with your content
2. ✅ Add your photos
3. ✅ Test on mobile devices
4. ✅ Deploy to GitHub Pages
5. ✅ Set up custom domain (optional)
6. ✅ Share with the world!

---

**Happy Building! 🌌✨**
