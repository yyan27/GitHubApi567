import requests
import json


def get_git_info(user_name):
    
    resq = requests.get("https://api.github.com/users/" + user_name + "/repos")
    repos_list = json.loads(resq.text)
    result = []
    result.append('User: ' + user_name)
    
    try:
        repos_list[0]
    except:
        return 'unable to fetch repositories from user'

    for repo in repos_list:
        rep_name = repo['name']
        repo_info = requests.get("https://api.github.com/repos/" + user_name + "/" + rep_name + "/commits")
        repo_info_text = json.loads(repo_info.text)
        result.append("Repo: " + rep_name + " Number of commits: " + str(len(repo_info_text)))

    return result


# if __name__ == '__main__':
#     for i in get_git_info("yyan27"):
#         print(i)