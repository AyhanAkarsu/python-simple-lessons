import sys
import requests
url = 'https://api.apilayer.com/fixer/latest?base='
headers = {
    'apikey' : 'W9AH7f53YsxEy90Ai7C5KlW0LQdxdGRu'
}
birinci_doviz = input("Birinci döviz: ")
ikinci_doviz = input("İkinci döviz: ")
miktar = float(input("Miktar giriniz: "))
response = requests.get(url + birinci_doviz, headers)
json_verisi = response.json()
try:
    print(json_verisi["rates"][ikinci_doviz] * miktar)
except KeyError:
    sys.stderr.write("Yanlış döviz girişi...")
    sys.stderr.flush()
