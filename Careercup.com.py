# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:19:40 2016

@author: Lalit
"""
import re,sys,time
from selenium import webdriver

#reload(sys)  

# Set default python encoding to utf-8 instead of asciii.
sys.setdefaultencoding('utf8')
#sys.getdefaultencoding()

driver = webdriver.Chrome('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\chromedriver.exe')

def parsePage(html):
#p = re.compile('<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?(<span class="tags">.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?</span>)')
    p=re.compile('<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?<abbr.*?Z">(.*?)</abbr>.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?(<span class="tags">.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?</span>)')
    
    #working 1 #  '<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*?[\s\-\<a-zA-Z\/\>\=\"\:\.\?\d\(\)\;]*?<abbr.*class="timeago".*?">(.*?)</abbr>.*[a-zA-Z\s\<\_\=\"\d\/\?\>\|\:\.]*?\
            #[\s\<\>\:\/\\\?a-zA-Z\_\=\"\d\|\.]*?(<span.*class="tags">.*[\s\<\>\:\/\\\?a-zA-Z\_\=\"\d\|\.\-]*?</span>)')    
    # Working 2 #for 3 tags '<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*?[\s\-\<a-zA-Z\/\>\=\"\:\.\?\d\(\)\;]*?<abbr.*class="timeago".*?\"\>(.*?)\<\/abbr>[a-zA-Z\s\<\_\=\"\d\/\?\>\|\:\.]*?(<span.*class="tags">.*[a-zA-Z\s\<\=\"\:\/\/\?\.\-\>]*?</span>)')
    #'<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\<\>]*?)</p>.*?<a href="/user.*popup\(.*\)\;\"\>(.*?)</a>')    
    Ms=re.finditer(p,html)
    for count,M in enumerate(Ms):
        fw.write('\n'+"----------- Question :"+str(count+1)+"-----------"+'\n')        
        fw.write(M.group(1)+'\n')
        fw.write('\n'+M.group(2)+'\n')
        tagshtml=M.group(3)
        tags=re.finditer('<a.*?[a-z\<\s\=\"\>\/\?\-]*?>(.*?)</a>',tagshtml)
        for tag in tags:
            fw.write('\n'+tag.group(1))
        
fw=open('dataset43.txt','a+')
page=1
while True:
    
    try:    
        url='https://www.careercup.com/page?n='+str(page)
        driver.get(url)
        htmldat=driver.page_source
        
        html1=htmldat.replace("<br />","")
        html=html1.replace("<br>","")
        print html
        parsePage(html)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break
        time.sleep(2)
    page+=1
fw.close()
