# -*- coding: utf-8 -*-

"""
Created on Thu Mar 10 19:19:40 2016
@author: Lalit
"""
import re,sys,time
from selenium import webdriver
#Set up encoding to UTF in case translation error occurs during scrape

# Set default python encoding to utf-8 instead of asciii. 
#sys.setdefaultencoding('utf8')
#sys.getdefaultencoding()

driver = webdriver.Chrome('C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCup\\chromedriver.exe')

def parsePage(html):
    #Regex to find the questions between <a><p></p></a> tags.Escape all special characters to fetch programs.
    p=re.compile('<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?<abbr.*?Z">(.*?)</abbr>.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?(<span class="tags">.*[\sa-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?</span>)')
    Ms=re.finditer(p,html)
    for count,M in enumerate(Ms):
        global qnum
        qnum=qnum+1 #increate question count for every page HENCE SET GLOBAL
        fw.write('\n'+"---Question :"+str(qnum)+"---"+'\n')        
        ques=re.sub(' +',' ',M.group(1)).strip()
        question=re.sub(' +',' ',ques).strip()#remove duplicate spaces
        fw.write(question+'\n')   
        #print question
        tagshtml=M.group(3) #Get questions tags HTML and retrive each tag using below RE 
        tags=re.finditer('<a.*?[a-z\<\s\=\"\>\/\?\-]*?>(.*?)</a>',tagshtml)
        for tag in tags:
            fw.write('\n'+tag.group(1))
        fw.write('\n'+'EndOfQuestion'+'\n') #Adding EndOfQuestion to detect question end.

fw=open('dataset.txt','a+')
page=1
#Global qnum is used to identfy the question sequence on pagination
qnum=0  
while True:
    
    try:    
        url='https://www.careercup.com/page?n='+str(page)
        print 'Processing Page:',page
        driver.get(url)
        htmldat=driver.page_source
        #Removing all <BR> tags as this was causing problems in scrape
        html1=htmldat.replace("<br />","")
        html=html1.replace("<br>","")
        #print html
        parsePage(html) 
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break
    time.sleep(3)
    page+=1 #Go to Next page
fw.close()
