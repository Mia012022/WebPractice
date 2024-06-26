import requests
from bs4 import BeautifulSoup
import json
url = "https://www.ptt.cc/bbs/NBA/index.html"  # 替换为实际的目标 URL
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all('div',class_='r-ent')

data_list = []
for a in articles:
    data = {}
    title = a.find("div",class_="title")
    popular = a.find('div',class_='nrec')
    date = a.find('div',class_='date')
    if title and title.a:
        title = title.a.text
    else:
        title ="沒有標題"
   
    if popular and popular.span:
        popular = popular.span.text 
    else:
        popular = "N/A"
    data['標題'] = title
    data['人氣'] = popular    
    data['日期'] = date.text
    data_list.append(data)
with open('ptt_nba_data.json','w',encoding='utf-8') as file:
    json.dump(data_list,file,ensure_ascii=False,indent=3)
print("資料已成功儲存")
# print(data_list)
    # print(f"標題:{title} 人氣{popular} 日期{date.text}" )
 

# if response.status_code == 200:
#     with open('output.html','w',encoding='utf-8') as f:
#         f.write(response.text)
#         print("寫入成功")
# else:
#     print("沒抓到網頁")




