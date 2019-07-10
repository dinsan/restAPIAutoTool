from django.http import JsonResponse
import pandas as pd
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'ceramica_routes.xlsx')

def topic(request):
    data = {
        "Country of origin":
        {
         "EU" : [ "Local", "Non Local"],
         "Non EU" : [ "Local", "Non Local"]
         },
         "Language" : [ "Language of the institutions ", "Device Language","Application Language","User Language"],
         "Technology": [ "Operation System","Applications and visits","Am/Pm","Day", "Week","Month","se of the Content","Exhibits","ser Typology","Ceramica visitors","Other Institution Visitors"]
    }
    return JsonResponse(data)


def customer(request):

    jsonData = GetCeramicaPivotData()

    #print(jsonData)

    return JsonResponse(jsonData, safe=False)

def GetCeramicaPivotData():

    
    movies = pd.read_excel(my_file)
    pivotMovie = movies.head()
    json = pivotMovie.to_json(orient='split')

    return json


def byCountry(request):
    data = {
        "ByCountry":
        {
         "labels" : ["es",
      "en",
      "nl",
      "it",
      "de",
      "fr",
      "ru",
      "pt",
      "pl",
      "ca",
      "zh",
      "da",
      "ko",
      "zh-cn",
      "ro",
      "ja",
      "lt",
      "nb",
      "sk",
      "sl",
      "zh-hk"],
         "datasets" :[{
          "label": 'By country',
          "data": [365,
            278,
            194,
            141,
            60,
            58,
            25,
            21,
            12,
            8,
            7,
            3,
            3,
            3,
            2,
            1,
            1,
            1,
            1,
            1,
            1],
          "backgroundColor": [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)'
          ],
          "borderColor": [
              'rgba(255,99,132,1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
          ],
          "borderWidth": 1}]
         }


    }
    return JsonResponse(data)