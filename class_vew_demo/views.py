from django.http import HttpResponse
from django.views.generic import View,TemplateView
from django.shortcuts import render

def index(request):

    return HttpResponse('index')

class BookListView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('book list view')

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_book.html')
    def post(self,request,*args,**kwargs):
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print('name:{} \nauthor:{}'.format(book_name,book_author))
        return HttpResponse('success')

class BookDetailView(View):
    def get(self,request,book_id):
        print('图书ID是%s'%book_id)
        return HttpResponse('detail')

    #总会先调用这个方法
    def dispatch(self, request, *args, **kwargs):
        print("dispatch")
        return super(BookDetailView,self).dispatch(request,*args,**kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持post请求")

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {'phone':'123456'}
        return  context







