#!/usr/bin/python


# this will graph data found in a text file with timestamps
import pkg_resources
pkg_resources.require("matplotlib")
import math, time, datetime, cgi, cgitb

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from matplotlib.dates import MONDAY
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter


class graph_data:

	def __init__(self, data_type):
		self.xdata=[]
		self.ydata=[]
		self.fig, self.ax = plt.subplots()
	
	
	"""
	this function accepts a string and an integer.
	The string is the file path to a text file containing the data.
	resolution is the number of samples to be averaged to reduce large datasets.

	"""
	def get_data(self, file_path, resolution):
		t_val = []
		d_val = []
		t_val_sum=0
		temp=[]
		try:
			data_file = open(file_path, "r")
		except:
			return
		i=0
		for line in data_file:
			t_val_sum += float(line.split(" ")[1])
			if (i%resolution==0):  #sum the temperature values until the line count is a multiple of resolution
				t_val.append(t_val_sum/50)
				t_val_sum=0

				'''
				extract the datetime into a string formatted
				<day month year hour minute second> (spaces between values)
				'''
				temp_d = line.split(" ")[0]
				temp_d = temp_d.replace("-", " ")
				temp_d = temp_d.replace(":", " ")
				temp_d = temp_d.replace("/", " ")
				'''
				convert datetime string formatted <day month year hour minute second>
				to a datetime object and append it to a list
				'''
				d_val.append(datetime.datetime(*time.strptime(temp_d[-19:], "%d %m %Y %H %M %S")[:6]))
			i+=1
			
			self.ydata = t_val
			self.xdata = d_val # return 2 lists, (t_val = temperatures, d_val = datetime objects


	def get_ticks(self, frodate, todate):
		x_data=[]
		y_data=[]
		#graphing data
		for x in range(len(self.ydata)):
			if (self.xdata[x]>=frodate) & (self.xdata[x]<=todate):
				x_data.append(self.xdata[x])
				y_data.append(self.ydata[x])



				
				
		
		if (max(y_data)-min(y_data))>25:
			yinc = 1
			if(max(y_data)-min(y_data))>50:
				yinc = 2
				if(max(y_data)-min(y_data))>100:
					yinc = 4
		else:
			yinc = 1

		self.yticks=np.arange(0, max(y_data), yinc)
		self.xticks=np.arange(0, len(x_data)-1, 100)
		self.ax.set_yticks(self.yticks)
		self.ax.set_xticks(self.xticks)
		self.ax.yaxis.grid(True, which='minor')
		self.ax.yaxis.grid(True, which='major')
		self.ax.xaxis.grid(True, which='minor')
		self.ax.xaxis.grid(True, which='major')
		
		
		
		years    = mdates.YearLocator()   # every year
		months   = mdates.MonthLocator()  # every month
		yearsFmt = mdates.DateFormatter('%Y')		
		mondays = WeekdayLocator(MONDAY)
		months = MonthLocator()
		monthsFmt = DateFormatter("%b %d")
		
		self.ax.plot(x_data, y_data)

		self.ax.xaxis.set_major_locator(mondays)
		self.ax.xaxis.set_major_formatter(monthsFmt)
		#ax.xaxis.set_minor_locator(mondays)
		self.ax.autoscale_view()

		plt.ylabel('Temperature (celsius)')
		plt.xlabel('Date Time (dependent on magnification)')
		plt.title(str(self.xdata[0])+"     to      "+str(self.xdata[len(self.xdata)-1]))
		plt.grid(b=True, which='both', color='0.65', linestyle='-')
		self.fig.autofmt_xdate()
	#def graph_data(*arg):

	