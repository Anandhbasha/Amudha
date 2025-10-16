import pandas as pd

# s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(s1)

# data = {"apple":30,"banana":10,"cherry":70}
# s2 = pd.Series(data,index=["apple","banana","cherry"])
# print(s2)

# print(s1*2)
# print(s1[s1>2])

# print(s1['c'])


# dataframe
# data = {
#     "Name":["arun","Bala","Deepa","Justin"],
#     "age":[20,15,18,22],
#     "City":["Cbe","Erode","Salem","Ooty"]
# }

# df = pd.DataFrame(data,index=[1,2,3,4])
# print(df)


# data list

dl = [
    {"Name":"arun","age":20,"City":"CBE"},
    {"Name":"bala","age":22,"City":"Erode"},
    {"Name":"Ajay","age":18,"City":"Salem"},
]

df_from_list = pd.DataFrame(dl)
# print(df_from_list)

# print(df_from_list.head(1))
# print(df_from_list.tail(1))
# # print(df_from_list.columns)
# # print(df_from_list.shape)
# # print(df_from_list['Name'])
# # print(df_from_list[['Name','City']])

# df_from_list["Degree"] = ["BE","BSC","BSC"]
# # print(df_from_list)
# # print(df_from_list[(df_from_list["Degree"]=="BSC")&(df_from_list['City']=="Erode")])

# # print(df_from_list[df_from_list["City"].isin(["Erode","Salem"])])


# # df_from_list.to_csv("data.csv",index=False)
# # print("Csv file created")


# excelData = pd.read_csv('data.csv')
# # print(excelData)

# # excelData.loc[excelData['Name']=="arun","age"]=21
# # print(excelData)
# # excelData.to_excel("Upadted.xlsx",index=False)


# # excelData.loc[excelData['Degree']=="BSC","Degree"]="Medical"

# excelData["Degree"] = excelData["Degree"].replace("BSC","Medical")
# print(excelData)


# json
import json
data = {
    "Name":["arun","Bala","Deepa","Justin"],
    "age":[20,15,18,22],
    "City":["Cbe","Erode","Salem","Ooty"]
}
print(type(data))

jsonNew = json.dumps(data)
print(type(jsonNew))

dicData = json.loads(jsonNew)
print(type(dicData))