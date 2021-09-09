# Sqlalchemy-Climate-Analysis

A connection was made to a sqlite database hawaii in the Resources folder to get daily temperatures and precipitations 
by date from different station readers.

A)  Jupyter notebook connections
	1)  Each table class is assigned to a variable.
	2)  The last date in the dataset is saved and then the date 12 months prior is determined.
	3)  A bar chart is used to plot the precipitations over the last 12 months.
	4)  The number of stations and the station with the most readings are recorded.
	5)  The temperature readings of each day by the that station is graphed on a histogram with 12 bins.

B)  Flask app.py
	1)  An index page that lists the 5 additional pages that can be viewed.
		a)  precipitation - displaying the same precipitation query as the jupyter notebook.
		b)  stations - list all the stations in the dataset
		c)  temperature - displaying the same temperature query as the jupyter notebook.
		d)  start - returns the minimum, maximum and average reading between the stations for each date
			starting with the date entered in the URL.
		e)  start/end - the same as the start page, but allows the user to also add an end date.
![image](https://user-images.githubusercontent.com/80318883/132769769-f7ed7a40-bd94-4364-9f7b-6eaab1d5df3e.png)
