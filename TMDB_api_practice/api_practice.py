import requests
api_key = 'myapikey'
url = f'https://api.themoviedb.org/3/movie/top_rated?'
params = {'api_key': api_key, 'language': 'ko-KR', 'page' : 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    # Process the response here
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
