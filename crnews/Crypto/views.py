from django.shortcuts import render

def home(request):
    import requests
    import json
    api_req=requests.get("https://api.coingecko.com/api/v3/search/trending")
    api=json.loads(api_req.content)
    
    return render(request,'home.html',{'api':api})

