from django.shortcuts import render

# Create your views here.
def temp(request):
    return render(request, "base.html", {})


def check(request):
    """
    if request.method == "POST":
        
        fullName = (request.POST['fullName']).title()
        
        if Students.objects.filter(name=fullName).exists():
            # create session for login user
            request.session.get('stdName', '')
            request.session['stdName'] = fullName

            return redirect('register')
        else:
            messages.info(request, "Invalid Credentials")
            messages.info(request, "Make Sure you Input your name correctly or contact the school for help")
            return redirect('check')
            
    else:
        # delete user session
        try:
            del request.session['stdName']
        except KeyError: pass
    """
    return render(request, 'check.html', {})

