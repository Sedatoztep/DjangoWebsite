from django.http.response import HttpResponse
from django.shortcuts import render

data = {
    "blogs": [
        {
            "id": 1,
            "title": "About Python",
            "image": "1.jpeg",
            "is_active": True,
            "is_home": False,
            "description": "very good language"
        },
        {
            "id": 2,
            "title": "About Django",
            "image": "2.png",
            "is_active": True,
            "is_home": True,
            "description": "very good language"
        },
        {
            "id": 3,
            "title": "Cyber Security",
            "image": "3.jpeg",
            "is_active": False,
            "is_home": True,
            "description": "very good language"
        },
    ]
}

# Create your views here.
def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request,"blog/index.html", context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request,"blog/blogs.html", context)

def blog_details(request,id):
    return render(request, "blog/blog-details.html", {
        "id": id
    })
