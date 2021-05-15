import requests

BASEURL = 'https://iss.ndl.go.jp/api/opensearch'
_from = '2021-04'
_until = '2021-05'
query = {'ndc': '007', 'mediatype': '1', 'from': _from, 'until': _until}

r = requests.get(BASEURL, params=query)

url = 'https://api.rss2json.com/v1/api.json'
print(r.url)

param2 = {'rss_url': r.url}
r2 = requests.get(url, params=param2)
print(r2.url)