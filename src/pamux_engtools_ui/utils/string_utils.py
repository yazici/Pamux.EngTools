class StringUtils:
    GenericKeywords = [ "the", "and", "but" ]

    Separators = [' ', ',', '\t', '.', ';', '/', '_']

    @staticmethod
    def splitex(string: str, separators: list = Separators):
        for separator in separators:
            string = " ".join(string.split(separator))
    
        return string.split()

    @staticmethod
    def isGenericKeyword(extension, keyword: str):
        if extension:
            if keyword == "unity":
                return True;

        if len(keyword) < 2:
            return True
        
        if len(keyword) == 2:
            return keyword != "3d"

        return keyword in StringUtils.GenericKeywords