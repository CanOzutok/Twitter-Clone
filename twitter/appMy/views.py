from django.shortcuts import render

# Create your views here.


def Home(requeset):
    
    return render(requeset,'home.html')



def Explore(requeset):
    
    return render(requeset, 'explore.html')




def Profile(requeset):
    
    return render(requeset, 'profile.html')



def UserProfile(requeset):
    
    return render(requeset, 'userprofile.html')



def Login(request):
    
    return render(request, 'login.html')