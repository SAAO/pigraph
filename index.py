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
						<td style="background:#333; width:500px; text-align:center; color:white;"><h2 > Sutherland </h2> </td>
					</tr>
					
					<tr >
						<td class="myrow" align="center"> <a href="hello.py" target="_blank"><button type="button">1.9m Lower Dome Temperature</button></a></td>
					</tr>
					<tr >
						<td class="myrow" align="center"> 

						
						
						
						
						
						</td>
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
					<tr >
						<td class="myrow" align="center"> <a href="http://10.2.55.4:4000" target="_blank"><button type="button" >1.9m Secondary Mirror Temperature</button></a></td>
					</tr>
					<tr >
						<td class="myrow" align="center"> <a href="http://10.2.55.5:4000" target="_blank"><button type="button" >MeerLICHT Dome Temperature</button></a></td>
					</tr>
					<tr >
						<td class="myrow" align="center"> <a href="http://10.2.55.5:4000" target="_blank"><button type="button" >MeerLICHT Dome Humidity</button></a></td>
					</tr>
				</table>
			</div>
		</div>
		
		<footer>
			<div class="designer" align="center">
			<p> sig goes here </p>
			</div>
		</footer>
		
	</body>

</html>

"""
