import requests
from bs4 import BeautifulSoup as bs
import pprint
import json

from requests.api import put

def main(query):
    r_rss = requests.get(BASEURL, params=query)
    q_json = {'rss_url': r_rss.url}
    r_json = requests.get(JSONURL, params=q_json).json()

    put_in_data = {}
    for i in range(len(r_json['items'])):
        _link = r_json['items'][i]['link']
        _img = ''
        try:
            _img = getImg(searchIsbn(_link))
        except:
            _img = ''
        put_in_data[i] = {
            'title': r_json['items'][i]['title'],
            'link': _link,
            'isbn': searchIsbn(_link),
            'img': _img
        }
    pprint.pprint(put_in_data)
    with open('./json/2021/d0405.json', 'w') as f:
        json.dump(put_in_data, f, indent=4)
    result = requests.put('https://technical-book-list-default-rtdb.firebaseio.com/', json=put_in_data)
    print(result)
    return put_in_data

def searchIsbn(link):
    soup = bs(requests.get(link).text, 'lxml')
    isbn = soup.find('th', text='ISBN').find_parent('tr').td.span.string
    return isbn

def getImg(isbn):
    r_googlebooks = requests.get(GOOGLEBOOKSURL, params={'q': f'isbn:{isbn}'})
    r_googlebooks_json = r_googlebooks.json()
    return r_googlebooks_json['items'][0]['volumeInfo']['imageLinks']['thumbnail']

if __name__ == '__main__':
    BASEURL = 'https://iss.ndl.go.jp/api/opensearch'
    JSONURL = 'https://api.rss2json.com/v1/api.json'
    GOOGLEBOOKSURL = 'https://www.googleapis.com/books/v1/volumes'
    isbn = '4295010731'
    _from = '2021-04'
    _until = '2021-05'
    query = {'ndc': '007', 'mediatype': '1', 'from': _from, 'until': _until}
    main(query)