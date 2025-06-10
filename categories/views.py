from django.shortcuts import render

def category_list(request):
    return render(request, 'categories/category_list.html', {'categories': ['student', 'teacher']})

def category_detail(request, category):
    return render(request, 'categories/category_detail.html', {'category': category})