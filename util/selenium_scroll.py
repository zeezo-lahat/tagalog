searchword = 'ayaw'
from selenium import webdriver
browser = webdriver.Chrome()
browser.get(f'https://www.tagalog.com/words/{searchword}.php')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
s1 = browser.page_source
fh = open(f"{searchword}.php", "w")
fh.write(s1)
browser.close()
browser.quit()
