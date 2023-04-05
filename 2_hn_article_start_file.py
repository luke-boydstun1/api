import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

outfile = open('hm.json', 'w')
json.dump(r.json(), outfile, indent=4)

submissionIDsList = r.json()

# Explore the structure of the data.
url = 'https://hacker-news.firebaseio.com/v0/item/35455770.json'
r = requests.get(url)
outfile = open('hm2.json','w')
json.dump(r.json(), outfile, indent=4)

# for i in submissionIDsList[:21]:
#     url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
#     r = requests.get(url)
#     dictionary = r.json()
#     print('--------------------------------')
#     print("Author:", dictionary["by"])
#     if "descendants" in dictionary: 
#         print("Likes:", dictionary["descendants"])
#     else:
#         print("Likes: 0")
#     print(f"URL: http://news.ycombinator.com/item?id={i}")

entries = []
for i in submissionIDsList[:21]:
    entry = {}
    url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
    r = requests.get(url)
    dictionary = r.json()

    entry["author"] = dictionary["by"]
    if "descendants" in dictionary: 
        entry["comments"]= dictionary["descendants"]
    else:
        entry["comments"] = 0
    entry["url"] = f"http://news.ycombinator.com/item?id={i}"
    entries.append(entry)

from operator import itemgetter

entries = sorted(entries, key=itemgetter('comments'), reverse=True)

for x in entries:
    print('---------------------------------')
    print("Author:", x["author"])
    print("Comments:", x["comments"])
    print("URL:", x["url"])