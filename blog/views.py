from django.shortcuts import render

def resume_template(request):
    return render(request, 'index.html')
