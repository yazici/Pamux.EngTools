from lxml.html.soupparser import fromstring
from lxml import etree
import time
from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
import os
from Folders import Folders

class ContentInfoBase:
    def __init__(self, searchResult):
        pass

    def getCsvLine(self):
        return f"'{self.title}'\t'{self.href}'\t'{self.imgSrc}'\t'{self.format}'\t'{self.price}'"

    
class Free3dContentInfo(ContentInfoBase):
    def __init__(self, searchResult):
        innerHtmlTree = fromstring("<html><body>" + etree.tostring(searchResult).decode("utf-8") + "</div></body></html>")

        self.imgSrc = innerHtmlTree.xpath("//a[contains(@class,'search-result__thumb-wrapper')]/img/@src")[0]

        titleElement = innerHtmlTree.xpath("//a[contains(@class,'product-page-link') and contains(concat(' ', @class, ' '),' link ')]")[0]

        self.title = titleElement.text
        self.href = titleElement.attrib["href"]

        formatElement = innerHtmlTree.xpath("//span[contains(@class,'search-result__format')]")[0]
        self.format = formatElement.text

        priceElement = innerHtmlTree.xpath("//span[contains(@class,'search-result__price')]")[0]
        self.price = priceElement.text


class BlendSwapContentInfo(ContentInfoBase):
    def __init__(self, searchResult):
        innerHtmlTree = fromstring("<html><body>" + etree.tostring(searchResult).decode("utf-8") + "</body></html>")

        v = etree.tostring(innerHtmlTree).decode("utf-8")

        self.imgSrc = innerHtmlTree.xpath("//img/@src")[0]

        titleElement = innerHtmlTree.xpath("//a[contains(@class,'continue')]")[0]

        self.title = titleElement.text
        self.href = titleElement.attrib["href"]

        self.format = "blend"
        self.price = "FREE"



# <html><body><div assetname="Stone knife" class="thumbnail thumbnail-md" id="Asset19601" thumbcount="7">
# <table cellpadding="0" cellspacing="0">
#<tr>
# < td><a href="https://www.turbosquid.com/3d-models/ancient-stone-knife-3d-model-1160514">
# <img alt="ancient stone knife 3D model" class="" large_url="https://static.turbosquid.com/Preview/001160/514/VK/ancient-stone-knife-3D-model_600.jpg" src="https://static.turbosquid.com/Preview/001160/514/VK/ancient-stone-knife-3D-model_200.jpg"/></a></td>
#</tr>
#</table>
#</div>
#</body></html>
class TurboSquidContentInfo(ContentInfoBase):
    def __init__(self, searchResult):
        innerHtmlTree = fromstring(etree.tostring(searchResult).decode("utf-8"))

        self.title = ""
        try:
            self.title = innerHtmlTree.xpath("//div/@assetname")[0]
        except:
            pass

        try:
            self.title =  self.title + ":"
            self.title =  self.title + innerHtmlTree.xpath("//img/@ALT")[0]
        except:
            pass

        self.imgSrc = innerHtmlTree.xpath("//img/@src")[0]
        self.href = innerHtmlTree.xpath("//a/@href")[0]

        self.format = "???"
        self.price = "FREE"


class CatalogCrawlerBase:
    def __init__(self, urlPrefix, imageUrlPrefix, firstPageUrl, catalogFileNamePrefix):
        self.urlPrefix = urlPrefix
        self.imageUrlPrefix = imageUrlPrefix
        self.firstPageUrl = firstPageUrl
        self.currentPageUrl = firstPageUrl
        self.catalogFileNamePrefix = catalogFileNamePrefix
        
    @staticmethod
    def stringBetweenStrings(s, first, last ):
        try:
            start = s.index(first) + len(first)
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return None

    def getCatalogPage(self):
        try:
            response = urlopen(self.urlPrefix + self.currentPageUrl)
            if (response.status != 200):
                return None
            contentType = response.getheader('Content-Type')
            #if contentType == 'text/html' or contentType == 'text/html; charset=UTF-8':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            return htmlString
        except:
            print(pageUrl + " failed")
            return None

    def getHtmlTree(self, htmlString):
        raise NotImplementedError()

    def getSearchResults(self, htmlString):
        raise NotImplementedError()

    def getNextPageUrl(self, htmlTree):
        raise NotImplementedError()

    def getContentInfo(self, searchResult):
        raise NotImplementedError()
        
    def getCatalogFilePath(self):
        return os.path.join(Folders.ENGTOOLS_DATA, f"{self.catalogFileNamePrefix}.catalog.tsv")
        
       
    def readImageUrls(self):
        self.imageUrls = []
        with open(self.getCatalogFilePath(), "r") as tsvFile:
            for line in tsvFile:
                cols = line.split('\t')
                self.imageUrls.append(cols[2].strip("' \t"))
        return self.imageUrls
            
    def fetchImage(self, i):
        if (i >= len(self.imageUrls)):
            return False
        
        
        imageFileName = self.imageUrls[i][self.imageUrls[i].rfind("/")+1:]
        
        imageFilePath = os.path.join(Folders.ENGTOOLS_DATA, f"{self.catalogFileNamePrefix}", imageFileName)

        try:
            response = urlopen(f"{self.imageUrlPrefix}{self.imageUrls[i]}")
            if (response.status != 200):
                return True
            
            with open(imageFilePath, "wb") as imageFile:
                imageFile.write(response.read())
                
            #print(imageFilePath)
            return True
        except:
            print(pageUrl + " failed")
            return True

        return True
        
    def crawlCatalog(self, useSamplePage = False):
        with open(self.getCatalogFilePath(),"a") as tsvFile:
            self.currentPageUrl = self.firstPageUrl

            while self.currentPageUrl != None:
                print (self.currentPageUrl)

                if (useSamplePage):
                    htmlFile = open(f"{self.catalogFileNamePrefix}.SamplePage.html","r")
                    htmlString = htmlFile.read()
                    htmlFile.close()
                else:
                    htmlString = self.getCatalogPage()

                if (htmlString == None):
                    return

                htmlTree = self.getHtmlTree(htmlString)

                for searchResult in self.getSearchResults(htmlTree):
                    content = self.getContentInfo(searchResult)
                    try:
                        tsvFile.write(content.getCsvLine() + "\n")
                    except:
                        pass

                self.currentPageUrl = self.getNextPageUrl(htmlTree)

                if (useSamplePage):
                    return

                # time.sleep(1)



#https://www.blendswap.com/blends/index/page:1

class BlendSwapCatalogCrawler(CatalogCrawlerBase): 
    # <span class="next disabled">next</span>
    # <span class="next"><a href="/blends/index/page:888" rel="next">next</a></span>

    def __init__(self):
        super().__init__( "https://www.blendswap.com", "https://www.blendswap.com", "/blends/index/page:1", "BlendSwap")

       
    def getHtmlTree(self, htmlString):
        return fromstring(CatalogCrawlerBase.stringBetweenStrings(htmlString, "<!-- the actual content -->", "<!-- ads sidebar if allowed -->"))

    def getSearchResults(self, htmlTree):
        return htmlTree.xpath("//div[contains(@class,'index-blend')]")

    def getNextPageUrl(self, htmlTree):
        e = htmlTree.xpath("//span[@class = 'next']/a/@href")
        if (e == None or len(e) == 0):
            return None
        return e[0]

    def getContentInfo(self, searchResult):
        return BlendSwapContentInfo(searchResult)

#https://free3d.com/3d-models/?page=1
class Free3DCatalogCrawler(CatalogCrawlerBase):

    # (166 pages) on 3/4/2019
    def __init__(self):
        super().__init__("https://free3d.com" , "", "/3d-models/?page=53", "Free3d")


    def getHtmlTree(self, htmlString):
        return fromstring(newString)

    def getSearchResults(self, htmlTree):
        return htmlTree.xpath("//div[contains(@class,'search-result__content-wrapper')]")

    def getNextPageUrl(self, htmlTree):
        e = htmlTree.xpath("//a[contains(@class, 'paging-link__next') and contains(concat(' ' , @class, ' '), ' active ')]")
        if (e == None or len(e) == 0):
            return None
        return e[0].attrib['href']

    def getContentInfo(self, searchResult):
        return Free3dContentInfo(searchResult)




# https://www.turbosquid.com/Search/3D-Models/free?page_num=1
# https://www.turbosquid.com/Search/3D-Models?page_num=2
# next: "https://www.turbosquid.com/Search/3D-Models?page_num=198"

class TurboSquidCatalogCrawler(CatalogCrawlerBase):

    def __init__(self):
        super().__init__("https://www.turbosquid.com/Search/3D-Models/free?page_num=", "", "1", "TurboSquid")


    def getHtmlTree(self, htmlString):
        return fromstring(htmlString)

    def getSearchResults(self, htmlTree):        
        return htmlTree.xpath("//div[contains(@class,'thumbnail-md')]")

    def getNextPageUrl(self, htmlTree):
        nextPageNo = int(self.currentPageUrl)+1
        if (nextPageNo > 197):
            return None
        self.currentPageUrl = str(nextPageNo)
        return self.currentPageUrl

    def getContentInfo(self, searchResult):
        return TurboSquidContentInfo(searchResult)

# htmlString  = Free3DCatalogCrawler.getCatalogPage()



				
# <a href='/3d-model/19-low-poly-buildings-974347.html' class='search-result__thumb-wrapper'>
	# <img class='search-result__thumb' src='https://free3d.com/imgd/s72/5ac9e28b26be8b03368b4567/9766-19-low-poly-buildings.jpg' alt='19 Low Poly Buildings 3d model' title='19 Low Poly Buildings 3d model' rel='{"pret":"&#36;0","type":".c4d .3ds .fbx .obj","standard":null,"imgd":"https:\/\/free3d.com\/imgd\/l72\/5ac9e28b26be8b03368b4567\/9766-19-low-poly-buildings.jpg"}'>
# <div class='standard '>
	# </div>
# </a>
# <div class='search-result__info-wrapper'>
#       <div class='search-result__title'><a href='/3d-model/19-low-poly-buildings-974347.html' class='link product-page-link'>19 Low Poly Buildings</a></div>
#       <span class='search-result__format'>.c4d .3ds .fbx .obj</span>
#       <div class='search-result__footer'>	
#           <span data-price='0' class='search-result__price free  product-page-link'>FREE </span>
#           <span class='search-result__stats'><span class="stat-item downloads">40,399</span></span>
#       </div>
# </div>
			
#  <div class='sec_entry_group'></div>
# <a href='/3d-model/19-low-poly-buildings-974347.html' class='product-tools product-page-link'><span class='product-tool product-tool__zoom'></span></a>

turboSquidCrawler = TurboSquidCatalogCrawler()
turboSquidCrawler.readImageUrls()

free3dCrawler = Free3DCatalogCrawler()
free3dCrawler.readImageUrls()


blendSwapCrawler = BlendSwapCatalogCrawler()
blendSwapCrawler.readImageUrls()

i = 19943
with open(os.path.join(Folders.ENGTOOLS_DATA, "errors.txt"), "a") as errorFile:
    while True:
        try:
            fetched = turboSquidCrawler.fetchImage(i)
            fetched = free3dCrawler.fetchImage(i) or fetched
            fetched = blendSwapCrawler.fetchImage(i) or fetched
        except:
            print(f"failed to fetch {i}")
            errorFile.write(f"failed to fetch {i}\n")
            i = i + 1
            continue
        
        
        print(i)
        if (not fetched):
            break
        time.sleep(0.1)    
        i = i + 1
        
#crawler.crawlCatalog(False)
    

        
print ("DONE")

# <a href="/3d-models/?page=2" class="paging-link paging-link__next active ">Next</a>