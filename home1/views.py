from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from home1.forms import HomeForm1
from home1.models import Post,Friends
from TTU_SYSTEM.models import CustomUser

# Create your views here.
class HomeView1(TemplateView):
    template_name = 'home1/home1.html'

    def get(self, request):
        form = HomeForm1()
        posts = Post.objects.order_by('-created')
        users = CustomUser.objects.exclude(id=request.user.id)
        friend = Friends.objects.get(current_user=request.user)
        friends = friend.users.all()
        
        context = {'form':form,'posts':posts,'users':users,'friends':friends}
        return render(request,self.template_name,context)

    def post(self, request):
        form = HomeForm1(request.POST)
        if form.is_valid():
            new_post1 = form.save(commit=False)
            new_post1.user = request.user
            new_post1.save()
            form = HomeForm1()
            return redirect('home1:home1')            

        context = {'form':form}
        return render(request,self.template_name,context)

def change_friend(request,operation,id):
    friend = CustomUser.objects.get(id=id)
    if operation =='add':
        Friends.make_friend(request.user,friend)
    elif operation =='remove':
        Friends.lose_friend(request.user,friend)
    return redirect('home1:home1')

