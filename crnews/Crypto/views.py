from tkinter import E
from django.shortcuts import render


def home(request):
    import requests
    import json
    api_req = requests.get("https://api.coingecko.com/api/v3/search/trending")
    api = json.loads(api_req.content)
    coin = ['bitcoin', 'ethereum', 'cardano', 'polkadot', 'tether']
    api_for_history = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&ids=bitcoin,ethereum,tether,cardano,polkadot,&order=market_cap_desc&per_page=100&page=1&sparkline=false")
    api_hist = json.loads(api_for_history.content)
    return render(request, 'home.html', {'api': api, 'api_hist': api_hist})


def prices(request):
    if request.method=='POST':
        import requests
        import json
        quote=request.POST['quote']
        coin_name=quote.lower()
        crypto_req = requests.get("https://api.coingecko.com/api/v3/coins/"+coin_name+"")
        crypto = json.loads(crypto_req.content)
        return render(request, 'prices.html', {'crypto': crypto})
    else:
        return render(request,'prices.html',{})
    


    