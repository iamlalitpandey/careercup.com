# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:19:40 2016

@author: Lalit
"""
import re,sys,time
from selenium import webdriver
from fuzzywuzzy import fuzz
import json
#reload(sys)  

# Set default python encoding to utf-8 instead of asciii.
#sys.setdefaultencoding('utf8')
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
    strTags=''
    for count,M in enumerate(Ms):
        tagshtml=M.group(3)
        tags=re.finditer('<a.*?[a-z\<\s\=\"\>\/\?\-]*?>(.*?)</a>',tagshtml)
                
        strTags=''
        for tag in tags:
            strTags+=str(tag.group(1)+' ')
        data = {'question' : M.group(1),'tags' :strTags}
        json.dump(data, f)             
        f.write('\n')
        
#fw=open('dataset.txt','a+')
f=open('data.json', 'a+')
page=1
while True:
    
    try:    
        url='https://www.careercup.com/page?n='+str(page)
        driver.get(url)
        htmldat=driver.page_source
        
        html1=htmldat.replace("<br />","")
        html=html1.replace("<br>","")
        #print html
        parsePage(html)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break
    time.sleep(5)
    page+=1
f.close()
#####################


s1='System design of high traffic eCommerce website including inventory'
s2='eCommerce including inventory designs'
s3='eCommerce website including inventory design system is use less'
s4='info sys maths website inventory design'
s5='Maths what info sys in not a competitive in area of sector'


fuzz.partial_ratio(s1, s1)
fuzz.partial_ratio(s1, s2)
fuzz.partial_ratio(s1, s3)
fuzz.partial_ratio(s1, s4)
fuzz.partial_ratio(s1, s5)


fuzz.token_set_ratio(s1, s2)
fuzz.token_set_ratio(s1, s3)


from difflib import SequenceMatcher as SM
s1 = ' It was a dark and stormy night. I was all alone sitting on a red chair. I was not completely alone as I had three cats.'
s2 = ' It was a murky and stormy night. I was all alone sitting on a crimson chair. I was not completely alone as I had three felines.'
SM(None, s1, s2).ratio()
#0.9112903225806451


#difflib 
 #get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
 #s = SequenceMatcher(None, "abcd", "bcde")


#s.ratio()
#s.real_quick_ratio()


#simstring















