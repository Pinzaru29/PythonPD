import requests
import json

url = "www.cbr-xml-daily.ru/daily_json.js"
array = []

with open("dataset.csv", "w") as dataset:

    for i in range(15):

        urlmodified = "https://" + url

        response = requests.get(urlmodified)
        response_json = json.loads(response.text)

        date = response_json['Date']
        dollar = response_json['Valute']['USD']['Value']

        url = response_json['PreviousURL'][2:]

        dllar = dollar
        dte = date

        stroke = ''
        stroke += str(dte) + ' , ' + str(dllar) + ' \n'
        print(stroke)
        array.append(stroke)

    for i in array:
        dataset.write(i)
