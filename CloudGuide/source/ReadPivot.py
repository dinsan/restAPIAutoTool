import pandas as pd
import pkgutil


excel_file = 'ceramica_routes.xlsx'
movies = pd.read_excel(excel_file)
pivotMovie = movies.head()

json = pivotMovie.to_json(orient='split')
print (json)


def GetCeramicaPivotData():

    excel_file = 'ceramica_routes.xlsx'
    movies = pd.read_excel(excel_file)
    pivotMovie = movies.head()

    json = pivotMovie.to_json(orient='split')

    return  json
