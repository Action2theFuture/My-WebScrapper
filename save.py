import csv

def save(data_language, language):
  file = open(f"csv/{language}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","link"])
  for data in data_language:
    writer.writerow(list(data.values()))
  
  return 