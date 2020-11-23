#!/usr/bin/env python3
'''
# search input form from the web page:
<form method="post" action="/example-sentences/index.php">
<div style="text-align:center;">
<input type="text" placeholder="" name="sentence_keyword" id="sentence_keyword" value="lagi" class="prettyformsmall searchbox" style="min-height:50px; box-sizing:border-box; font-size:21px; width:100%; max-width:500px; min-width:280px; margin:4px 0 4px 0;">
<br>
<div style="padding-top:4px; padding-bottom:4px;">
<input type="checkbox" name="ligature_search" checked selected id="ligature_search" value="1">
<label for="ligature_search" style="padding:4px 24px 4px 6px; display:inline-block; cursor:pointer; color:#555; font-size:14px;">
<b>Recommended:</b>
Include sentences with ligature match.<br>
(Ex: keyword "bata" will show results for "bata" and "batang")
</label>
</div>
<br>
<input type="submit" value="Search &raquo;" class="bigbtn bluebtn majorbtn">
</div>
</form>


POST /example-sentences/index.php HTTP/2
Host: www.tagalog.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 39
Origin: https://www.tagalog.com
DNT: 1
Connection: keep-alive
Referer: https://www.tagalog.com/example-sentences/index.php
Cookie: sess_id=ma_5fa6ffad59f689.46266600; sess_id=ma_5fa6ffad59f689.46266600; sess_id=ma_5fa6ffad59f689.46266600; uniquecookieid=a2155c; forumsign=5738; recently_viewed_section_csid=3; recentlyviewedlessons=%5B%7B%22csid%22%3A47%2C%22title%22%3A%22Everyday+Greetings+to+Start+a+Co%22%2C%22pcsid%22%3A3%2C%22item_type%22%3A%22Lesson%22%2C%22item_id%22%3A28%7D%2C%7B%22csid%22%3A63%2C%22title%22%3A%22Expressions+Used+When+Leaving+or%22%2C%22pcsid%22%3A3%2C%22item_type%22%3A%22Lesson%22%2C%22item_id%22%3A37%7D%2C%7B%22csid%22%3A60%2C%22title%22%3A%22Saying+Sorry+and+Excusing+Onesel%22%2C%22pcsid%22%3A3%2C%22item_type%22%3A%22Lesson%22%2C%22item_id%22%3A36%7D%2C%7B%22csid%22%3A69%2C%22title%22%3A%22Other+Useful+Expressions+for+Eve%22%2C%22pcsid%22%3A3%2C%22item_type%22%3A%22Lesson%22%2C%22item_id%22%3A39%7D%5D; recently_viewed_csid=63; tz=America%2FLos_Angeles; __cfduid=d5e01f824c45251363c4b3c80f673811f1604028976; uniquecookieid=a2155c; agegroup=Adult; lessonlanguage=Tagalog; recently_viewed_thread=16849; pickupwhereyouleftoffalreadyasked=1; pvs=x; selectedlanguage=Tagalog; nightmode=1
Upgrade-Insecure-Requests: 1

sentence_keyword=lagi&ligature_search=1
'''

import requests

_word='lagi'

_headers = {
    'Host': 'www.tagalog.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.tagalog.com',
    'DNT': '1',
}

_dat = f'sentence_keyword={_word}&ligature_search=1'
#_dat = {'sentence_keyword': f'{_word}&ligature_search=1'}

_out = requests.post('https://www.tagalog.com/example-sentences/index.php', headers=_headers, data=_dat)
if _out.ok:
    f = open(f'{_word}.php', 'w')
    f.write(_out.text)
    f.close()
else:
    print('Fail.  Got ', _out.headers['Content-Type'])
