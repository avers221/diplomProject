from django.shortcuts import render


def company_information(request):
    return render(request, 'newsFeed/about/about_company.html')
