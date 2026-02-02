# 🚀 Professional Bento Portfolio & Blog - Django

A stunning, "top-notch" portfolio website with a **Modern Bento Grid Homepage**, **Glassmorphic Design**, and elite-level **SEO & Speed** optimizations. Built with Django and powered by a beautiful visual admin experience.

**Powered by [Master Junction](https://masterjunction.com.np)**

---

## ✨ Features

### 🎨 Design & UI
- **Modern Bento Grid Homepage** - Interactive, card-based layout for high impact.
- **Glassmorphic UI** - Professional frosted glass effects and fluid transitions.
- **Micro-Animations** - Premium hover-state transformations and typing effects.
- **Dynamic Logo Upload** - Instantly brand your site from the admin panel.
- **Fully Responsive** - Flawless experience on Mobile, Tablet, and Desktop.

### 🔍 Elite SEO Suite
- **Social Cards (OG/Twitter)** - Beautiful previews when sharing on Facebook, LinkedIn, or Twitter.
- **JSON-LD Structured Data** - Schema.org `BlogPosting` support for rich search results.
- **Dynamic Sitemaps** - Automatically generated `sitemap.xml` for all content.
- **Robots.txt** - Proper guidance for search engine crawlers.
- **Canonical URLs** - Advanced tag management to protect SEO authority.

### ⚡ Performance & Optimization
- **Whitenoise Integration** - Compressed and cached static file serving for maximum speed.
- **Native Lazy Loading** - Optimized image delivery (`loading="lazy"`) across all pages.
- **GZip Compression** - Encoded responses for reduced bandwidth and faster load times.
- **NPR Currency Support** - Optimized pricing suggestions for the Nepalese market.

### 🔒 Security Hardening
- **Environment Variables** - Secure configuration management via `.env`.
- **Production Headers** - HSTS (1-year), XSS Filter, and Content Type Sniffing protection.
- **Site Integrity Protection** - Built-in `SiteIntegrityMiddleware` to safeguard codebase value.

### 🔧 Modern Admin Experience
- **Unfold Admin** - A state-of-the-art, beautiful administrative dashboard.
- **Visual Icon Picker** - Grid-based icon selection for Services, Skills, and Social Links.
- **Complete CMS** - Manage Blog, Projects, Work History, Education, and Testimonials.

---

## 🎨 Theme Customization

### From Admin Panel:
1. Go to **Admin → Profile Settings**
2. Find **🎨 Theme Settings** section
3. Choose **Theme Mode**: Gradient or Solid
4. **Logo**: Upload a custom logo to replace textual branding in the navbar.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone/Navigate to project
cd portfolio_site

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup Environment
cp .env.example .env  # Or create a .env file with your SECRET_KEY

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Start the "Top-Notch" experience
python manage.py runserver
```

### Access
- **Website**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 🌐 Deployment

### For Production:
1. **Set DEBUG=False** in your `.env` file.
2. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```
3. **Whitenoise** will automatically handle high-performance serving.
4. **Use gunicorn**:
   ```bash
   gunicorn portfolio_site.wsgi:application
   ```

---

## ⚠️ Important Notice

**Please do not remove the "Powered by Master Junction" credit in the footer.**

The `SiteIntegrityMiddleware` is active to ensure the developer credit is maintained. Removing this credit without authorization may lead to site instability in production. 

---

## 📞 Support

For support, customization, or feature requests:
- Website: [masterjunction.com.np](https://masterjunction.com.np)
- Email: Contact through website

---

**Built with ❤️ by [Master Junction](https://masterjunction.com.np)**
