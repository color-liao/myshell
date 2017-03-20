#!/usr/bin/python 
#coding=utf8
_DEBUG=True
import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
VAR_KEYWORDS='文员'
VAR_PAGES=1
def getHtml(pages):
	params = urllib.urlencode({'curr_page':pages,'fromJs': 1,'jobarea': '030200','keyword':VAR_KEYWORDS,'keywordtype': 2,'lang': 'c','stype': 2,'postchannel': 0000,'fromType': 1,'confirmdate': 9})
#	print "http://search.51job.com/jobsearch/search_result.php?%s" % params
	page = urllib.urlopen("http://search.51job.com/jobsearch/search_result.php?%s" % params)
	html = page.read()
	return html

#	def getImg(html):
#	reg = r'src="(.+?\.jpg)" pic_ext'
#	imgre = re.compile(reg)
#	imglist = re.findall(imgre,html)
#	return imglist

def grep(html):
	reg = re.compile(r'.*target="_blank" title.*')
	items = re.findall(reg,html)
	return items 
def findurl(html):
        items = re.findall(r'title.*',html)
        items = re.findall(r'\"([^\"]*)\"',items[0])
        return items
def allpages(html):
        items = re.findall(r'jumpPage\(\'\d{1,5}\'\)',html)
	items = re.findall(r'\d{1,5}',items[0])
        return items
html = getHtml(1)
html=html.decode('gbk')
html=html.encode('utf8')
#print html
VAR_PAGES=allpages(html)[0]
pages=int(VAR_PAGES)
while pages>0:
	html = getHtml(pages)
	pages-=1
	html=html.decode('gbk')
	html=html.encode('utf8')
	ghtml=grep(html)
	for a in ghtml:
		b=findurl(a)
		print b[0],b[1]

