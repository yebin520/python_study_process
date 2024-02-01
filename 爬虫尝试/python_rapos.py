import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars%27'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}
response = requests.get(url,headers=headers)
response_dict = response.json()

print(f"Total_count:{response_dict['total_count']}")

repo_dicts =response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for k in repo_dict.keys():
    print(k)