import mysql.connector as mysql
import json
import csv
import xlsxwriter
import pymongo

dbku = mysql.connect(
                     host = 'localhost',
                     port = 3306,
                     user = 'root',
                     passwd = 'F12345',
                     auth_plugin = 'mysql_native_password',
                     db = 'world'
)


cursor = dbku.cursor(dictionary=True)

# table city
cursor.execute('select * from city')
dataJsonCity = cursor.fetchall()
with open('city.json', 'w') as myjson:
    json.dump(dataJsonCity, myjson)

with open('city.csv','w') as mycsv:
    writer = csv.DictWriter(mycsv, delimiter = ';',fieldnames=['ID', 'Name', 'CountryCode', 'District', 'Population'])
    writer.writerows(dataJsonCity)

book = xlsxwriter.Workbook('city.xlsx')
sheet = book.add_worksheet('Sheet 1')

dataExcelCity = []
for data in dataJsonCity:
    dataExcelCity += [list(data.values())]
row = 0
for ID, Name, CountryCode, District, Population in dataExcelCity:
    sheet.write(row, 0, 'ID')
    sheet.write(row, 1, 'Name')
    sheet.write(row, 2, 'CountryCode')
    sheet.write(row, 3, 'District')
    sheet.write(row, 4, 'Population')
row = 1
for ID, Name, CountryCode, District, Population in dataExcelCity:
    sheet.write(row, 0, ID)
    sheet.write(row, 1, Name)
    sheet.write(row, 2, CountryCode)
    sheet.write(row, 3, District)
    sheet.write(row, 4, Population)
    row += 1
book.close()

# table Country
cursor.execute('select * from country')
dataJsonCountry = cursor.fetchall()

keys = []
values = []
for data in dataJsonCountry:
    for i in data.values():
        values.append(str(i))
    for k in data.keys():
        keys.append(k)

countryDict = []
counter = 0
while counter < len(keys):
    for i in range(counter,counter+1):
        dicti = {keys[i]:[values[i]]}
        for j in range(i,i+15):
            dicti2 = {keys[j]:values[j]}
            dicti.update(dicti2)
        countryDict.append(dicti)
    counter += 15

with open('country.json', 'w') as myjson:
    json.dump(countryDict, myjson)

with open('country.csv','w') as mycsv:
    writer = csv.DictWriter(mycsv, delimiter = ';',fieldnames=['Code', 'Name', 'Continent', 'Region', 'SurfaceArea', 'IndepYear',
                                                               'Population', 'LifeExpectancy', 'GNP', 'GNPOld', 'LocalName',
                                                               'GovernmentForm', 'HeadOfState', 'Capital', 'Code2'])
    writer.writerows(countryDict)

book = xlsxwriter.Workbook('country.xlsx')
sheet = book.add_worksheet('Sheet 1')

dataExcelCountry = []
for data in countryDict:
    dataExcelCountry += [list(data.values())]
row = 0
for Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2 in dataExcelCountry:
    sheet.write(row, 0, 'Code')
    sheet.write(row, 1, 'Name')
    sheet.write(row, 2, 'Continent')
    sheet.write(row, 3, 'Region')
    sheet.write(row, 4, 'SurfaceArea')
    sheet.write(row, 5, 'IndepYear')
    sheet.write(row, 6, 'Population')
    sheet.write(row, 7, 'LifeExpectancy')
    sheet.write(row, 8, 'GNP')
    sheet.write(row, 9, 'GNPOld')
    sheet.write(row, 10, 'LocalName')
    sheet.write(row, 11, 'GovernmentForm')
    sheet.write(row, 12, 'HeadOfState')
    sheet.write(row, 13, 'Capital')
    sheet.write(row, 14, 'Code2')
row = 1
for Code, Name, Continent, Region, SurfaceArea, IndepYear, Population, LifeExpectancy, GNP, GNPOld, LocalName, GovernmentForm, HeadOfState, Capital, Code2 in dataExcelCountry:
    sheet.write(row, 0, Code)
    sheet.write(row, 1, Name)
    sheet.write(row, 2, Continent)
    sheet.write(row, 3, Region)
    sheet.write(row, 4, SurfaceArea)
    sheet.write(row, 5, IndepYear)
    sheet.write(row, 6, Population)
    sheet.write(row, 7, LifeExpectancy)
    sheet.write(row, 8, GNP)
    sheet.write(row, 9, GNPOld)
    sheet.write(row, 10, LocalName)
    sheet.write(row, 11, GovernmentForm)
    sheet.write(row, 12, HeadOfState)
    sheet.write(row, 13, Capital)
    sheet.write(row, 14, Code2)
    row += 1
book.close()

# table Country Language
cursor.execute('select * from countrylanguage')
dataJsonCountryLanguage = cursor.fetchall()

keys = []
values = []
for data in dataJsonCountryLanguage:
    for i in data.values():
        values.append(str(i))
    for k in data.keys():
        keys.append(k)

countryLanguageDict = []
counter = 0
while counter < len(keys):
    for i in range(counter,counter+1):
        dicti = {keys[i]:values[i]}
        for j in range(i,i+4):
            dicti2 = {keys[j]:values[j]}
            dicti.update(dicti2)
        countryLanguageDict.append(dicti)
    counter += 4

print(countryLanguageDict)
with open('countryLanguage.json', 'w') as myjson:
    json.dump(countryLanguageDict, myjson)

with open('countryLanguage.csv','w') as mycsv:
    writer = csv.DictWriter(mycsv, delimiter = ';',fieldnames=['CountryCode', 'Language', 'IsOfficial', 'Percentage'])
    writer.writerows(countryLanguageDict)

book = xlsxwriter.Workbook('countryLanguage.xlsx')
sheet = book.add_worksheet('Sheet 1')

dataExcelCountryLanguage = []
for data in countryLanguageDict:
    dataExcelCountryLanguage += [list(data.values())]
row = 0
for CountryCode, Language, IsOfficial, Percentage in dataExcelCountryLanguage:
    sheet.write(row, 0, 'CountryCode')
    sheet.write(row, 1, 'Language')
    sheet.write(row, 2, 'IsOfficial')
    sheet.write(row, 3, 'Percentage')
row = 1
for CountryCode, Language, IsOfficial, Percentage in dataExcelCountryLanguage:
    sheet.write(row, 0, CountryCode)
    sheet.write(row, 1, Language)
    sheet.write(row, 2, IsOfficial)
    sheet.write(row, 3, Percentage)
    row += 1
book.close()

# to mangoDB
urldb = 'mongodb://localhost:27017'
mongoku = pymongo.MongoClient(urldb)

dbku = mongoku['world'] # use ptabc
collCity = dbku['city']
send = collCity.insert_many(dataJsonCity)
print(send.inserted_ids)

collCountry = dbku['country']
send = collCountry.insert_many(countryDict)
print(send.inserted_ids)

collCountryLanguage = dbku['countryLanguage']
send = collCountryLanguage.insert_many(countryLanguageDict)
print(send.inserted_ids)
