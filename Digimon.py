from bs4 import BeautifulSoup
import requests
import json
import csv
import xlsxwriter
import pymongo
import mysql.connector as mysql

# http://digidb.io/digimon-list/ <=> json , csv, excel, 
# mongodb db = digimon collections=digimon , 
# mysql db = digimon, table = digimon
# feature = web ( 13col ) + picture (link saja)


url = 'http://digidb.io/digimon-list/'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

x = soup.find('tbody')
findId  = x.find_all('b')
findImg = x.find_all('img')
findName = x.find_all('a')
findStage = x.find_all('center')

digiId = []
digiImg = []
digiName = []

listAttr = []

for item in findId:
    digiId.append(item.text.replace('\xa0',''))
for item in findImg:
    digiImg.append(item['src'])
for item in findName:
    digiName.append(item.text)
for item in findStage:
    listAttr.append(item.text)

digiStage = listAttr[::11]
digiType = listAttr[1::11]
digiAttribute = listAttr[2::11]
digiMemory = listAttr[3::11]
digiEquipSlots = listAttr[4::11]
digiHP = listAttr[5::11]
digiSP = listAttr[6::11]
digiAtk = listAttr[7::11]
digiDef = listAttr[8::11]
digiInt = listAttr[9::11]
digiSpd = listAttr[10::11]

allData = list(zip(digiId, digiImg, digiName, digiStage, digiType, digiAttribute, digiMemory, digiEquipSlots, digiHP, digiSP, digiAtk, digiDef, digiInt, digiSpd))
allDataList = []
for data in allData:
    allDataList.append(list(data))

# to excel
book = xlsxwriter.Workbook('digimon.xlsx')
sheet = book.add_worksheet('Sheet 1')

row = 0
for ID, Image, Digimon, Stage, Type, Attribute, Memory, Equip, HP, SP, Atk, Def, Int, Spd in allDataList:
    sheet.write(row, 0, 'ID')
    sheet.write(row, 1, 'Image')
    sheet.write(row, 2, 'Digimon')
    sheet.write(row, 3, 'Stage')
    sheet.write(row, 4, 'Type')
    sheet.write(row, 5, 'Attribute')
    sheet.write(row, 6, 'Memory')
    sheet.write(row, 7, 'Equip Slots')
    sheet.write(row, 8, 'HP')
    sheet.write(row, 9, 'SP')
    sheet.write(row, 10, 'Atk')
    sheet.write(row, 11, 'Def')
    sheet.write(row, 12, 'Int')
    sheet.write(row, 13, 'Spd')
row = 1
for ID, Image, Digimon, Stage, Type, Attribute, Memory, Equip, HP, SP, Atk, Def, Int, Spd in allDataList:
    sheet.write(row, 0, ID)
    sheet.write(row, 1, Image)
    sheet.write(row, 2, Digimon)
    sheet.write(row, 3, Stage)
    sheet.write(row, 4, Type)
    sheet.write(row, 5, Attribute)
    sheet.write(row, 6, Memory)
    sheet.write(row, 7, Equip)
    sheet.write(row, 8, HP)
    sheet.write(row, 9, SP)
    sheet.write(row, 10, Atk)
    sheet.write(row, 11, Def)
    sheet.write(row, 12, Int)
    sheet.write(row, 13, Spd)
    row += 1

book.close()

# to Json
listOfDict = []
for i in range(len(allDataList)):
    dictID = {'ID':allDataList[i][0]}
    dictImg = {'Img':allDataList[i][1]}
    dictDigimon = {'Digimon':allDataList[i][2]}
    dictStage = {'Stage':allDataList[i][3]}
    dictType = {'Type':allDataList[i][4]}
    dictAttribute = {'Attribute':allDataList[i][5]}
    dictMemory = {'Memory':allDataList[i][6]}
    dictEquip = {'Equip Slots':allDataList[i][7]}
    dictHP = {'HP':allDataList[i][8]}
    dictSP = {'SP':allDataList[i][9]}
    dictAtk = {'Atk':allDataList[i][10]}
    dictDef = {'Def':allDataList[i][11]}
    dictInt = {'Int':allDataList[i][12]}
    dictSpd = {'Spd':allDataList[i][13]}
    dictID.update(dictImg)
    dictID.update(dictDigimon)
    dictID.update(dictStage)
    dictID.update(dictType)
    dictID.update(dictAttribute)
    dictID.update(dictMemory)
    dictID.update(dictEquip)
    dictID.update(dictHP)
    dictID.update(dictSP)
    dictID.update(dictAtk)
    dictID.update(dictDef)
    dictID.update(dictInt)
    dictID.update(dictSpd)
    listOfDict.append(dictID)

with open('Digimon.json', 'w') as myjson:
    json.dump(listOfDict, myjson)

# to csv
with open('Digimon.csv', 'w', newline='') as mycsv:
    writer = csv.DictWriter(mycsv, delimiter = ';',fieldnames=['ID', 'Img', 'Digimon', 'Stage', 'Type', 'Attribute', 'Memory', 'Equip Slots', 'HP',
                                                               'SP', 'Atk', 'Def', 'Int', 'Spd'])
    writer.writerow(
        {'ID':'ID', 'Img':'Img', 'Stage':'Stage', 'Type':'Type', 'Attribute': 'Attribute', 'Memory': 'Memory', 'Equip Slots': 'Equip Slots', 'HP': 'HP',
                                                                   'SP': 'SP', 'Atk': 'Atk', 'Def': 'Def', 'Int': 'Int', 'Spd': 'Spd'}
        )
with open('Digimon.csv', 'a', newline='') as mycsv:
    writer = csv.DictWriter(mycsv, delimiter = ';',fieldnames=['ID', 'Img', 'Digimon', 'Stage', 'Type', 'Attribute', 'Memory', 'Equip Slots', 'HP',
                                                               'SP', 'Atk', 'Def', 'Int', 'Spd'])
    writer.writerows(listOfDict)

# to mongoDB
urldb = 'mongodb://localhost:27017'
mongoku = pymongo.MongoClient(urldb)
mydb = mongoku['digimon'] # use digimon
mycolls = mydb['digimon'] # db.createCollection('digimon')

send = mycolls.insert_many(listOfDict)
print(send.inserted_ids)

# to mysql
dbku = mysql.connect(
                     host = 'localhost',
                     port = 3306,
                     user = 'root',
                     passwd = 'F12345',
                     auth_plugin = 'mysql_native_password'
 )

cursor = dbku.cursor()
cursor.execute('create database digimon')
cursor.execute('use digimon')
cursor.execute('''create table digimon2 (
               ID varchar(100),
               Image varchar(100),
               Digimon varchar(100),
               Stage varchar(100),
               Type varchar(100),
               Attribute varchar(100),
               Memory varchar(100),
               Equip varchar(100),
               HP varchar(100),
               SP varchar(100),
               Atk varchar(100),
               Def varchar(100),
               `Int` varchar(100),
               Spd varchar(100)
               )''')

dataTuple = []
for data in allDataList:
    tple = tuple(data)
    dataTuple.append(tple)

queryku = 'insert into digimon values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)'
datanew = dataTuple
cursor.executemany(queryku, datanew)

dbku.commit()
print(cursor.rowcount, 'data sukses tersimpan!')
