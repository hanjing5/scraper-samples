from bs4 import BeautifulSoup
import urllib2


u = "http://www.yelp.com/search?find_desc=bar+with+live+music&find_loc=San+Francisco%2C+CA&ns=1#find_desc=hipster+bars"

html_doc = urllib2.urlopen(u).read()


#print html_doc
soup = BeautifulSoup(html_doc)

#for link in soup.find_all('a'):
#    print(link.get('href'))

schema = {
        'name': None,
        'rating':None,
        'neightborhood':None,
        'address':None
        }

def getData(tag, h):
    d = data.find_all(tag, h)
    if len(d) > 0:
        return d.pop().contents
    return None

data_seg = soup.find_all('div',{'class':'biz-listing-large'})
for data in data_seg:

    neighborhood_d = data.find_all('span',{'class':'neighborhood-str-list'})
    if len(neighborhood_d) > 0:
        neightborhood = d.pop().contents

    address_d = data.find_all('address',{'class':'neighborhood-str-list'})
    if len(address_d) > 0:
        address = address_d.pop().contents

    address_d = data.find_all('address',{'class':'neighborhood-str-list'})
    if len(address_d) > 0:
        address = address_d.pop().contents

