## PS398 Homework 5
## Matthias Orlowski
## 02/21/12
## Script implementing a basic webcrawler to grab liks and meta infos from Matt's blog at http://yspr.wordpress.com/

#!/opt/local/bin/python2.7

import urllib2
import BeautifulSoup
import csv
import sys
from time import sleep
from datetime import date

# First specify some little helpers. They are very specific to the formatting of the blog

def titleOut(input):
    mkstring = str(input)
    out = mkstring[mkstring.find('entry-title">') + 13 : mkstring.find('</h1')]
    return out

def authorOut(input):
    mkstring = str(input)
    out = mkstring[mkstring.find('author">') + 8 : mkstring.find('</a')]
    return out

def dateOut(input):
    mkstring = str(input)
    temp = mkstring[mkstring.find('entry-date">') + 12 : mkstring.find('</span')]
    out = transDate(temp)
    return out

def transDate(stringdate):
    try:
        months = {"January" : 1,"February" : 2,"March" : 3,"April" : 4,"Mai" : 5,"June" : 6,"July" : 7,"August": 8,"September":9,"Oktober":10,"November":11,"December":12}
        sdate = stringdate.split()
        month = months[sdate[0]]
        day = int(sdate[1].rstrip(","))
        year = int(sdate[2])
        outdate = date(year,month,day)
        return outdate
    except:
        return(stringdate)

# now let's crawl

root = 'http://yspr.wordpress.com/'

post_title = []
author = []
publish_date = []
urls = []
comment_count = []
tempurls = []

# grab first site links
home = urllib2.urlopen(root)
shome = BeautifulSoup.BeautifulSoup(home.read())
for link in shome('a'):
    if root in link['href'] and link['href'] not in tempurls:
        tempurls.append(link.get('href'))

# now crawl them
while len(tempurls) > 0:
    for links in tempurls:
        post = urllib2.urlopen(links)
        spost = BeautifulSoup.BeautifulSoup(post.read())

        for link in spost('a'):
            if root in link['href'] and link['href'] not in urls and link['href'] not in tempurls:
                tempurls.append(link.get('href'))

        temptitle = titleOut(spost.findAll("h1", {"class" : "entry-title"}))
        post_title.append(temptitle)

        tempauthor = authorOut(spost.findAll("a", {"rel":"author"}))
        author.append(tempauthor)

        indate = dateOut(spost.findAll("span", {"class" : "entry-date"}))
        publish_date.append(indate)

        comments = spost.findAll("div", {"class":"comment-meta commentmetadata"})
        comment_count.append(len(comments))

        urls.append(tempurls.pop(0))

        sleep(2)


# generate output
Output = []
for i in range(0,len(post_title)):
    Output.append([post_title[i],author[i],str(publish_date[i]), urls[i], comment_count[i]])

# write output into file
with open('yspr_crawl.csv', 'wb') as file:
  csvWriter = csv.writer(file)
  for i in Output:
    csvWriter.writerow(i)
