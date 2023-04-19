from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from home.forms import HomeForm
from home.models import Post1,Friend
from TTU_SYSTEM.models import CustomUser

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get(self, request):
        form = HomeForm()
        posts = Post1.objects.order_by('-created')
        users = CustomUser.objects.exclude(id=request.user.id)
        context = {'form':form,'posts':posts,'users':users}
        return render (request,self.template_name,context)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            form = HomeForm()
            return redirect('home:home')                       

        context = {'form':form}
        return render (request,self.template_name,context)

def add_friend(request,operation,pk):
    friend = CustomUser.objects.get(pk=pk)
    if operation =='add':
        Friend.make_friend(request.user,friend)
    elif operation =='remove':
        Friend.lose_friend(request.user,friend)
    return redirect('home:home')