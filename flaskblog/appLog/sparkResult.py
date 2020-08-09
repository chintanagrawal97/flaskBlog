

class sparkLog():
    def __init__(self,data):
        self.specificE = data['SpecificError']
        self.filepath = data['filepath']
        self.res = data['res']
        self.flag = data['flag']
        self.Keyword = data['Keyword']
        self.KeywordLen = data['KeywordLen']
        self.resLen = data['resLen']
        self.specificW = data['SpecificWarn']
        self.flag = data['flag']

        