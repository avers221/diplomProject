from django.shortcuts import render
from .models import Contact


def contact_list(request):
    object_list = Contact.published.all()
    return render(request,
                  'newsFeed/contacts/list.html',
                  {'object_list': object_list})