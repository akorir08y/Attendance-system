from django.shortcuts import render,redirect
from TTU_SYSTEM.models import CustomUser
from django.views.generic import TemplateView
from .forms import HomeForm2
from .models import Post2

# Create your views here.

class GroupView1(TemplateView):
    template_name = 'home1/group.html'

    def get(self, request):
        form = HomeForm2()
        posts = Post2.objects.order_by('-created')
        users = CustomUser.objects.exclude(id=request.user.id)
        group = UserGroup.objects.get(current_user1=request.user)
        groups = group.users.all()

        context = {'users':users,'groups':groups}
        return render(request,self.template_name,context)

    def post(self, request):
        form = HomeForm2(request.POST)
        if form.is_valid():
            new_post2 = form.save(commit=False)
            new_post2.user = request.user
            new_post2.save()
            form = HomeForm2()
            return redirect('home1:group')            

        context = {'form':form}
        return render(request,self.template_name,context)



def group1(request,operation,id):
    usergroup, created = UserGroup.objects.get_or_create(name='group')
    usergroup.value = request.POST.get('group')
    usergroup.save()

    usergroup = CustomUser.objects.get(id=id)
    if operation =='add':
        UserGroup.add_to_group(request.user,usergroup)
    elif operation =='remove':
        UserGroup.remove_from_group(request.user,usergroup)
    return render(request,('home1/group.html'))