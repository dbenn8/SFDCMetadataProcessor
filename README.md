SFDCMetadataProcessor
=====================

This code is used for the generation of package.xml files based on the lastModifiedBy and lastModifiedDate of each component in a Salesforce.com org.

*****************************************************************************
Copyright (C) 2014  Daniel A Bennett
Created on Jan 21, 2014

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

*****************************************************************************

SUMMARY

This combination of .bat files, ANT Files, and Python Scripts can be used to automate the creation of a package.xml file comprised of all of the components lastModified within a data range and by All or any user.  The .Bat file uses the ANT files to run the listMetaData() command for most component types, appending them all in a single text file.  You will need to supply SFDC login credentials in the build.properties file in the typical manner.

The main.py file uses a number of variables to process the single text file generated above, converting the file to valid xml, appending lastModifiedBy and lastModifiedDate info to each component, and finally creating a package.xml file containing just the components that meet the modifiedBy and date criteria set in the main.py variables.

The Latest Version
  ------------------

  Details of the latest version can be found on the github project page under 


Licensing
  ---------

This code is distributed under the GPL 2.0 license, the text of which can be found in the included file GNU GPL 2.0 License.txt or at http://www.gnu.org/licenses/gpl-2.0.html
