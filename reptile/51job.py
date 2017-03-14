#!/usr/bin/python 
_DEBUG=True
import re
import urllib

def getHtml():
	params = urllib.urlencode({'curr_page': 3,'fromJs': 1,'jobarea': 030200,'keyword':'%E8%BF%90%E7%BB%B4','keywordtype': 2,'lang': 'c','stype': 2,'postchannel': 0000,'fromType': 1,'confirmdate': 9})
	page = urllib.urlopen("http://search.51job.com/jobsearch/search_result.php?%s" % params)
	html = page.read()
	return html

#	def getImg(html):
#	reg = r'src="(.+?\.jpg)" pic_ext'
#	imgre = re.compile(reg)
#	imglist = re.findall(imgre,html)
#	return imglist

def grep(html):
	reg = re.compile(r'.*s=01.*')
	items = re.findall(reg,html)
	return items 
def findurl(html):
        items = re.findall(r'\"([^\"]*)\"',html)
        return items
def allpages(html):
        items = re.findall(r'jumpPage\(\'\d{0,5}\'\)',html)
	items = re.findall(r'\d{,5}',items[0])
        return items
html = getHtml()
html=html.decode('gbk')
html=html.encode('utf8')
print html
print allpages(html)
ghtml=grep(html)
for a in ghtml:
	b=findurl(a)
	print b[1],b[2]


