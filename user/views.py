from django.shortcuts import render

# Create your views here.


def save_user(request):
    pass
    #if request type is POST
    #pass the request.POST to serializer and 
    #check if it was valid or not and save it
    #return HttpResponse or render page
    

def login(request):
    pass
    #check email_id and passwords are correct or NOT
    #if correct the render success page
    #else render to login page with error message
    