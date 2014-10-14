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

import re, datetime
from bs4 import BeautifulSoup

#Globals:
global versionNumber
versionNumber = 'none found'


"""  Hard coded variables for testing  """
#fileToClean = "../outputTest.xml"
#testFileStack = []

def findVersion(myString):
    """Finds the first set of <client></client> tags in a MetadataDescribe file and extracts the version number
        
    """
    p = re.compile(r'<client>\S*/(\d*.\d*)</client>') 
    m = p.search(myString)
    return m.group(1)   

def removeBracketLists(fileIn, fileOut): 
    """Removes the string [sf:listMetadata] (followed by 1 whitespace) from each line in a text file)
    
    """
    fileIn = open(fileIn, "r") 
    data = fileIn.read()
    data = re.sub("\[sf\:listMetadata\]\s", "", data)
    #print(data)
    fileIn.close()
    ''''p = re.compile(r'<client>\S*/(\d*.\d*)</client>')
    #p = re.compile(r'<client>\S*(\d\d.\d)</client>')
    m = p.search(data)'''
    global versionNumber 
    versionNumber = findVersion(data)
    print('versionNumber: ' + versionNumber)
    fileOut = open(fileOut, "w")  
    fileOut.write(data)
    fileOut.close()
    print("[sfListMetadata] tags successfully removed" + chr(10))
    
def parseXML(xmlFile):
    """ Takes an XML file and parses the xml using DOM and prints the xmlDoc to stdOut
    
    """
    from xml.dom import minidom
    xmlDoc = minidom.parse(xmlFile)
    xmlDoc
    print(xmlDoc.toxml())
    print("completed")


def filterByDateAndName(xmlFile, startDate, endDate, userName, outputPackage, version, getServiceMaxFields):
    """Takes a well formatted XML File and start and end dates
    call parseXML, filters to just the resultObjects that meet the date criteria and output as a package.xml file
    """
    
    #Commented by DB on 6/5/14 to remove duplicate doc headers
    output = '<?xml version="1.0" encoding="UTF-8"?>' + '\n' + '<Package xmlns="http://soap.sforce.com/2006/04/metadata">' + '\n<types>\n'
    
    #soup = BeautifulSoup(open(xmlFile), "xml")  Requires lxml which requires Visual Studio C++ (2010?)
    try: 
        soup = BeautifulSoup(open(xmlFile), "xml")
    except:
        FileNotFoundError
        soup = BeautifulSoup(xmlFile, "xml")
         
    '''
    endDateTime = datetime.datetime.strptime(endDate, "%Y-%m-%d")
    for result in root.findall('result'):
        lastmodifiedby = result.find('lastModifiedByName').text
        lastmodifieddate = result.find('lastModifiedDate').text
        datePart = datetime.datetime.strptime(lastmodifieddate[0:10], "%Y-%m-%d" )
        #print(lastmodifiedby + " - " + str(datePart) )  #%Y-%m-%d
        #today = datetime.date.today()
        if(datePart - endDate > endDate - endDate):
           print("<members>" + result.find('fullName').text + "</members>    <!-- " + str(lastmodifiedby) + " - " + str(datePart) + "  -->")  #%Y-%m-%d
    
    '''
    
    
    
    #print(soup.result.contents)
    #for result in soup.findAll(["result", "lastModifiedByName", "lastModifiedDate"], recursive=True):
    myType = ''
    nameString = ""
    #responseList = soup.find_all("listMetadataResponse")
    count = soup.find_all("result")
    count = len(count)
    print('Count: ' + str(count) + '\n\n\n')  #+ '\nResponseListLen: ' + str(len(responseList)))
    
    for child in soup.find_all('result'):
        #thisDate = datetime.datetime.strptime('20110930', "%Y-%m-%d%H:%M:%S.%z")
        
        '''  ADDED by DB on 8/8 to get all SVMXC__ Custom Fields for record type permissions  '''
        #print(str(child.type.string))
        '''
        if ( (str(child.type.string) == 'CustomField' or ( str(child.type.string) == 'RecordType' and child.fullName.string.startswith('SVMXC__'))) and child.fullName.string.startswith('SVMXC__')): #and getServiceMaxFields == 1 and child.fullName.string.startswith("SVMXC__") ):
            #print("Success!!!!")
            output = output + '\t<members>' + child.fullName.string + '</members> <!-- ' + str(child.lastModifiedByName.text) + '>   <' + str(child.lastModifiedDate.text) + '-->\n'
            myType = child.type
        '''
        myDateTime = datetime.datetime.strptime(str(child.lastModifiedDate.text), "%Y-%m-%dT%H:%M:%S.%fZ")
        '''********Removed for List Test DB 10/02/14 -- 
        if ( ( (str(child.type.string) == 'CustomField' or  str(child.type.string) == 'RecordType') and getServiceMaxFields==1  and child.fullName.string.startswith('SVMXC__') ) or ((myDateTime > datetime.datetime.strptime(startDate, "%Y-%m-%d") and myDateTime < datetime.datetime.strptime(endDate, "%Y-%m-%d") and ( userName == 'all' or userName == 'All' or str(child.lastModifiedByName.text) == userName )))):'''
        if ( ( (str(child.type.string) == 'CustomField' or  str(child.type.string) == 'RecordType') and getServiceMaxFields==1  and child.fullName.string.startswith('SVMXC__') ) or ((myDateTime > datetime.datetime.strptime(startDate, "%Y-%m-%d") and myDateTime < datetime.datetime.strptime(endDate, "%Y-%m-%d") and ( userName == 'all' or userName == 'All' or str(child.lastModifiedByName.text) in userName )))):
        #if ( ( (str(child.type.string) == 'CustomField' or  str(child.type.string) == 'RecordType') and getServiceMaxFields==1  and child.fullName.string.startswith('SVMXC__') ) or ((datetime.datetime.strptime(str(child.lastModifiedDate.text), "%Y-%m-%dT%H:%M:%S.%fZ") > datetime.datetime.strptime(startDate, "%Y-%m-%d") and datetime.datetime.strptime(str(child.lastModifiedDate.text), "%Y-%m-%dT%H:%M:%S.%fZ") < datetime.datetime.strptime(endDate, "%Y-%m-%d") and ( userName == 'all' or userName == 'All' or str(child.lastModifiedByName.text) == userName )))):
            #output = output + '\t<members>' + child.fullName.string + '</members> <!-- ' + str(child.lastModifiedByName.text) + '>   <' + str(child.lastModifiedDate.text) + '-->\n'
            #print(child.fullName)
            #print(child.lastModifiedByName)
            if myType == '':
                #output = output + '\t<members>' + child.fullName.string + '</members> <!-- ' + str(child.lastModifiedByName.text) + '>   <' + str(child.lastModifiedDate.text) + '-->\n'
                myType = child.type
                #output = output + '\n' + nameString + '\n</types>\n\n<types>\n\n\n\n'
            
            
                  
                
            if (myType != '' and child.type != myType):
                nameString = '\t<name>' + myType.string + '</name>'
                output = output + '\n' + nameString + '\n</types>\n\n<types>\n\n\n'
                output = output + '\t<members>' + child.fullName.string + '</members> <!-- ' + str(child.lastModifiedByName.text) + '>   <' + str(child.lastModifiedDate.text) + '-->\n'
                myType = child.type
                
                print('myType: ' + str(myType))
            else:
                output = output + '\t<members>' + child.fullName.string + '</members> <!-- ' + str(child.lastModifiedByName.text) + '>   <' + str(child.lastModifiedDate.text) + '-->\n'
                myType = child.type
                #print(myType)
            nameString = '\t<name>' + str(child.type.string) + '</name>'
        else: 
            ''' Commented out by DB 8/8'''
            #print(str(child.lastModifiedByName.text) + " - " + str(child.lastModifiedDate.text) + " : " + str(child.type.text) + ":" + str(child.fullName.text))
            
            
                
    #nameString = '\t<name>' + str(child.type.string) + '</name>'
    output = output + '\n'  + nameString + '\n</types>\n'
    output = output + '\n\t' + '<version>'+ version + '</version>\n\n</Package>' 
    
    print(output)
    with open(outputPackage, "w") as fileOut:
        fileOut.write(output)
        fileOut.close()
    return output
    #print(str(count))
    
    '''   Replaced by Beautiful Soup  DB 6/1
    from xml.dom import minidom
    xmlDoc = minidom.parse(xmlFile)
    resultList = xmlDoc.getElementsByTagName('result')
    #print(resultList[0].toxml())
    
    
    #Element.getAttribute(name)
    #Return the value of the attribute named by name as a string. If no such attribute exists, \
    #an empty string is returned, as if the attribute had no value.'''
   
def createXMLReadyFile(myFileStack, fileOutName):
    #with open('..\outputClean.xml', "w") as fileOut:
    with open(fileOutName, "w") as fileOut:
        for f in myFileStack:
            
            fileOut.write(f)
    
    fileOut.close()   
    
def getResults(fileName, fileStack):
    """Takes a file and the listMetadataType 
    and returns a fileStack, a list of cleaned up XML files named 'listMetadata[fileName].xml'
    each full of <Result> Objects
    """
    stringList = []
    lineCount=1 
    with open(fileName, "r") as fileIn:
            lineCount = lineCount + 1
            findResponse = False
            """#Initialize the data variable with the <?xml... tag so since it's static, 
            #this saves us a regex search"""
            data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" #"<?xml version=\"1.0\" encoding=\"UTF-8\"?><env:Envelope"
            """Set responseCount (counts down) to proper number based on listMetadataType"""
            stringList.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" #"<?xml version=\"1.0\" encoding=\"UTF-8\"?><env:Envelope"
            """Set responseCount (counts down) to proper number based on listMetadataType""")
            for line in fileIn:
                """#If this row of the file starts with 'listMetaData'* then we've found a header for 
                a section full of metadata that is ready to convert to an XML file, so we need to set our 
                variables to let the loop know to look for a 'Response'
                """
                listMetadataMatch = re.match("(listMetadata\S*)", line)
                if(listMetadataMatch):
                    findResponse = True
                    #print(str(listMetadataMatch.groups()))
                    print("listMetadataMatch: " + str(line))
                    print ("lineCount: " + str(lineCount))
                    responseCount = 1
                    print("responseCount: " + str(responseCount))
                    data = data + "  <!-- " + str(line) + "  -->" + chr(10) + chr(10)
                    stringList.append("  <!-- " + str(line) + "  -->" + chr(10) + chr(10))
                    fileOutName = re.sub(":\n", ".xml", str(line))
                    print(fileOutName + chr(10))
                    #nameString = fileOutName
                    #fileOut = open(fileOutName,"r+")
                
                    
                """#This whole section of checks fires when we are in a potentially output worthy section of the doc  """      
                if(findResponse):
                    #print("Line: " + str(line))
                    responseStartMatch = re.match("\s*<listMetadataResponse>", line)
                    responseEndMatch = re.match("\s*<\SlistMetadataResponse>", line)  #"       </listMetadataResponse>"
                    
                    
                    """If we have reached the end of the response, write data to a new file out and clean
                    up loose ends     """
                    if(responseEndMatch and responseCount == 0):
                        print("responseEndMatch: True - " + str(lineCount))
                        #data = data + str(line)  Commented by DB 6/5/14
                        stringList.append(str(line))
                        print("FileOutName Appended: ", fileOutName)
                        stringList.append(fileOutName)
                        findResponse = False
                        #fileStack.append(stringList)
                        fileStack.append(data)
                        stringList = []
                        '''
                        fileIn.close()
                        with open(fileName, "w") as fileIn:
                            fileIn.write(data)
                            fileIn.close()
                            '''
                        
                    
                        
                        
                        # DB 5/26
                        #fileOut.write(data)
                        # parseXML(fileOut)
                        #fileOutName
                        #print('fileOutName: ', fileOutName)  # DB 5/26
                        #fileOut.close()
                        #fileStack.append(fileOut)
                        #fileOut.close()
                        data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
                        
                    """If we are at the start of a response, begin appending lines to data  """
                    if(responseStartMatch):
                        print("responseStartMatch: True - " + str(lineCount))
                        lineCount = 1
                        data = data + str(line)
                        stringList.append(str(line))
                        responseCount = responseCount - 1
                    #Add lines between Response Start and End to data for output
                                     
                    if(responseCount == 0 and not responseEndMatch and not responseStartMatch): # and not responseStartMatch ???  
                        xmlMatch = re.match("\s*\<\?xml version=\"1.0\" encoding=\"UTF-8\"\?>", line)
                        """if(envelopeMatch):
                            print("envelopeMatch: " + str(line))
                            data = data + str(line) + "  -->"
                            """
                        """Only append lines if they aren't another <xml?.. tag, as multiple tags make the
                        doc unparseable by the python XML classes (invalid)  """    
                        if(not xmlMatch):
                            #print("Appending line to data")
                            data = data + str(line)
                            stringList.append(str(line))
                            lineCount = lineCount + 1
                    
        
    fileIn.close()
    #fileOut.close() #fix attempt DB 5/26
    return fileStack
    #fileOut = open(fileName, "w")  
    #fileOut.write(data)
    #fileOut.close()
                         

#removeBracketLists(fileToClean)
#getResults(fileToClean, testFileStack)

#file = open("outputTest.xml", "r") 