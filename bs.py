from bs4 import BeautifulSoup
import urllib2
import json

URL = "http://www.yelp.com/search?find_desc=bar+with+live+music&find_loc=San+Francisco%2C+CA&ns=1#find_desc=hipster+bars"

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

def getData(soup, tag, h):
    """Get content(text) from an BeautifulSoup object
    given a base tag and an attribute in the form of a hash
    
    ex: <div class="foo"> will be ('div', {'class':'foo'})

    :Parameters:
      - `tag`: html tag name
      - `h`: hash representing the attribute name and value
    """
    d = soup.find_all(tag, h)
    if len(d) > 0:
        return str(clean(d.pop().contents[0]))
    return None


def parse(url):
    """Given an URL u, fetch all data we want into an array of objects
    """
    html_doc = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html_doc)
    results = []

    data_seg = soup.find_all('div',{'class':'biz-listing-large'})

    for data in data_seg:
        schema = initSchema()

        schema['neighborhood'] = getData(data,'span', {'class':'neighborhood-str-list'})
        schema['address'] = getData(data,'address',{})
        schema['name'] = getData(data,'a',{'class':'biz-name'})

        # ratings is special
        rating_data = data.find_all('div',{'class':'rating-large'})
        if len(rating_data) > 0:
            rating = rating_data.pop().contents
            schema['rating'] = rating[1]['title']
        results.append(schema)
    return {'results':results}

if __name__ == "__main__":
    # Export the file
    with open("yelp-results.json","w") as f:
        f.write(json.dumps(parse(URL)))
