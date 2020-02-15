import sys
import urllib.request
import requests
import json



def getRepositories(UserID):
    r=requests.get(f"https://api.github.com/users/{UserID}/repos")
    
    for i in r.json():
        url2 = f"https://api.github.com/repos/{UserID}/{i['name']}/commits"
        r2 = requests.get(url2)
        
        print(f"Repo: {i['name']} Number of commits: {len(r2.json())}" )
    

if __name__=="__main__":
    
    UserID = input("User ID : ")

    
    res = getRepositories(UserID)
    