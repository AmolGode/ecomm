from django.shortcuts import render

# Create your views here.


def save_user(request):
    pass
    #if request type is POST
    #pass the request.POST to serializer and 
    #check if it was valid or not and save it
    #return sucess render page
    # else render signup page with error message
    

def login(request):
    pass
    #check email_id and passwords are correct or NOT
    #if correct the render success page
    #else render to login page with error message

def send_OTP(request):
    pass
    # generate OTP and snd it on moble number
    
    
def verify_mobile_number(request):
    pass
    # check OTP is correct or NOT 
    # if correct set mobile_number_verified field to True
    # else render OTP page with error_message