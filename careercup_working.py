# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 22:00:09 2016

@author: lalit
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:19:40 2016

@author: Lalit
"""
import re
#import wsgi2cgi
#wsgi2cgi.re.escape('')    a<b
#Lalit final <a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*?[\s\-\<a-zA-Z\/\>\=\"\:\.\?\d\(\)\;]*?<abbr.*class="timeago".*?\"\>(.*?)\<\/abbr>[a-zA-Z\s\<\_\=\"\d\/\?\>\|\:\.]*?(<span.*class="tags">.*[a-zA-Z\s\<\=\"\:\/\/\?\.\-\>]*?</span>)

#<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p></a>[\s]*<span class="author">[\s]*- <a href="https://www.careercup.com/user\?id=.*\)\;">(.*?)</a> <abbr class="timeago".*?\"\>(.*?)\<\/abbr>(.*?)[\s]*?\<edit author_id\=\".*Flag</a> </span>[\s]*</span>[\s]*<span class="tags">[\s]*<a href=\"https://www.careercup.com/page\?pid\=.*?">(.*?)</a>
#<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)
#<span.*class="tags">[a-z\.\s\<\?\>\"\:\/\\\=\-]*?([A-Za-z].*)
fconn=open("C:\\Users\\lalit\\Desktop\\Stevens\\Python\\careerCuP\\1.html")
htmldat=fconn.read()#read the entire html into this variable
html=htmldat.replace("<br>","")
print html 
p = re.compile('<a.*?href.*?question.*?<p>([a-zA-Z\s\,\[\]\(\)\.\'\"\#\?\@\`\%\^\*\:\=\d\&\;\_\{\}\!\$\+\\\/\-\|\…\</>]*?)</p>.*?<a href="/user.*?popup\(.*\)\;\"\>(.*?)</a>')
#[] and <>

#<a.*?href.*?question.*?<p>([a-zA-Z\_\:\d\&\;\=\.\*\s\S\n].*[\s].*?[\.\s].*)?</p>')

Ms=re.finditer(p,html)
#print Ms
for M in Ms:
    print M.group(1),M.group(2)   #questions        
#            q=M.group(1)
            
            

#<.*?<a*?p>([a-zA-Z\s\S\n].*[\s].*?[\.\s].*)?</p>