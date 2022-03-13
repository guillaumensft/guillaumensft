from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import Article, UserProfile, Category


class UserProfileDetailView(ListView):
    template_name = 'blog/user_detail.html'
    model = UserProfile


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class ArticleCreateView(CreateView):
    template_name = 'blog/post_form.html'
    model = Article
    fields = ['titre', 'excerpt', 'content']


class ArticleUpdateView(UpdateView):
    template_name = 'blog/post_update.html'
    model = Article
    fields = '__all__'


def DeleteArticle(request, *args, **kwargs):

    context = {}

    qs = Article.objects.get(id=kwargs['id'])
    qs.delete()

    context['message'] = f"nous avons bien supprimer l'article {qs.id}"

    return render(request, 'blog/article_list.html', context)


'''from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request, 'form_template.html', {'form': form})'''

