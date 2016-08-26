#! python3
import requests, bs4, os

os.makedirs('Berserk', exist_ok=True)

#TODO Currently resolves at 20 and then downloads the image at comic 20
currNum = 4
while (currNum<20):
    webPage = requests.get('http://mangapark.me/manga/berserk/s3/c345/%d' % currNum)
    webPage.raise_for_status()
    currNum = currNum + 1

print(webPage)

#This creates the soup object
noStarchSoup = bs4.BeautifulSoup(webPage.text, "lxml")

type(noStarchSoup)

elems = noStarchSoup.select('img')

print(elems[2])

elemsURL = elems[2].get('src')

#download the file
res = requests.get(elemsURL)
res.raise_for_status()

def findATags():
    allATags = noStarchSoup.find_all('a')
    for x in allATags:
        print(x)

def saveImage():
    imageFile = open(os.path.join('Berserk',os.path.basename(elemsURL)), 'wb')   
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

#TODO there's no ID for the previous button, how do I select a JS variable?
prevLink = noStarchSoup.select('Prev')
print(prevLink)


saveImage()

