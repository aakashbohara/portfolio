"""
Portfolio Views
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import (
    ProfileSetting, SocialLink, SkillCategory, Skill, Service, ProjectCategory, Project,
    Experience, Education, Certification, Testimonial, BlogCategory, BlogPost,
    ContactMessage, NewsletterSubscriber
)
from .forms import ContactForm, NewsletterForm


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.filter(is_active=True, is_featured=True)[:8]
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        context['services'] = Service.objects.filter(is_active=True, is_featured=True)[:6]
        context['projects'] = Project.objects.filter(is_active=True, is_featured=True)[:6]
        context['project_categories'] = ProjectCategory.objects.all()
        context['experiences'] = Experience.objects.filter(is_active=True)[:3]
        context['testimonials'] = Testimonial.objects.filter(is_active=True, is_featured=True)[:6]
        context['blog_posts'] = BlogPost.objects.filter(is_published=True).order_by('-published_date')[:3]
        context['social_links'] = SocialLink.objects.filter(is_active=True)
        context['featured_links'] = SocialLink.objects.filter(is_active=True, is_featured=True)
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill_categories'] = SkillCategory.objects.prefetch_related(
            'skills'
        ).filter(skills__is_active=True).distinct()
        context['experiences'] = Experience.objects.filter(is_active=True)
        context['educations'] = Education.objects.filter(is_active=True)
        context['certifications'] = Certification.objects.filter(is_active=True)
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.filter(is_active=True)
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        context['current_category'] = self.request.GET.get('category', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(
            is_active=True,
            category=self.object.category
        ).exclude(pk=self.object.pk)[:3]
        return context


class ServiceListView(ListView):
    model = Service
    template_name = 'core/services.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'core/service_detail.html'
    context_object_name = 'service'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class BlogListView(ListView):
    model = BlogPost
    template_name = 'core/blog.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True)
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('search')
        
        if category:
            queryset = queryset.filter(category__slug=category)
        if tag:
            queryset = queryset.filter(tags__slug=tag)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['featured_posts'] = BlogPost.objects.filter(is_published=True, is_featured=True)[:3]
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'core/blog_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = BlogPost.objects.filter(
            is_published=True,
            category=self.object.category
        ).exclude(pk=self.object.pk)[:3]
        return context


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for your message! I will get back to you soon.')
        return super().form_valid(form)


class ResumeView(TemplateView):
    template_name = 'core/resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.filter(is_active=True)
        context['educations'] = Education.objects.filter(is_active=True)
        context['certifications'] = Certification.objects.filter(is_active=True)
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        return context


def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'success': True, 'message': 'Successfully subscribed!'})
            else:
                return JsonResponse({'success': False, 'message': 'You are already subscribed.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})
