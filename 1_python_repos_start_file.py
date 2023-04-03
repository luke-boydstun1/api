import requests
import json
import plotly
from plotly import offline


# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") 

outfile = open('output.json','w')
response_dict = r.json()
json.dump(response_dict,outfile,indent=4)

list_of_repos = response_dict["items"]

print(f"Number of repos: {len(list_of_repos)}")
first_repo = list_of_repos[0]
print("----------------------------------------------------")
print(f"Name of repo: {first_repo['name']}")
print(f"Owner of repo: {first_repo['owner']['login']}")
print(f"number of stars: {first_repo['stargazers_count']}")
print(f"repo url: {first_repo['html_url']}")
print(f"Created at: {first_repo['created_at']}")
print(f"Last updated: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}\n")

repos = []
stars = []
for repo in list_of_repos[:10]:
    repos.append(repo['name'])
    stars.append(repo['stargazers_count'])

data = [{
    "type":"bar",
    "x":repos,
    "y":stars,
    "marker":{
        "color":"rgb(60,100,150)",
        "line":{"width":1.5,"color":"rgb(60,100,150)"},
    },
    "opacity":0.6,
}]

my_layout = {
    "title": "Most-Shared Pyhton Projects on GitHub",
    "xaxis":{"title":"Repository"},
    "yaxis":{"title":"Stars"}
}

fig = {"data":data,"layout":my_layout}
offline.plot(fig, filename="python_repos.html")

'''
print
name of repo
owner
number of stars
repo url
when it was created
when it was last updated
description
'''