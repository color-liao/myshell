#!/usr/bin/python 
#coding=utf8
_DEBUG=True
import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
VAR_KEYWORDS='运维'
VAR_PAGES='http://jobs.51job.com/qingdao-hdq/50455880.html'
def getpage(url):
	page = urllib.urlopen(url)
	html = page.read()
	html=html.decode('gbk')
	#html=html.encode('utf8')
	start = html.find(r'class="cn"') #起点记录查询位置    
	end = html.find(r'tPosition_center_bottomText')        
	html = html[start:end]
	value = re.sub('<[^>]+>','', html) #过滤HTML标签  
	value = re.sub('class="cn">','',value) #过滤HTML标签  
	value = re.sub('tPosition_center_bottomText','',value) #过滤HTML标签  
	value = re.sub('<p class="','',value) #过滤HTML标签  
	value = re.sub('\|?(&nbsp;)','',value) #过滤HTML标签  
	value = re.sub('\r\n','',value) #过滤HTML标签  
	value = value.split(' ') 
	print "=============================================================="
	for i in value:
		if i!='':
			i=re.sub('[^\S+]','',i)			
			print i 
			print "======================"
	print "=============================================================="
	return 0
pages=getpage(VAR_PAGES)
