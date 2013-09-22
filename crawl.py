#!/usr/bin/python
# Filename: crawl.py
from BeautifulSoup import BeautifulSoup
import urllib2
import codecs
import copy
import re
import argparse

parser = argparse.ArgumentParser(description='Query FormSpring for Questions')
parser.add_argument('query', default="love", help='query to search for')
parser.add_argument('num', type=int, default=50, help='Number of questions to return')
args = parser.parse_args()


threshold = args.num
query = args.query

if " " in query:
	out_query = ""
	s = query.split(" ")
	for word in s:
		out_query = out_query + word + "+";
	query = out_query[:-1]
		
		
pagenum = 0
questions = []
index = 0
#lib - crawl specific persons profile, all questions and responses
#format: username, question, response, question, response
#crawl responses to queries. format, question, response, response repsone
print query
while index < threshold:
	url = "http://formspring.blekko.com/ws/?source=e6a5f261&q" + query + "&p=" + str(pagenum)
	#print url
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	#print soup
	results = soup.findAll('div')
	for row in results:
		class_ = row.findAll('h2')
		if class_ != []:
			for i in class_:
				print "~~~~~~~~~~~~"
				matchObj = re.match( r'.*href=(.*)dest.*', str(i))
				qu = matchObj.group(1)
				if "/q/" in qu:
					questions.append(qu)
					index = index + 1
					print qu
	pagenum = pagenum + 1


for qt in questions:
	try:
		q = qt[1:-2]
		print q
		response2 = urllib2.urlopen(q)
		html = response2.read()
		soup = BeautifulSoup(html)
		titleTag = soup.html.head.title
		print titleTag.string	
		print soup('meta', {'property' : 'og:description'})[0]["content"]
	except urllib2.HTTPError:
		pass





