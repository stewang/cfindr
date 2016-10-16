
import urllib2
url="http://www.wsj.com/articles/salesforce-won-t-pursue-bid-for-twitter-1476468050"
page = urllib2.urlopen(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page,"html.parser")
#highlighted the text and looked for id name
for content in soup.find_all('div', {"id":"wsj-article-wrap"}):
   print content.text
#The random -.63% comes from stock changes in the day. This is because whenever wsj mentions a company, the name in the text is linked
#to wall street journal's stock page and the number is just the max change during the day. This is included because the <a> tag
#is included in the id "wsj-article-wrap" I couldn't get it to be any more specific because there wasn't a class for all the paragraph
#types but this should be specific enough for now. 





