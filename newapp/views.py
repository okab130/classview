from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Company,Company2,Books,Post
from .forms import BookForm,TestForm


class IndexView(TemplateView):
    template_name ='newapp/index.html'
    def get_context_data(self, **kwargs):
        print("get CONTEXT関数")
        context = super().get_context_data(**kwargs)
        queryset = Company.objects.all()
        context['name1'] = queryset
        sql='select * from newapp_company2'
        queryset = Company2.objects.raw(sql)
        context['name2'] = queryset
        context['XXX'] = "あああああああああああああああああああああ"
        context['YYY'] = "いいいいいいいいいいいいいいいいいいいいいいいい"
    #    context['name1'] = queryset[0].name
    #    context['name2'] = queryset[0].memo
    #    context['name3'] = queryset[1].name
    #    context['name4'] = queryset[1].memo
        return context
    
#    def get(self,request,**kwargs):
#        print("get関数")
#        queryset = Company.objects.all()
#        context = {
#            'name': queryset,
#        }
#        #context = {
#        #    'name1': queryset[0].name,
#        #    'name2': queryset[0].memo
#        #}
#        return self.render_to_response(context)
class BookFormView(FormView):
    
    template_name = 'newapp/form_book.html'
    form_class = BookForm
    success_url = reverse_lazy('store:book_form')

    def get_initial(self):
        initial = super(BookFormView, self).get_initial()
        initial['name'] = 'form sample'
        print("init中")
        return initial

    def form_valid(self, form):
        print("valid中")
        if form.is_valid():
            print("valid　OK")
            form.save()
        return super(BookFormView, self).form_valid(form)

class TestView(FormView):
    template_name = 'newapp/index2.html'
    form_class = TestForm
    success_url = reverse_lazy('store:index2')
    def form_valid(self, form):
        form.save()  # 保存処理など
        messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        return super().form_valid(form)

def listfunc(request):
    posts = Post.objects.all()
    return render(request, 'newapp/list2.html', {'posts': posts})

def detailfunc(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'newapp/detail2.html', {'post': post})



