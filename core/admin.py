"""
Portfolio Admin Configuration
With Theme Customization
"""

from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from .models import (
    ProfileSetting, SocialLink, SkillCategory, Skill, Service, ProjectCategory, Project, ProjectImage,
    Experience, Education, Certification, Testimonial, BlogCategory, BlogTag, BlogPost,
    ContactMessage, NewsletterSubscriber
)


@admin.register(ProfileSetting)
class ProfileSettingAdmin(ModelAdmin):
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'title', 'subtitle', 'typing_texts', 'profile_image', 'logo', 'cover_image', 'resume')
        }),
        ('Bio', {
            'fields': ('bio_short', 'bio_full')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'whatsapp', 'location')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter', 'instagram', 'youtube', 'dribbble', 'behance', 'medium', 'dev_to', 'facebook', 'tiktok', 'website'),
            'classes': ('collapse',)
        }),
        ('Statistics', {
            'fields': ('years_experience', 'projects_completed', 'happy_clients', 'awards_won')
        }),
        ('Availability', {
            'fields': ('is_available_for_hire', 'availability_status')
        }),
        ('🎨 Theme Settings', {
            'fields': ('theme_mode',),
            'description': 'Choose your theme mode - gradient or solid colors'
        }),
        ('🌈 Gradient Theme', {
            'fields': ('gradient_preset', 'custom_gradient_start', 'custom_gradient_end'),
            'description': 'Select a preset or create custom gradient',
            'classes': ('collapse',)
        }),
        ('🎨 Solid Color Theme', {
            'fields': ('solid_color_preset', 'custom_solid_color'),
            'description': 'Select a preset or use custom color',
            'classes': ('collapse',)
        }),
        ('✨ Accent & Background', {
            'fields': ('accent_color', 'bg_dark', 'bg_card'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords', 'google_analytics_id'),
            'classes': ('collapse',)
        }),
        ('Footer', {
            'fields': ('footer_text',),
        }),
    )

    def has_add_permission(self, request):
        return not ProfileSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):
    list_display = ('title', 'url', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    list_filter = ('is_featured', 'is_active')
    search_fields = ('title', 'url')

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }


@admin.register(SkillCategory)
class SkillCategoryAdmin(ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'is_featured', 'is_active', 'order')
    list_editable = ('proficiency', 'is_featured', 'is_active', 'order')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('name',)

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('title', 'price_starting', 'is_featured', 'is_active', 'order')
    list_editable = ('is_featured', 'is_active', 'order')
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }


class ProjectImageInline(TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'order')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'category', 'client', 'project_date', 'is_featured', 'is_active', 'thumbnail_preview')
    list_filter = ('category', 'is_featured', 'is_active')
    search_fields = ('title', 'client', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category')
        }),
        ('Media', {
            'fields': ('thumbnail', 'featured_image')
        }),
        ('Content', {
            'fields': ('short_description', 'description')
        }),
        ('Project Details', {
            'fields': ('client', 'project_date', 'project_url', 'github_url', 'technologies')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="60" height="40" style="object-fit:cover;border-radius:4px;"/>', obj.thumbnail.url)
        return "-"
    thumbnail_preview.short_description = "Thumbnail"


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'is_current', 'is_active')
    list_filter = ('is_current', 'is_active')
    search_fields = ('job_title', 'company')


@admin.register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('degree', 'institution')


@admin.register(Certification)
class CertificationAdmin(ModelAdmin):
    list_display = ('name', 'issuing_organization', 'issue_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'issuing_organization')


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active')
    list_filter = ('is_featured', 'is_active', 'rating')


@admin.register(BlogCategory)
class BlogCategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogTag)
class BlogTagAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'category', 'published_date', 'views', 'is_featured', 'is_published', 'image_preview')
    list_editable = ('is_featured', 'is_published')
    list_filter = ('category', 'is_featured', 'is_published', 'tags')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    date_hierarchy = 'published_date'

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="80" height="50" style="object-fit:cover;border-radius:4px;"/>', obj.featured_image.url)
        return "-"
    image_preview.short_description = "Image"


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read', 'is_replied')
    list_editable = ('is_read', 'is_replied')
    list_filter = ('is_read', 'is_replied')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'budget', 'project_type', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('email',)
