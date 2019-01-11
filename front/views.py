from django.shortcuts import render
from .models import Alticle
from django.http import HttpResponse
from django.views.generic import ListView

def add_article(request):
    articles = []
    for x in range(0,102):
        article = Alticle(title='标题:%s'%x,content='内容:%s'%x)
        articles.append(article)
    Alticle.objects.bulk_create(articles)
    return HttpResponse('article add success')

class ArticleListView(ListView):
    model = Alticle
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'creat_time'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'xxxxx'

        paginator = context.get('paginator')
        page_obj = context.get('page_obj')

        pagination_data = self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)

        return context

    # def get_queryset(self):
    #     return Alticle.objects.filter(id__lte=20)

    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1,current_page)
        else:
            left_has_more = True
            left_pages = range(current_page-around_count,current_page)

        if current_page >= num_pages - around_count -1:
            right_pages = range(current_page+1,num_pages+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1,current_page+around_count+1)

        return {
            'current_page': current_page,
            'left_pages': left_pages,
            'right_pages': right_pages,
            'num_pages': num_pages,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }









