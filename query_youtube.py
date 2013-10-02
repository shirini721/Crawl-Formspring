import re
import argparse
#xml files from youtube API v2

#parser = argparse.ArgumentParser(description='Query Youtube for Relevant Videos and Comment Pages')
#parser.add_argument('query', default="feminism.xml", help='query to search for')
#parser.add_argument('num', type=int, default=50, help='Number of questions to return')

#args = parser.parse_args()
#print args.query

with open ("feminism.xml", "r") as myfile:
    data=myfile.read()
arr = data.split("<entry>")
metadata = arr[0]

result = re.search('<title type=\'text\'>(.*)</title><logo>', metadata)
search_q = result.group(1)
print search_q

arr = arr[1:]
i = 0
while i < len(arr):
    arr[i] = arr[i].split("</entry")[0] 
    i = i + 1

for element in arr:
    try:
 #       print element
        result = re.search('<gd:comments><gd:feedLink rel=\'http://gdata.youtube.com/schemas/2007#comments\' href=\'(.*)\' countHint=\'\d+\'/></gd:comments>', element)
        comment_url = result.group(1)
        print comment_url
        result = re.search('<link rel=\'alternate\' type=\'text/html\' href=\'(.*)\'/><link rel=\'http://gdata.youtube.com/schemas/2007#video.responses\'', element)
        print "********"
        link_url = result.group(1)
        print link_url
         #        print "----------------"
    except AttributeError:
        pass



