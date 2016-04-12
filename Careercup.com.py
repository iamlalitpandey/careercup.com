# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:19:40 2016

@author: Lalit
"""
import re
import time#,sys
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

def parsePage(html):
    p = re.compile('<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\<\>]*?)</p>.*?<a href="/user.*popup\(.*\)\;\"\>(.*?)</a>')    
    Ms=re.finditer(p,html)
    for M in Ms:
        fw.write(M.group(1)+'\n')
        fw.write(M.group(2)+'\n')    
    
    #questions=re.findall('<span class="entry">(.*?)<a href="/(question=.*?)><p>(.*?)</p>(.*?)</a>(.*?)</span>',html)    
    #for question in questions:
     #   print question.group(1).strip()        
        #userSet.add(user.group(1).strip())
fw=open('questions.txt','a+')
page=1
while True:
    
 #   try:    
        url='https://www.careercup.com/page?n='+str(page)
        #fconn=open("C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCuP\\1.html")
        #htmldat=fconn.read()#read the entire html into this variable
        #fconn.close()
        #type(htmldat)
        #print htmldat
        driver.get(url)
        htmldat=driver.page_source
        #htmldat1=htmldat.replace("<br/>","")
        html=htmldat.replace("<br />","")
        #html=htmldat.replace("<br />,"")
        parsePage(html)
        
#[] and <>

#<a.*?href.*?question.*?<p>([a-zA-Z\_\:\d\&\;\=\.\*\s\S\n].*[\s].*?[\.\s].*)?</p>')

        
      
        #parsePage(driver.page_source)
        #button=driver.find_element_by_css_selector(cssPath)
   # except:
       # error_type, error_obj, error_info = sys.exc_info()
     #   print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
     #   print error_type, 'Line:', error_info.tb_lineno
     #   break
        time.sleep(2)
        page+=1
fw.close()
