import requests
from bs4 import BeautifulSoup


response = requests.get('http://oracleofbacon.org/')

if response.status_code == 200:

    response = requests.post('http://oracleofbacon.org/', data={'a':'kevin bacon','b':'tim roth'})

    if response.status_code == 200:

        # print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.body.findAll(text= 'Bacon')
        print(results)


