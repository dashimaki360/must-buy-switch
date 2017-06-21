# -*- coding: utf-8 -*- 
 
# please run with `python3`

from urllib.request import urlopen
 
 
def check_yodobashi():
    # yodobashi.com swhitch url
    url = "http://www.yodobashi.com/product/100000001003431566/"

    # URLを指定してHTMLファイルを開く
    response = urlopen(url)
    html =  response.read().decode('utf-8')
    # serch 'hanbaikyushi'
    can_buy = not '予定数の販売を終了しました' in html

    print(can_buy)
    return can_buy

if __name__ == "__main__":

    print(check_yodobashi())

