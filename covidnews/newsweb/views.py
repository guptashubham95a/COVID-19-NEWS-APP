from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    new_api_request =requests.get(
        "https://newsapi.org/v2/top-headlines?sortBy=publishedAt&country=in&category=health&apiKey=36a94d922b084fd1be08ec67e96b190e"

        # "https://newsapi.org/v2/everything?q=coronavirus&sortBy=publishedAt&sortBy=popularity&apiKey=36a94d922b084fd1be08ec67e96b190e"
        )
    api=json.loads(new_api_request.content)    
    return render(request, 'home.html',{'api':api})