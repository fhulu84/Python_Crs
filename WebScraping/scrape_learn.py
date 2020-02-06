import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news') 
# print(res.text) # receive all data from the link as a html, we gonna manipulate and use this data to get what we want
# BeautifulSoup parses this string into an object to manipulate it
soup = BeautifulSoup(res.text, 'html.parser') # BS also parse xml
# print(soup) #not a text, a bit cleaner
# print(soup.body) #only body
# print(soup.body.contents) #all content in a list form
# print(soup.find_all('a')) #all a elements in a list form
# print(soup.title)

# print(soup.find('a')) #first a tag
# print(soup.a) #first a tag

# print(soup.find(id='score_22252330'))

# print(soup.select('div')) #CSS selector

# print(soup.select('.score'))#all elements with a class=score

# print(soup.select('.storylink')[0]) #first link from hackernews

links = soup.select('.storylink')
# votes = soup.select('.score') #we gonna change this bcs some links doesnt have scores
subtexts = soup.select('.subtext')

# print(votes[0].get('id')) #score_22252330 id of the first vote
# print(votes[0].string) #205 points

def sort_stories_by_votes(hn_list):
  return sorted(hn_list, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtexts):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None) #default=None in case of no link
    vote = subtexts[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
    # points = int(votes[idx].getText().replace(' points', '')) #might be error here bcs some links doesnt have votes so links > votes
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtexts))


