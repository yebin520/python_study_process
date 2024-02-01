import requests,parsel
headers = {
"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
}
def get_html(url,headers):
    res = requests.get(url=url, headers=headers)
    selector = parsel.Selector(res.text)
    with open("a1.html",encoding='utf-8',mode='w') as f:
        f.write(res.text)
name = input("请输入小说名称:\n")

url = f"http://www.biqu5200.net/modules/article/search.php?searchkey={name}"
get_html(url,headers)
