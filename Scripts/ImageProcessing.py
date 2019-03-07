import sys
import os
from PIL import Image

class Texture:
    def __init__(self, filePath):
        self.filePath = filePath
        self.img = Image.open(filePath)
        
    def Save(self, fileNamePrefix):
        folderName, fileName = os.path.split(self.filePath)        
        self.img.save(os.path.join(folderName, f"{fileNamePrefix}.{fileName}"))
        
    def MakeSquare(self):
        sz = self.img.size
        if (sz[0] == sz[1]):
            return
        
        if (sz[0] < sz[1]):
            newSize = sz[0]
        else:
            newSize = sz[1]
            
        self.img = self.img.resize((newSize, newSize))
        
    def MakeSeamless(self):
        sz = self.img.size
        region = []
        for i in range(4):
            region += [self.img.crop((0,0,sz[0],sz[1]))]
        self.img = self.img.resize((sz[0] * 2, sz[1] * 2))
        
        region[1] = region[1].transpose(Image.FLIP_TOP_BOTTOM)
        
        region[2] = region[2].transpose(Image.FLIP_LEFT_RIGHT)
        
        region[3] = region[3].transpose(Image.FLIP_TOP_BOTTOM)
        region[3] = region[3].transpose(Image.FLIP_LEFT_RIGHT)
        
        self.img.paste(region[0], ((0,0,sz[0],sz[1])))
        self.img.paste(region[1], ((0,sz[1],sz[0],sz[1]*2)))
        self.img.paste(region[2], ((sz[0],0,sz[0]*2,sz[1])))
        self.img.paste(region[3], ((sz[0],sz[1],sz[0]*2,sz[1]*2)))
        
# mst C:/assets/Pamux/03062019/RemovedWM/Natural_Sea_Sand_Background_Texture-741.jpg
class ImageProcessing:
    def MakeSeamlessTexture(inFilePath):
        texture = Texture(inFilePath)
        texture.MakeSquare()
        texture.MakeSeamless()
        texture.Save("Seamless")