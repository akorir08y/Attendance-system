from django.shortcuts import redirect

def login_success(request):
    """
    Redirects users based on whether they are in the student group
    """
    if request.user.user_profile.reg_no:
        return redirect('home1:home1')
    elif request.user.lec_profile.Employee_no:
        return redirect('home:home')  
    else:
        return None