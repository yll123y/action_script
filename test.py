import requests
 
url = "https://push.showdoc.com.cn/server/api/push/c59cbd9bc8f07a5e3bf108ee705588b92019146896"
myParams = {"title":"username","content":"plusroax"}
res = requests.get(url=url, params=myParams)
 
print('url:',res.request.url)
