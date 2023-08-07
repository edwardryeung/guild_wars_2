from . import models, forms
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import F
from django.http import HttpResponseRedirect
# Create your views here.


class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_posts = models.Post.objects.published().order_by('-published')[:3]

        context.update({'latest_posts': latest_posts})

        return context


class AboutView(TemplateView):
    template_name = 'blog/about.html'


def terms_and_conditions(request):
    return render(request, 'blog/terms_and_conditions.html')


class PostListView(ListView):
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')


class TopicListView(ListView):
    model = models.Topic
    context_object_name = 'topics'
    queryset = models.Topic.objects.order_by('name')


class CommentListView(ListView):
    model = models.Comment
    context_object_name = 'comments'
    queryset = models.Comment.objects.order_by('-created')


class CommentDetailView(DetailView):
    model = models.Comment


def comment_like(request, pk):
    if request.method == 'POST':
        likedcomment = models.Comment.objects.get(pk=pk)
        likedcomment.likes = F('likes') + 1
        likedcomment.save()
        # return HttpResponseRedirect(reverse('post-detail', args=[str(likedcomment.post_id)]))


def comment_dislike(request, pk):
    if request.method == 'POST':
        dislikedcomment = models.Comment.objects.get(pk=pk)
        dislikedcomment.dislikes = F('dislikes') + 1
        dislikedcomment.save()
        # return HttpResponseRedirect(reverse('post-detail', args=[str(dislikedcomment.post_id)]))


class PostDetailView(DetailView):
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset().published()

        if 'pk' in self.kwargs:
            return queryset

        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.get_object().comments.all
        return context


class TopicDetailView(DetailView):
    model = models.Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = self.get_object()
        context['posts'] = models.Post.objects.published().order_by('-published')
        return context


def form_example(request):
    if request.method == 'POST':
        form = forms.ExampleSignupForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data

            return render(
                request,
                'blog/form_example_success.html',
                context={'data': cleaned_data}
            )

    else:
        form = forms.ExampleSignupForm()

    return render(request, 'blog/form_example.html', context={'form': form})


class FormViewExample(FormView):
    template_name = 'blog/form_example.html'
    form_class = forms.ExampleSignupForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for signing up!'
        )
        return super().form_valid(form)


class ContactFormView(CreateView):
    model = models.Contact
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'message',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )
        return super().form_valid(form)


class PhotoContestSubmissionFormView(CreateView):
    model = models.PhotoContestSubmission
    template_name = 'blog/contest_form.html'
    success_url = reverse_lazy('home')
    fields = [
        'first_name',
        'last_name',
        'email',
        'photo',
    ]

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your photo submission has been received.'
        )
        return super().form_valid(form)
