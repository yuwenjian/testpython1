import requests
from lxml import etree




result = []

def getHtml(page):

    url = page
    headers ={
        "User - Agent" : "Mozilla / 5.0(Macintosh;Intel Mac OS X 10_14_6) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.182 Safari / 537.36"
    }
    response = requests.get(url, headers = headers)
    html_str = response.text

    # 排行榜数字列表

    html = etree.HTML(html_str)

    bookImage = html.xpath('//div[@class="pct"]/div[@class="pcb"]/div[@class="t_fsz"]//td[@class="t_f"]//img/@zoomfile')
    print(bookImage)





if __name__ == '__main__':

        getHtml("http://bbs.mob.com/forum.php?mod=viewthread&tid=8212&extra=page%3D1")

    # 保存到excel文件
    # saveFile(result)