'''
Created on July 1, 2014
This code is used for the generation of package.xml files based on the lastModifiedBy and lastModifiedDate of each component in a Salesforce.com org.

Copyright (C) 2014  Daniel A Bennett

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
@author: Daniel Bennett
'''


import  re, datetime, cleanAndAppend, bs4 #, TKinter as tk
#import datetime

myFileStack = []
myInputBatResult = 'data\output2-10-07-2014.xml'#'..\debugData.xml'  #'..\OutputEnphase.xml'
myWorkingFile = 'data\myWorkingFile.xml'
myStartDate = '2014-08-08T13:10:22.000Z' #'2014-07-26'
myEndDate = '2014-10-08T00:00:00.000Z'  
myUsername =  'All' #['Daniel Bennett', 'NTTCS Admin']     #'All'
myPackageName = 'data\packageTest.xml'
myGetServiceMaxFields = 0

#Globals:
global myVersionNumber
myVersionNumber=''


def processor(batResult, workFile, startDate='1900-01-01', endDate=str(datetime.date.today())[0:10], username='all', getServiceMaxFields=0):
    """
    Main program that calls functions from the rest of the package
    """
    cleanAndAppend.removeBracketLists(batResult, workFile)
    
    myVersionNumber = cleanAndAppend.versionNumber
    print('myVersionNumber-- ' + myVersionNumber)
    cleanAndAppend.getResults(myWorkingFile, myFileStack)
    cleanAndAppend.createXMLReadyFile(myFileStack, workFile)
    cleanAndAppend.filterByDateAndName(workFile, startDate, endDate, myUsername, myPackageName, myVersionNumber,getServiceMaxFields )
     
    
    #processMetadata.cleanAndAppend.filterByDateAndName(myWorkingFile, startDate, endDate)

def tester(batResult, workFile, startDate='1900-01-01', endDate=str(datetime.date.today())[0:10], username='all', getServiceMaxFields=0):    
    cleanAndAppend.removeBracketLists(batResult, workFile)
    myVersionNumber = cleanAndAppend.versionNumber
    print('myVersionNumber-- ' + myVersionNumber)
    
    
if __name__ == '__main__':
    pass
    print('Running main test...')
    # = tk.Tk()
    processor(myInputBatResult, myWorkingFile, myStartDate, myEndDate , myUsername, myGetServiceMaxFields)
    
    