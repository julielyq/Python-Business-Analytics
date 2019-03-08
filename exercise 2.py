#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:42:58 2018

@author: liyunqiu
"""
#Yunqiu Li
#Assignment 1
#Exercise 2

import csv

def cleanDataAndSave():
    data_writer = csv.writer(open('exercise2dataClean.csv', 'w', encoding='utf-8', newline=''))
    with open('exercise2data.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for item in row:
                #switch "," to "" in data to make it comparable.
                row[row.index(item)] = item.replace(",","")
                #item.replace won't change the item, keep the value of item updated
                item = item.replace(",","")
                #slice the data to get rid of bracket and the content in it
                if '[' in item:
                    row[row.index(item)] = (item[:item.find('[')])
            row.append(str(int(row[4])/0.386))
            data_writer.writerow(row)

def readCleanedDataAndDisplay():     
    with open('exercise2dataClean.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        sortedListByDensity = sorted(reader, key = lambda row: int(row[4]), reverse = True)
        sortedListByCountry = sorted(sortedListByDensity, key=lambda row: row[5])
        for item in sortedListByCountry:
            print(item)

print("start to read data and save cleaned data.")
cleanDataAndSave()
print("data cleaned and saved")
print("read, sort and print cleaned data in console")
readCleanedDataAndDisplay()
   
    


                        
        


    

