
import json 

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

    def convertSpecificError(self):
        specificErrors = self.specificE
        newlist=[]
        for specificError in specificErrors:
            temp={}
            for key in specificError.keys():
                temp['Error']=key
                temp['Path'] =specificError[key]
                newPath = []
                errorMapping = {}
                if temp['Path'].keys():
                    temp['ErrorPresent'] = True
                    for path in temp['Path'].keys():
                        errorMapping['filePath']=path
                        errorMapping['errorMessage'] = temp['Path'][path][0]
                        newPath.append(errorMapping)
                else : 
                    temp['ErrorPresent'] = False
                temp['Path']= newPath
            
            newlist.append(temp)
        
        self.specificE = newlist

   


with open("sample.json", "r") as read_file:
        data = json.load(read_file)
    

# ---Class Testing ----

# dataset = sparkLog(data)
# dataset.convertSpecificError()
# print(dataset.specificE)

# for new in dataset.specificE:
#     if new['ErrorPresent']:
#         print('Yo')
#         for allMssg in new['Path']:
#             print(allMssg['errorMessage'])




# ----Testing Purpose------
# specificErrors=data['SpecificError']
# newlist=[]
# for specificError in specificErrors:
#     temp={}
#     for key in specificError.keys():
#         temp['Error']=key
#         temp['Path'] =specificError[key]
#         newPath = []
#         errorMapping = {}
        
#         if temp['Path'].keys():
#             temp['ErrorPresent'] = True
#             for path in temp['Path'].keys():
#                 errorMapping['filePath']=path
#                 errorMapping['errorMessage'] = temp['Path'][path]
#                 newPath.append(errorMapping)
#         else : 
#             temp['ErrorPresent'] = False
#         temp['Path']= newPath  
#     newlist.append(temp)

# print('Lets see the new list ')
   
# for new in newlist:
#     if new['ErrorPresent']:
#         print('Yo')
#         for allMssg in new['Path']:
#             # print(allMssg['errorMessage'])

#             # tempList = allMssg['errorMessage']
#             # print((tempList[0]))

#             print(allMssg['errorMessage'][0])