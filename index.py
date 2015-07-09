#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()  # for troubleshooting


print "Content-Type: text/html\n\n"
print """

<html>
	<head>
		<title> Climate data</title>
	</head>
	
	<body style="margin: 0 auto;">
		
		</div>
			
			<div id="sutherland" align="center">
			
			<table border="1" align="center">
					<tr>
						<td style="background:#333; width:500px; text-align:center; color:white;"><h2 > 74" Climate Data Logger </h2><br> Please select which sensor's data you would like to view and the date range </td>
					</tr>
					<tr >
						<td class="myrow" align="center">
						
						
						
							<form action="/cgi-bin/data_selector.py" method="post">
								From:<input type="date" name="fromonth" placeholder="yyyy-mm-dd">
								To:<input type="date" name="tomonth" placeholder="yyyy-mm-dd"><br />
								Select Data:<input type="checkbox" name="lower_dome_temp" value="data_selection">lower dome
								<input type="checkbox" name="upper_dome_temp" value="data_selection">upper dome
								<input type="checkbox" name="secondary_mirror_temp" value="data_selection">secondary mirror	
								<input type="checkbox" name="primary_mirror_temp" value="data_selection">primary mirror
								
								<input type="submit" value="Submit"/>
								
							</form>
							
							
						</td>
					</tr>
				</table>
			</div>
		</div>
		
		<footer>
			<div class="designer" align="center">
			<p> ~J </p>
			</div>
		</footer>
		
	</body>

</html>

"""
