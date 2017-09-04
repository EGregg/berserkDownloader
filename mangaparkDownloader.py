#! python3
import requests, bs4, os

mangaName = input("Please paste the exact name of the manga from the URL (e.g. http://mangapark.me/manga/WHAT IS HERE!!!/s5/c135/1: ")

mangaSession = input("Please paste the exact number of the session from the URL (e.g. http://mangapark.me/manga/baki-dou-itagaki-keisuke/WHAT IS HERE!!!/c1/1: ")

beginVol = int(input("What chapter to begin with: "))

endVol = int(input("What chapter to end with: "))


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
    os.makedirs(mangaName + ' %d' % (beginVol), exist_ok=True)
    imageFile = open(os.path.join(mangaName + ' %d' % (beginVol),os.path.basename(elemsURL)), 'wb')
    print(elemsURL + ' created correctly')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

#Not currently being used
def findATags():
    allATags = noStarchSoup.find_all('a')
    for x in allATags:
        print(x)


currChapter = 1
while (beginVol<endVol):
    while (currChapter<22):
        try:
            webPage = requests.get('http://mangapark.me/manga/' + mangaName + '/' + mangaSession + '/c%d/%d' % (beginVol,currChapter))
            #print (webPage)
            webPage.raise_for_status()

            #This creates the soup object
            noStarchSoup = bs4.BeautifulSoup(webPage.text, "lxml")
            type(noStarchSoup)

            elems = noStarchSoup.select('img')
            #print(elems)

            elemsURL = elems[1].get('src')

            #download the file
            res = requests.get(elemsURL)
            res.raise_for_status()

            saveImage()
                
            currChapter = currChapter + 1
        except:
            print("----------------------------------------------------")
            print("Skipping junk file at " + str(elems))
            print("----------------------------------------------------")
            currChapter = 0
            beginVol = beginVol + 1
            pass
    beginVol = beginVol + 1
    currChapter = 0



#TODO there's no ID for the previous button, how do I select a JS variable?
#prevLink = noStarchSoup.select('Prev')
#print(prevLink)

