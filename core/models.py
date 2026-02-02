"""
Professional Portfolio - Data Models
Complete models for portfolio, blog, and professional profile
With Theme Customization Support
"""

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from fontawesome_6.fields import IconField


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Theme Color Choices
GRADIENT_CHOICES = [
    ('purple-blue', 'Purple to Blue (#667eea → #764ba2)'),
    ('cyan-blue', 'Cyan to Blue (#4facfe → #00f2fe)'),
    ('pink-orange', 'Pink to Orange (#f093fb → #f5576c)'),
    ('green-teal', 'Green to Teal (#11998e → #38ef7d)'),
    ('orange-red', 'Orange to Red (#ff512f → #f09819)'),
    ('blue-purple', 'Blue to Purple (#667eea → #764ba2)'),
    ('pink-purple', 'Pink to Purple (#f953c6 → #b91d73)'),
    ('gold-orange', 'Gold to Orange (#f7971e → #ffd200)'),
    ('teal-green', 'Teal to Green (#00b09b → #96c93d)'),
    ('red-pink', 'Red to Pink (#ed213a → #93291e)'),
    ('ocean', 'Ocean Blue (#2193b0 → #6dd5ed)'),
    ('sunset', 'Sunset (#ff7e5f → #feb47b)'),
    ('custom', 'Custom Gradient'),
]

SOLID_COLOR_CHOICES = [
    ('#667eea', 'Purple'),
    ('#4facfe', 'Cyan'),
    ('#f093fb', 'Pink'),
    ('#11998e', 'Teal'),
    ('#ff512f', 'Orange'),
    ('#f953c6', 'Magenta'),
    ('#f7971e', 'Gold'),
    ('#ed213a', 'Red'),
    ('#2193b0', 'Ocean'),
    ('#00b09b', 'Green'),
    ('custom', 'Custom Color'),
]




class ProfileSetting(models.Model):
    """Personal/Professional profile settings - Singleton"""
    # Personal Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., Full Stack Developer")
    subtitle = models.CharField(max_length=300, blank=True, help_text="Tagline or short intro")
    typing_texts = models.CharField(max_length=500, blank=True, default="Developer,Designer,Creator", help_text="Comma-separated texts for typing animation")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    logo = models.ImageField(upload_to='profile/logo/', blank=True, null=True, help_text="Upload a logo to replace the text name in navbar")
    cover_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    
    # Bio
    bio_short = models.TextField(help_text="Short bio for homepage (2-3 sentences)")
    bio_full = RichTextUploadingField(blank=True, help_text="Full bio for about page")
    
    # Contact Info
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True, help_text="With country code, no + sign")
    location = models.CharField(max_length=200, blank=True)
    
    # Social Links
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    dribbble = models.URLField(blank=True)
    behance = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    dev_to = models.URLField(blank=True, verbose_name="Dev.to")
    facebook = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    website = models.URLField(blank=True)
    
    # Professional Stats
    years_experience = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    happy_clients = models.PositiveIntegerField(default=0)
    awards_won = models.PositiveIntegerField(default=0)
    
    # Availability
    is_available_for_hire = models.BooleanField(default=True)
    availability_status = models.CharField(max_length=100, blank=True, default="Available for Work", help_text="e.g., Available for freelance")
    
    # ========== THEME SETTINGS ==========
    # Theme Mode
    theme_mode = models.CharField(max_length=20, choices=[
        ('gradient', 'Gradient Colors'),
        ('solid', 'Solid Colors'),
    ], default='gradient', help_text="Choose between gradient or solid color theme")
    
    # Gradient Theme
    gradient_preset = models.CharField(max_length=50, choices=GRADIENT_CHOICES, default='purple-blue', help_text="Select a gradient preset")
    custom_gradient_start = models.CharField(max_length=7, blank=True, default='#667eea', help_text="Start color (hex) for custom gradient")
    custom_gradient_end = models.CharField(max_length=7, blank=True, default='#764ba2', help_text="End color (hex) for custom gradient")
    
    # Solid Color Theme
    solid_color_preset = models.CharField(max_length=20, choices=SOLID_COLOR_CHOICES, default='#667eea', blank=True)
    custom_solid_color = models.CharField(max_length=7, blank=True, default='#667eea', help_text="Custom solid color (hex)")
    
    # Accent Color
    accent_color = models.CharField(max_length=7, default='#00f2fe', help_text="Accent color for highlights (hex)")
    
    # Background
    bg_dark = models.CharField(max_length=7, default='#0f172a', help_text="Main background color")
    bg_card = models.CharField(max_length=7, default='#1e293b', help_text="Card/glass background color")
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # Analytics
    google_analytics_id = models.CharField(max_length=50, blank=True)
    
    # Footer - IMPORTANT: Do not remove Master Junction credit
    footer_text = models.CharField(max_length=200, blank=True)
    show_powered_by = models.BooleanField(default=True, help_text="⚠️ Please keep this enabled to support the developers")

    class Meta:
        verbose_name = "Profile Setting"
        verbose_name_plural = "Profile Settings"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def typing_texts_list(self):
        return [t.strip() for t in self.typing_texts.split(',') if t.strip()]

    def get_primary_gradient(self):
        """Returns the primary gradient colors"""
        gradients = {
            'purple-blue': ('#667eea', '#764ba2'),
            'cyan-blue': ('#4facfe', '#00f2fe'),
            'pink-orange': ('#f093fb', '#f5576c'),
            'green-teal': ('#11998e', '#38ef7d'),
            'orange-red': ('#ff512f', '#f09819'),
            'blue-purple': ('#667eea', '#764ba2'),
            'pink-purple': ('#f953c6', '#b91d73'),
            'gold-orange': ('#f7971e', '#ffd200'),
            'teal-green': ('#00b09b', '#96c93d'),
            'red-pink': ('#ed213a', '#93291e'),
            'ocean': ('#2193b0', '#6dd5ed'),
            'sunset': ('#ff7e5f', '#feb47b'),
        }
        if self.gradient_preset == 'custom':
            return (self.custom_gradient_start, self.custom_gradient_end)
        return gradients.get(self.gradient_preset, ('#667eea', '#764ba2'))

    def get_primary_color(self):
        """Returns the primary solid color"""
        if self.solid_color_preset == 'custom':
            return self.custom_solid_color
        return self.solid_color_preset

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_profile(cls):
        obj, created = cls.objects.get_or_create(pk=1, defaults={
            'first_name': 'John',
            'last_name': 'Doe',
            'title': 'Full Stack Developer',
            'email': 'hello@example.com',
            'bio_short': 'I am a passionate developer creating amazing digital experiences.',
        })
        return obj


class SocialLink(TimeStampedModel):
    """Custom social/link tree links"""
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon = IconField(blank=True)
    description = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, help_text="Show prominently on homepage")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Link / Social"
        verbose_name_plural = "Links / Socials"

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    """Skill categories"""
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(TimeStampedModel):
    """Technical and soft skills"""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    icon = IconField(blank=True)
    proficiency = models.PositiveIntegerField(default=80, help_text="0-100 percentage")
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    """Services offered"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icon = IconField(blank=True)
    short_description = models.TextField()
    description = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    price_starting = models.CharField(max_length=50, blank=True, help_text="e.g., Rs. 5000")
    
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})


class ProjectCategory(models.Model):
    """Project categories for filtering"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(TimeStampedModel):
    """Portfolio projects"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, related_name='projects')
    
    # Media
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    
    # Content
    short_description = models.TextField()
    description = RichTextUploadingField()
    
    # Project Details
    client = models.CharField(max_length=200, blank=True)
    project_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True, help_text="Live project URL")
    github_url = models.URLField(blank=True)
    
    # Technologies
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated technologies")
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-project_date', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class ProjectImage(models.Model):
    """Additional images for projects"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class Experience(TimeStampedModel):
    """Work experience"""
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_url = models.URLField(blank=True)
    company_logo = models.ImageField(upload_to='experience/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    
    description = RichTextUploadingField()
    
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Education(TimeStampedModel):
    """Education history"""
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    institution = models.CharField(max_length=200)
    institution_logo = models.ImageField(upload_to='education/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    
    grade = models.CharField(max_length=50, blank=True, help_text="e.g., 3.8 GPA, First Class")
    description = models.TextField(blank=True)
    
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(TimeStampedModel):
    """Professional certifications"""
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    organization_logo = models.ImageField(upload_to='certifications/', blank=True, null=True)
    
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    
    description = models.TextField(blank=True)
    
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"


class Testimonial(TimeStampedModel):
    """Client testimonials"""
    client_name = models.CharField(max_length=200)
    client_title = models.CharField(max_length=200, blank=True, help_text="e.g., CEO at Company")
    client_photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    client_company = models.CharField(max_length=200, blank=True)
    
    content = models.TextField()
    rating = models.PositiveIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.client_company}"


class BlogCategory(models.Model):
    """Blog categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogTag(models.Model):
    """Blog tags"""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogPost(TimeStampedModel):
    """Blog posts"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(BlogTag, blank=True, related_name='posts')
    
    # Media
    featured_image = models.ImageField(upload_to='blog/')
    
    # Content
    excerpt = models.TextField(help_text="Short summary for cards")
    content = RichTextUploadingField()
    
    # SEO
    meta_title = models.CharField(max_length=60, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    
    # Publishing
    published_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    # Stats
    views = models.PositiveIntegerField(default=0)
    reading_time = models.PositiveIntegerField(default=5, help_text="Minutes to read")

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class ContactMessage(TimeStampedModel):
    """Contact form submissions"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    # For project inquiries
    budget = models.CharField(max_length=100, blank=True)
    project_type = models.CharField(max_length=100, blank=True)
    
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"


class NewsletterSubscriber(TimeStampedModel):
    """Newsletter subscribers"""
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"

    def __str__(self):
        return self.email
