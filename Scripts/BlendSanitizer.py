import sys
import os
import shutil
import bpy
import space_view3d_panel_measure as pm

class BlendSanitizer:
    
    def SetMetricUnits(self):
        scene = bpy.context.scene
        uinfo = pm.getUnitsInfo()
        print("Setting Blend Units To METRIC")
    
    def Save(self):
        print("Saving Blend")
        
    
    def Sanitize(self):
        self.SetMetricUnits()
        return True
          
            
    
    
    
print(__name__)

# c:/apps\blender-2.80-18e5540a48b6-win64\blender.exe --background 
# --python C:\src\Pamux\Pamux.EngTools\Scripts\BlendSanitizer.py
#  C:/assets/04102019_BlendSwap\unpacked\14092_Greeble-material.zip\greeble_texture.blend
#print(sys.argv[0]) # c:/apps\blender-2.80-18e5540a48b6-win64\blender.exe
#print(sys.argv[1]) # --background
#print(sys.argv[2]) # --python
#print(sys.argv[3]) # C:\src\Pamux\Pamux.EngTools\Scripts\BlendSanitizer.py
#print(sys.argv[4]) # C:/assets/04102019_BlendSwap\unpacked\14092_Greeble-material.zip\greeble_texture.blend

if __name__ == "__main__":
    bs = BlendSanitizer()
    if bs.Sanitize():
        bs.Save()
