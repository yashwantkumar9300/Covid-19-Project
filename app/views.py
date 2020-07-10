from django.shortcuts import render,redirect
from Covid19Project.settings import COVID_19_FILE
import json
from app.middleware import covid_19

def showIndex(request):
    dict_data = json.loads(open(COVID_19_FILE).read())
    states = [x for x in dict_data]
    states.pop(0)
    return render(request,"index.html",{"data":states})

def open_state(request):
    sname = request.GET.get("state_name")
    dict_data = json.loads(open(COVID_19_FILE).read())
    total =[[],[],[],[]]
    for x in dict_data[sname]['districtData']:
        for k,v in dict_data[sname]['districtData'][x].items():
            if k != 'delta' and k != 'notes':
                if k == 'active':
                    total[0].append(v)
                elif k == 'confirmed':
                    total[1].append(v)
                elif k == 'deceased':
                    total[2].append(v)
                else:
                    total[3].append(v)
    list_of_total = [sum(total[0]),sum(total[1]),sum(total[2]),sum(total[3])]
    return render(request,"state.html",{"sname":sname,"data":dict_data[sname],"total":list_of_total})

def refresh(request):
    covid_19()
    sname = request.GET.get("state_name")
    dict_data = json.loads(open(COVID_19_FILE).read())
    total = [[], [], [], []]
    for x in dict_data[sname]['districtData']:
        for k, v in dict_data[sname]['districtData'][x].items():
            if k != 'delta' and k != 'notes':
                if k == 'active':
                    total[0].append(v)
                elif k == 'confirmed':
                    total[1].append(v)
                elif k == 'deceased':
                    total[2].append(v)
                else:
                    total[3].append(v)
    list_of_total = [sum(total[0]), sum(total[1]), sum(total[2]), sum(total[3])]
    return render(request, "state.html", {"sname": sname, "data": dict_data[sname], "total": list_of_total})