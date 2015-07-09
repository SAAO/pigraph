#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, time
import pkg_resources
pkg_resources.require("matplotlib")
import math, time, datetime, cgi, cgitb
import matplotlib.pyplot as plt, mpld3
import module_graph as g

cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
fromonth = form.getvalue('fromonth')
tomonth  = form.getvalue('tomonth')
froymd = fromonth.replace("-", " ")
toymd = tomonth.replace("-", " ")

frodt = datetime.datetime(*time.strptime(froymd, "%Y %m %d")[:6])
todt = datetime.datetime(*time.strptime(toymd, "%Y %m %d")[:6])

if form.getvalue('lower_dome_temp'):
	ldt=True
else:
	ldt=False
if form.getvalue('upper_dome_temp'):
	udt=True
else:
	udt=False
if form.getvalue('secondary_mirror_temp'):
	smt=True
else:
	smt=False
if form.getvalue('primary_mirror_temp'):
	pmt=True
else:
	pmt=False
	
	
	
object = g.graph_data("temperature")
object.get_data("lower_dome_temp.txt", 50)
object.get_ticks(frodt, todt)

'''
web_end = open("/var/www/pigraphs/index.html", "wb")
mpld3.save_html(object.fig, web_end)
web_end.close()
'''

print "Content-type: text/html\n\n"
print "<html>"
print "<body>"
if todt<frodt:
	print "<h2>The second date must be larger than the first {0}</h2>".format(frodt)
else:
	print "<h2>The data is valid {0}</h2>".format(frodt.year)
print "</body>"

print mpld3.fig_to_html(object.fig)
print "</html>"


	





