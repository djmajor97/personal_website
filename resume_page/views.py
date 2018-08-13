from django.shortcuts import render

# Since this website is just to display the main page, there's just one view
def homepage(request):
    return render(request, 'resume_page/homepage.html', {})