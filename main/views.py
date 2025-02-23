from django.shortcuts import render, HttpResponse

def body(request):
    list_of_items = [
        "blog", "to do list", "budget maker", "calendar", "navbar", "POST function"
    ]

    context = {
        'list': list_of_items
    }

    return render(request, "main/body.html", context)