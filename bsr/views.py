from django.shortcuts import render
from django.http import HttpResponse
from .models import data

#function to change the date format
def changeDate(old):
	new=old[8]+old[9]+"-"+old[5]+old[6]+"-"+old[0]+old[1]+old[2]+old[3]
	return new
	
	
def index(request):

	#Extract data from server
	all_data=data.objects.all()

	#Length of Data
	l=len(all_data)

	#List for parameters
	Tdate=["01-01-2020"]
	Ttotal=[0]
	Trecovered=[0]
	Tactive=[0]
	Tdeceased=[0]
	DataMap={}

	#Data Separation
	for i in range(l):
		Tdate.append(changeDate(str(all_data[i].Date)))
		Ttotal.append(int(all_data[i].Total))
		Trecovered.append(int(all_data[i].Recovered))
		Tdeceased.append(int(all_data[i].Death))
		TempActive=int(all_data[i].Total)-(int(all_data[i].Recovered)+int(all_data[i].Death))
		Tactive.append(int(TempActive))

	#Hasing the Data
	DataMap['Tdate']=Tdate
	DataMap['Ttotal']=Ttotal
	DataMap['Trecovered']=Trecovered
	DataMap['Tactive']=Tactive
	DataMap['Tdeceased']=Tdeceased

	#render the data
	return render(request,'front.html',{"datas":DataMap});


