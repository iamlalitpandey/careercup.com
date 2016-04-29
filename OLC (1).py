"""
The script parses a page of reviews from Amazon.com and stores the review Information in a text file
"""
import re
from bs4 import BeautifulSoup,Tag
import requests,time
#from bs4.builder import HTMLParserTreeBuilder
#import lxml.html


reviewChunks = tree.findAll('ul', {'id':'question_preview'})
# find all review Chunks


#print(tree)

for RC in reviewChunks:
    starChunk=RC.find('i',{'class':'a-icon-star'})#<i class="a-icon a-icon-star a-star-4 review-rating"><span class="a-icon-alt">4.0 out of 5 stars</span></i>
    stars=starChunk.text

    titleChunk=RC.find('a', {'class':'review-title'})#<a class="a-size-base a-link-normal review-title a-color-base a-text-bold" href="/gp/customer-reviews/RTCU9IHUSOC3K/ref=cm_cr_pr_rvw_ttl?ie=UTF8&amp;ASIN=B00XKRWTUE">Very Good</a>
    title=titleChunk.text

    userChunk=RC.find('a',{'class':'author'})#<a class="a-size-base a-link-normal author" href="/gp/pdp/profile/AZ0OW7VY5G26T/ref=cm_cr_pr_pdp?ie=UTF8">John McCarthy</a>
    user=userChunk.text

    dateChunk=RC.find('span',{'class':'review-date'})#<span class="a-size-base a-color-secondary review-date">on February 2, 2016</span>
    date=dateChunk.text

    textChunk=RC.find('span',{'class':'review-text'})#<span class="a-size-base review-text">Works great.  Quick to connect to GPS. ... </span>
    text=textChunk.text
    text=text.encode('ascii','ignore')# remove non-utf 8 characters
     
    print stars,'\n',title,'\n',user,'\n',date,'\n',text
    print
###replace
    ##save
page=1
html_data  = requests.get('https://www.careercup.com/page?n='+str(page))
print html_data.text
html=html_data.text.replace("<br />","")
print html
html.replace("<br>", "")
print html
fw=open('test.html','w')
fw.write(html)

fw.close()

tree = BeautifulSoup(html,"lxml")





#html.content = html.content.replace("Find", "UNFIND")
#html.renderContents()

#tree = BeautifulSoup(html)

#tree = BeautifulSoup(html.text)

questionChunks = tree.findAll('li', {'class':'question'})
for count,qc in enumerate(questionChunks):
    qtext=qc.find('span',{'class':'entry'})
    question=qtext.find('p')
    print count+1  
    print qtext

#tree1=tags.extract() for tags in tree('<br>','</br>')    
#type(tree1)
#print tree1
#type(tree)
#tree = tree.decompose('br')
#myi = tree.find("br")
#myi.replaceWith(BeautifulSoup(" "))
#myi = tree.find("br/")
#myi.replaceWith(BeautifulSoup(" "))
#new_tag = tree.new_tag(" ")
#new_tag.string = "example.net"
#tree.br.replace_with(new_tag)
#tree = BeautifulSoup(tree.renderContents())
print "after"
type(tree)    
#print tree    
        
    
    
    
    
    
    
    
page=1
while True:
    html  = requests.get('https://www.careercup.com/page?n='+str(page))
    tree = BeautifulSoup(html.text,"html.parser")
    
    
    questionChunks = tree.findAll('li', {'class':'question'})
    
    for count,qc in enumerate(questionChunks):
        qtext=qc.find('span',{'class':'entry'})
        question=qtext.find('p')
        
        print count+1  
        print question.text
        #print qc.find(qtext.find('p')).findNext('<br>').contents[0]
        #print "next"        
        #print qtext.next_sibling
        #print("next sibling above")

        
        #print question.text
        #print qtext.next_sibling
        time.sleep(6)

    try:
        print
        #button=driver.find_element_by_css_selector(cssPath)
    except:
    #    error_type, error_obj, error_info = sys.exc_info()
     #   print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
     #   print error_type, 'Line:', error_info.tb_lineno
        break

    #click the button to go the next page, then sleep    
    #button.click()
    time.sleep(2)
