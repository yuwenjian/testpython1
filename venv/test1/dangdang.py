import requests
from lxml import etree


result = []

def getHtml(page):

    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"+str(page)

    global result

    # headers = {
    #     "User-Agent:": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    # }
    response = requests.get(url)

    html_str = response.text

    # 排行榜数字列表
    rangNum = []

    html = etree.HTML(html_str)
    if(page == 1):
        rangNum1 = html.xpath('//div[@class="list_num red"]/text()')
        rangNum2 = html.xpath('//div[@class="list_num "]/text()')
        rangNum = rangNum1 + rangNum2
    else:
        rangNum2 = html.xpath('//div[@class="list_num "]/text()')
        rangNum = rangNum + rangNum2
    # print(rangNum)

    # 获取封面图片
    bookImage = html.xpath('//div[@class="pic"]/a/img/@src')
    # print(bookImage)

    # 获取书本名称
    bookName = html.xpath('//div[@class="name"]/a/@title')
    # print(bookName)

    # 获取书本价格
    bookPrice = html.xpath('//span[@class="price_n"]/text()')
    # print(bookPrice)


    for i in range(0,20):
        result_1 ={
            "range": rangNum[i],
            "bookImage": bookImage[i],
            "bookName": bookName[i],
            "bookPrice": bookPrice[i]
        }
        result.append(result_1)


import xlwt
import pandas as pd

def saveFile(result):
   # 将字典列表转换为DataFrame
   pf = pd.DataFrame(result)
   # 指定字段顺序
   order = ['range', 'bookImage', 'bookName', 'bookPrice']
   pf = pf[order]
   # 将列名替换为中文
   columns_map = {
      'range': '排行榜',
      'bookImage': '书面',
      'bookName': '书名',
      'bookPrice': '书价',

   }
   pf.rename(columns = columns_map, inplace = True)
   #指定生成的Excel表格名称
   file_path = pd.ExcelWriter('name.xlsx')
   #替换空单元格
   pf.fillna(' ', inplace = True)
   #输出
   pf.to_excel(file_path, encoding = 'utf-8', index = False)
   #保存表格
   file_path.save()





if __name__ == '__main__':
    for page in range(1, 26):
        getHtml(page)

    # 保存到excel文件
    saveFile(result)