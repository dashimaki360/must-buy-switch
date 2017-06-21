# -*- coding: utf-8 -*- 
# please run with `python3`
import check_yodobashi
import send_urlrequest

if __name__ == "__main__":
  if check_yodobashi.check_yodobashi():
      send_urlrequest.ifttt_urlreq()

