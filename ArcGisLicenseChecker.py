"""Reports availability of ArcGIS licenses and extensions.
"""

"""
The MIT License (MIT)

Copyright (c) 2013 Washington State Department of Transportation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


import sys

sys.stderr.write("Importing arcpy...\n")
import arcpy
sys.stderr.write("arcpy import complete.\n\n")

products = {
            "arcview": "ArcGIS for Desktop Basic",
            "arceditor": "ArcGIS for Desktop Standard",
            "arcinfo": "ArcGIS for Desktop Advanced",
            "engine": "Engine Runtime",
            "enginegeodb": "Engine Geodatabase Update",
            "arcserver": "Server"
           }

extensions = {"3D": "3D Analyst",
              "Schematics": "ArcGIS Schematics",
              "ArcScan": "ArcScan",
              "Business": "Business Analyst",
              "DataInteroperability": "Data Interoperability",
              "GeoStats": "Geostatistical Analyst",
              "JTX": "Workflow Manager",
              "Network": "Network Analyst",
              "Aeronautical": "Esri Aeronautical Solution",
              "Defense": "Esri Defense Solution",
              "Foundation": "Esri Production Mapping",            
              "Datareviewer": "ArcGIS Data Reviewer",
              "Nautical": "Esri Nautical Solution",
              "Nauticalb": "Esri Bathymetry",
              "Spatial": "Spatial Analyst",
              "StreetMap": "StreetMap",
              "Tracking": "Tracking"
              }

for product in products:
    print "%-44s\t%s" % (("%s (%s):" % (products[product], product)), arcpy.CheckProduct(product))

for extension in extensions:
    print "%-44s\t%s" % (("%s (%s):" % (extensions[extension], extension)), arcpy.CheckExtension(extension))