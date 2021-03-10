from flask import Flask, render_template, request, send_file
from scraper import search_soup, stack_page_link, stack_detail, wework_detail, remotek_detail
from save import save
import csv
import os

os.system("clear")
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""



def web_search(language):
  data_list = []
  stack_url = f"https://stackoverflow.com/jobs?r=true&q={language}"
  wework_url = f"https://weworkremotely.com/remote-jobs/search?term={language}"
  remotek_url = f"https://remoteok.io/remote-dev+{language}-jobs"
  stack_data = stack_detail(stack_url)
  wework_data = wework_detail(wework_url)
  remotek_data = remotek_detail(remotek_url)
  for data in stack_data:
    data_list.append(data)

  for data in wework_data:
    data_list.append(data) 

  for data in remotek_data:
    data_list.append(data)
  return data_list



app = Flask("language Search")

db = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  language = request.args.get('term')
  if language in db:
    data_language=db[language]
  else:
    data_language = web_search(language)
    db[language] = data_language
    save(data_language, language)
  return render_template("detail.html",data = data_language, language = language, number = len(data_language))

@app.route("/export")
def export():
  language = request.args.get('term')
  csv = open(f"csv/{language}.csv")
  return csv.read()


app.run(host="0.0.0.0")