import requests

response = requests.get('https://viacep.com.br/ws/{}/json/'.format('04272300'))
print(response.text)