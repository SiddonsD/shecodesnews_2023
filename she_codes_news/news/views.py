from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryFrom
# from .forms import StoryFrom, Comment


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryFrom
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# class AddCommentView(generic.CreateView):
#     form_class = Comment

#     def get(self, request, *args, **kwargs):
#         return ("news:story", pk==self.kwargs.get("pk"))
    
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         pk = self.kwargs.get("pk")
#         form.instance.story = get_object_or_404(NewsStory, pk=pk)
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")})
