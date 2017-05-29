# -*- coding: utf-8 -*- 
 
# please run with `python3`

from urllib.request import urlopen
 
 
def check_yodobashi():
    # yodobashi.com swhitch url
    url = "http://www.yodobashi.com/product/100000001003431566/"

    # URLを指定してHTMLファイルを開く
    response = urlopen(url)

    # serch 'hanbaikyushi'
    can_buy = not '販売休止中です' in response.read().decode('utf-8')

    return can_buy

if __name__ == "__main__":

    print(check_yodobashi())

