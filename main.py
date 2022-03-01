#Packages and modules
import requests
from bs4 import BeautifulSoup
import pprint

#This function shows stories sorted by votes.
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse= True)


#Title
def title():
    print('='*40)
    projname = 'Hacker News Reader!'
    print(f'{projname:^40}')
    print('='*40)

#Main function
def create_custom_hn(links, vote):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points >= vote_filter:
                hn.append({'title' : title, 'link' : href, 'votes' : points})
    return sort_stories_by_votes(hn)


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

title()
try:
    vote_filter = int(input('Minimum votes to show: '))
except:
    print('Please enter a number.')
pprint.pprint(create_custom_hn(links, subtext))