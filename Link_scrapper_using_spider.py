import requests
from  bs4 import BeautifulSoup





def extract_all_links(site):
    html = requests.get(site).text
    soup =BeautifulSoup(html,"html.parser").find_all("a")
    link = [link.get('href') for link in soup]
    return link



if __name__=="__main__":
    site_link = input("Enter the Url:")
    all_links = extract_all_links(site_link)
    print("The Links provided in the URL are as Follows: ")
    print(all_links)
    