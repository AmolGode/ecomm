from django.shortcuts import render

# Create your views here.

def get_phone_list(request):
    pass
    # make ORM query to get mobile list from database
    # serialize the query set
    # and return serializer.data
    
def get_phone_details(request, phone_id):
    pass
    # When user click on any specific phone it will return 
    # all data related to specific phone
    # by query database using ORM , 
    #  serialize the queryset and return 
    # serializer.data

def create_order_for_phone(request,phone_id):
    pass
    # Fill the appropriate information in the Model UserPhoneOrder
    # save it
    # return order information to user

def cancel_order_for_phone(request,order_id):
    pass
    # change the order_status of order_id to cancelled
    # return order info to user