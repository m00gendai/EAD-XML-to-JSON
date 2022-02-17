# EAD-XML-to-JSON
Simple script that converts and merges Eurocontrol European AIS Database SDO Report XML files to JSON. Written in Python 3.10.1.

## Dependencies ##

[xmltodict](https://pypi.org/project/xmltodict/)

## Setup ##

Just place the file in the same directory as the source XML files and run it. 

## Source Files ##

Available from EAD Basic.

Naming convention is according to script but you can change it however you like.

Attention: Some reports are extremely RAM-hungry when generating the XML (e.g.: Designated Points - Hemisphere North/East). Be aware if your RAM is <= 16GB.

