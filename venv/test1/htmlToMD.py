from tomd import Tomd
import requests
from lxml import etree



def getHtml(url):

    response = requests.get(url)

    html_str = response.text

    html = etree.HTML(html_str)
    htmlPage = html.xpath('//div[@class="pcb"]/div[@class="t_fsz"]//td[@id="postmessage_81"]')[0]
    for i in htmlPage:
        print(i.text)
    with open("kw.html", "w", encoding="utf-8") as fp:
        fp.write(htmlPage.text)




if __name__ == "__main__":

    getHtml("http://bbs.mob.com/forum.php?mod=viewthread&tid=62")
