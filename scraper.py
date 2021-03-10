import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def search_soup(url):
  data = requests.get(url, headers=headers)
  soup = BeautifulSoup(data.text, "html.parser")
  return soup

def stack_page_link(stack_url):
  link_list = []
  soup = search_soup(stack_url)
  stack_a = soup.find("div",{"class":"s-pagination"}).find_all('a')
  for page in stack_a[:-1]:
    if page != None:
      link_list.append(page["href"])
  return link_list
  

def stack_detail(stack_url):
  stack_list = []
  page_link_list = stack_page_link(stack_url)
  for page_link in page_link_list:
    soup = search_soup(f"https://stackoverflow.com/{page_link}")
    stack = soup.find_all("div",{"class":"grid--cell fl1"})
    for detail in stack:
      try:
        title = detail.find("h2", {"class":"mb4"}).find("a").text
        company = detail.find("h3", {"class":"mb4"}).span.text.strip()
        link = detail.find("h2", {"class":"mb4"}).find("a")["href"]
        stack_list.append({
          "title" : title,
          "company" : company,
          "link" : "https://stackoverflow.com" + link
        })
      except:
        print("")
  return stack_list

def wework_detail(wework_url):
  wework_list = []
  soup = search_soup(wework_url)
  wework = soup.find_all("li", {"class":"feature"})
  for detail in wework:
    try:
      title = detail.find("span", {"class":"title"}).text
      company = detail.find("span", {"class":"company"}).text
      link = detail.find("a")["href"]
      wework_list.append({
            "title" : title,
            "company" : company,
            "link" : "https://weworkremotely.com" + link
          })
      
    except:
      print("")
  return wework_list

def remotek_detail(remotek_url):
  remotek_list = []
  soup = search_soup(remotek_url)
  remotek = soup.find_all("td", {"class" : "company position company_and_position"})
  for detail in remotek:
      try:
        title = detail.find("h2").text
        link = detail.find("a")["href"]
        company = detail.find("a", {"class" : "companyLink"}).h3.text
        remotek_list.append({
            "title": title,
            "company": company,
            "link": "https://remoteok.io" + link 
        })
      except:
        print("")
       
  return remotek_list