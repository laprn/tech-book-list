import requests

def main(query):
    r_rss = requests.get(BASEURL, params=query)
    q_json = {'rss_url': r_rss.url}
    r_json = requests.get(JSONURL, params=q_json).json()
    result = []
    for i in range(len(r_json['items'])):
        result.append(r_json['items'][i]['title'])
    print(result)
    return result


if __name__ == '__main__':
    BASEURL = 'https://iss.ndl.go.jp/api/opensearch'
    JSONURL = 'https://api.rss2json.com/v1/api.json'
    _from = '2021-04'
    _until = '2021-05'
    query = {'ndc': '007', 'mediatype': '1', 'from': _from, 'until': _until}
    main(query)