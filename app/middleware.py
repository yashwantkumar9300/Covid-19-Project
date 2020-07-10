import requests
import json

class Covid19Middleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Constructor")
        covid_19()

    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        print("I am Call")
        return response

def covid_19():
    response = requests.get("https://api.covid19india.org/state_district_wise.json")
    print(response.status_code)
    dict_data = json.loads(response.text)
    json.dump(dict_data, open("app/raw/covid19.json", "w"))
    print("Data Written to File")