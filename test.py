import requests

import datetime
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

 
url = "https://push.showdoc.com.cn/server/api/push/c59cbd9bc8f07a5e3bf108ee705588b92019146896"
myParams = {"title":"test","content":time}
res = requests.get(url=url, params=myParams)
 
print('url:',res.request.url)
