import requests
url = 'https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&form=ANSNB1&refig=f4453eddf85a4a2e89c43402fe5b12cd&pc=U531'

headers = {
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64"
}

resp = requests.get(url,headers = headers)
ans = resp.text
print (ans)