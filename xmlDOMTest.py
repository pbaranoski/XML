import os

from xml.dom.minidom import parse
import xml.dom.minidom


inDir = r'C:\Users\user\Documents\PythonLearning\LandingDir'

# Example of XML
'''
<collection shelf="New Arrivals">
<movie title="Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
'''

xmlFile = os.path.join(inDir,"movies.xml")
print("xmlFile: "+xmlFile)

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse(xmlFile)
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print("Root element : %s" % collection.getAttribute("shelf"))

# Get all the movies in the collection
movies = collection.getElementsByTagName("movie")

# Print detail of each movie.
for movie in movies:
   print("*****Movie*****")
   if movie.hasAttribute("title"):
      print("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print("Description: %s" % description.childNodes[0].data)