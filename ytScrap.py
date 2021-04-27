from selenium import webdriver
from bs4 import BeautifulSoup
import json
from time import sleep

urls = [
  'TheCodingTrain',
  'Freecodecamp',
  
]

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False)

def main():
  
  driver = webdriver.Chrome()
  
  for url in urls:
    driver.get('https://www.youtube.com/c/{}/videos?view=0&sort=dd&shelf_id=0'.format(url))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.findAll('a', id='video-title')
    video_urls = soup.findAll('a', id='thumbnail')
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = 0
    data = []
    for title in titles:
      #print('\n\"title\": \"{}\",\n\"video_urls\": \"https://www.youtube.com/embed/{}\",'.format(title.text, video_urls[i].get('href').split("=",1)[1]))
      title = title.text
      video_url = video_urls[i].get('href').split("=",1)[1]
      i+=1
      data.append({
        "id": i,
        "title": title,
        "video_url": video_url,
      }) 
    filename = 'videos'
    writeToJSONFile('./', filename, data)
    

main()