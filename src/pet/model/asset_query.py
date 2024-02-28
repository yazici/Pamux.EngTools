from utils.string_utils import StringUtils

class AssetQuery:
    def __init__(self, queryText: str):
        self.__queryText = queryText.strip().lower()
        self.__tokens = []

        for token in StringUtils.splitex(self.__queryText):
            token = token.strip()

            if len(token) >= 3 or token == "3d":
                self.__tokens.append(token)

    @property
    def tokens(self):
        return self.__tokens