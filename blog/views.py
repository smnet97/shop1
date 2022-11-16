from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogModel, TagsModel, CommentsModel
from .forms import CommentForm


class CommentsView(CreateView):
    model = CommentsModel
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={"pk": self.kwargs.get('pk')})


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'main/blog-details.html'

    def get_context_data(self, **kwargs):
        data = super(BlogDetailView, self).get_context_data(**kwargs)
        data['comments'] = CommentsModel.objects.all().filter(blog=self.kwargs.get('pk')).order_by('-id')
        return data

class BlogListView(ListView):
    template_name = 'main/blog.html'

    def get_queryset(self):
        qs = BlogModel.objects.all()
        tag = self.request.GET.get('tag', '')
        if tag and tag.isdigit():
            tmp = TagsModel.objects.all().filter(id=tag).exists()
            if tmp:
                qs = qs.filter(tags=tag)

        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        tag = self.request.GET.get('tag', '')
        if tag and tag.isdigit():
            tmp = TagsModel.objects.all().filter(id=tag).exists()
            if tmp:
                data['tag'] = TagsModel.objects.get(id=tag)

        return data
