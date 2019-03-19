import sys
import os
import shutil
import re

class MakeHuman:
    ENCOUNTERED_MODIFIERS = set()
    
    def __init__(self):
        pass
        
        
    @staticmethod
    def IsModifier(aLine):
        return aLine.startswith("modifier ")
        
    @staticmethod
    def IsSymmetricModifier(aLine):
        return  
        
        
    # modifier mouth/mouth-cupidsbow-decr|incr -0.188000
    # modifier ears/r-ear-trans-backward|forward 0.035764
    @staticmethod
    def EnsureModifierSymmetry(aLine):
        parts = re.split("[\s\/]", aLine)
        modifierName = parts[2]
        if modifierName.startswith("r-"):
            otherModifierPrefix = "l-"
        else:
            otherModifierPrefix = "r-"
            
        modifierSuffix = modifierName[2:]
        if modifierSuffix in MakeHuman.ENCOUNTERED_MODIFIERS:
            return
        MakeHuman.ENCOUNTERED_MODIFIERS.add(modifierSuffix)
        
        thisModifier = parts[1] + "/" + modifierName
        otherModifier = parts[1] + "/" + otherModifierPrefix + modifierSuffix
        
        modifierValue = parts[3]
        print(f"modifier {thisModifier} {modifierValue}")
        print(f"modifier {otherModifier} {modifierValue}")
        
    @staticmethod
    def SymmetrizeHuman(mhmFilePath):
        print (mhmFilePath)
        shutil.copyfile (mhmFilePath, f"{mhmFilePath}.backup")
        lines = list(open(mhmFilePath))  # list of strings
        
        for aLine in lines:
            aLine = aLine.strip()
            if MakeHuman.IsModifier(aLine):
                if ("/r-" in aLine or "/l-" in aLine):
                    MakeHuman.EnsureModifierSymmetry(aLine)
                    continue
                    
            print(aLine)

        pass
   
if __name__ == "__main__":
    MakeHuman.main()

