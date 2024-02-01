import requests
url = "https://www.bilibili.com/video/BV1wL411e77T/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=9fa1e22c0e4bf2fce9c6d4890b3d3ae3"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37"
}
res = requests.get(url,headers=headers)

print(res.text)