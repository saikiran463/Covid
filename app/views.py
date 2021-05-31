from django.shortcuts import render
from django.http import HttpResponse
import matplotlib
matplotlib.use('Agg')
matplotlib.rc('figure',max_open_warning=0)
import matplotlib.pyplot as plt
import requests
import json
import os

def index(request):
    dat=True
    result=None
    globe=None
    country=None
    whole=None
    while (dat):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            data= result.json()
            request.session['value']=data
            globe = data["Global"]
            country= data['Countries']
            country1= sorted(country, key=lambda k: k["TotalConfirmed"],reverse=True)
            country1= country1[0:10]
            whole=json.dumps(data)
            dat= False
        except:
            dat= True
    return render(request,'index.html',{'globe':globe,'country':country,'whole':whole,'country1':country1})

def visual(request):
    if request.POST:
        val=request.POST.get('bt')
        if val==" ":
            val="Global"
        data1 = request.session['value']
        globe = data1["Global"]
        country = data1['Countries']
        whole = json.dumps(data1)
        x = ['NewConfirmed', 'TotalConfirmed', 'NewDeaths', 'TotalDeaths', 'NewRecovered', 'TotalRecovered']
        y = [0,0,0,0,0,0]
        if(val=='Global'):
            y[0] = globe['NewConfirmed']
            y[1] = globe['TotalConfirmed']
            y[2] = globe['NewDeaths']
            y[3] = globe['TotalDeaths']
            y[4] = globe['NewRecovered']
            y[5] = globe['TotalRecovered']
        else:
            for i in range(len(country)):
                if (country[i]['Country'] == val):
                    nc = country[i]['NewConfirmed']
                    tc = country[i]['TotalConfirmed']
                    nd = country[i]['NewDeaths']
                    td = country[i]['TotalDeaths']
                    nr = country[i]['NewRecovered']
                    tr = country[i]['TotalRecovered']
                    y[0] = nc
                    y[1] = tc
                    y[2] = nd
                    y[3] = td
                    y[4] = nr
                    y[5] = tr
                    break

        nc = y[0]
        tc = y[1]
        nd = y[2]
        td = y[3]
        nr = y[4]
        tr = y[5]

        plt.subplots(figsize=(10, 8))
        plt.bar(x, y, label=""+val, color='blue',width=0.4)
        for i in range(6):
            plt.text(i, y[i] , y[i], ha="center")
        plt.legend()
        plt.savefig("/app/static/output.png")
        plt.close()
        return render(request, 'visual.html', {'globe': globe, 'country': country, 'whole': whole,'val':val,'nc':nc,'tc':tc,'nd':nd,'td':td,'nr':nr,'tr':tr})
    return render(request, 'visual.html')




