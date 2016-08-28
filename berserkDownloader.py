#! python3
import requests, bs4, os



def soupObject():
    #This creates the soup object
    noStarchSoup = bs4.BeautifulSoup(webPage.text, "lxml")
    type(noStarchSoup)

    elems = noStarchSoup.select('img')
    print(elems[2])

    elemsURL = elems[2].get('src')
    print(elemsURL)

    #download the file
    res = requests.get(elemsURL)
    res.raise_for_status()

def saveImage():
    #TODO How can I change the file name that is created?
    os.makedirs('Berserk %d' % (currVol), exist_ok=True)
    imageFile = open(os.path.join('Berserk %d' % (currVol),os.path.basename(elemsURL)), 'wb')
    print(elemsURL + ' created correctly')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

#Not currently being used
def findATags():
    allATags = noStarchSoup.find_all('a')
    for x in allATags:
        print(x)


currChapter = 0
currVol = 336
while (currVol<339):
    while (currChapter<19):
        webPage = requests.get('http://mangapark.me/manga/berserk/s3/c%d/%d' % (currVol,currChapter))
        print (webPage)
        webPage.raise_for_status()

        #This creates the soup object
        noStarchSoup = bs4.BeautifulSoup(webPage.text, "lxml")
        type(noStarchSoup)

        elems = noStarchSoup.select('img')

        elemsURL = elems[2].get('src')

        #download the file
        res = requests.get(elemsURL)
        res.raise_for_status()

        saveImage()
            
        currChapter = currChapter + 1
    currVol = currVol + 1
    currChapter = 0



#TODO there's no ID for the previous button, how do I select a JS variable?
prevLink = noStarchSoup.select('Prev')
print(prevLink)


