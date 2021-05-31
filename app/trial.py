"""""


def index(request):
   data = True
   result = None
   globe = None
   country = None
   whole = None
   while (data):
      try:
         # result = requests.get('https://api.covid19api.com/summary')
         f = open("C:\\Users\\saikiran reddy\\Downloads\\data.json")
         globe = json["Global"]
         country = json['Countries']
         country1 = sorted(country, key=lambda k: k["TotalConfirmed"], reverse=True)
         country1 = country1[0:10]
         whole = json.load(f)
         data = False
      except:
         data = True
   return render(request, 'index.html', {'globe': globe, 'country': country, 'whole': whole, 'country1': country1})

"""""
import os
l=os.getcwd()
m=os.path.join(l+''+'\static\output.png')
s=r''+m
d=s.replace('\\','\\\\')
print(d)