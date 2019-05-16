import requests
import re
import cache

github_api = 'https://api.github.com'
headers = {'Accept': 'application/vnd.github.mercy-preview+json'}


def get_github_link(repo_name, user):
    return f'{github_api}/repos/{user}/{repo_name}'

location_regex = re.compile(r'location:([a-zA-Z0-9-]*)')
category_regex = re.compile(r'category:([a-zA-Z0-9-]*)')

def match_github_description(reply_json, regex):
    #return regex.search(reply_json['description'])
    return re.match(regex, 'category:school location:home').group(0)

def get_user_repos(user):
    # repos = requests.get(f'https://api.github.com/users/{user}/repos', headers=headers).json()
    repos = cache.get()
    # return list(map(lambda x: x['description'], repos))
    return parse_descriptions(repos)
    
    # for j in r.json():
      #   repo_name = j["name"]
       #  req = requests.get(f"{get_github_link(repo_name)}/topics", headers=headers)

def parse_descriptions(repos):
    locations = {}
    categories = {}
    return list(map(lambda x: match_github_description(x, location_regex), repos))
    