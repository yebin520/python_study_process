from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
ans = resp.read()
# print (ans)
filename = 'file_work/mybaidu.html'
with open (filename,'w') as f:
    f.write(ans.decode("utf-8"))
    print ("Over!")