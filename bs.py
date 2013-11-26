from bs4 import BeautifulSoup
import urllib2

u = "http://www.yelp.com/search?find_desc=bar+with+live+music&find_loc=San+Francisco%2C+CA&ns=1#find_desc=hipster+bars"

html_doc = urllib2.urlopen(u).read()
soup = BeautifulSoup(html_doc)

def initSchema():
    """
        Base schema object we will use to hold the translated HTML
    """
    return {
        'name': None,
        'rating':None,
        'neighborhood':None,
        'address':None
        }

def clean(s):
    """
        Give a string, replace all none useful characters
    """
    return s.replace('\t','').replace('\n','')

def getData(tag, h):
    """Get content(text) from an BeautifulSoup object
    given a base tag and an attribute in the form of a hash
    
    ex: <div class="foo"> will be ('div', {'class':'foo'})

    :Parameters:
      - `tag`: html tag name
      - `h`: hash representing the attribute name and value
    """
    d = data.find_all(tag, h)
    if len(d) > 0:
        return str(clean(d.pop().contents[0]))
    return None

data_seg = soup.find_all('div',{'class':'biz-listing-large'})
for data in data_seg:
    schema = initSchema()

    schema['neighborhood'] = getData('span', {'class':'neighborhood-str-list'})
    schema['address'] = getData('address',{})
    schema['name'] = getData('a',{'class':'biz-name'})

    # ratings is special
    rating_data = data.find_all('div',{'class':'rating-large'})
    if len(rating_data) > 0:
        rating = rating_data.pop().contents
        schema['rating'] = rating[1]['title']
    print schema

