import csv
import sys
import os

## The intent is to take records that look like this:
## year,month,precinct,street_name,lon,lat,accidents_with_injuries,accidents,involved,category,injured,killed,vehicle_type,vehicle_count
## 2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,,,,Sport utility / station wagon,1
## 2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Passengers,0,0,,
## 2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Pedestr,0,0,,
## 2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Total,0,0,,
## 2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Motorists,0,0,,
## 2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Cyclists,0,0,,
## 
## and make them look like this:
## 
## fdate,year,month,precinct,street_name,lon,lat,accidents_with_injuries,accidents,involved,totalInjured,totalKilled,passengersInjured,passengersKilled,pedInjured,pedKilled,motoristInjured,motoristKilled,cyclistInjured,cyclistKilled,PassengerVehicle,Ambulance,Bicycle,Bus,FireTruck,LargeComVeh,Livery,Motorcycle,Other,Pedicab,PickupTruck,Scooter,SmallComVeh,SUV,Taxi,Unknown,Van,boro,borocode
## 2/1/2012,2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,Manhattan,1

## INPUT:
##    all_accidents.csv - from http://nypd.openscrape.com
##    exception.csv
##    precinct.csv
## OUTPUT:
##    all_accidents_scrubbed.csv
##
##/****** Script for SelectTopNRows command from SSMS  ******/
##SELECT [boro]
##       ,[precinct]
##      ,[street_name]
##      ,[lon]
##      ,[lat]
##      ,sum([accidents_with_injuries]) as accidents_with_injuries
##      ,sum([accidents]) as accidents
##      ,sum([involved]) as involved
##      ,sum([totalInjured]) as totalInjured
##      ,sum([totalKilled]) as totalKilled
##      ,sum([passengersInjured]) as passengersInjured
##      ,sum([passengersKilled]) as passengersKilled
##      ,sum([pedInjured]) as pedInjured
##      ,sum([pedKilled]) as pedKilled
##      ,sum([motoristInjured]) as motoristInjured
##      ,sum([motoristKilled]) as motoristKilled
##      ,sum([cyclistInjured]) as cyclistInjured
##      ,sum([cyclistKilled]) as cyclistKilled
##      ,sum([PassengerVehicle]) as passengervehicle
##      ,sum([Ambulance]) as ambulace
##      ,sum([Bicycle]) as bicycle
##      ,sum([Bus]) as bus
##      ,sum([FireTruck]) as firetruck
##      ,sum([LargeComVeh]) as largeComVeh
##      ,sum([Livery]) as Livery
##      ,sum([Motorcycle]) as Motorcycle
##      ,sum([Other]) as other
##      ,sum([Pedicab]) as pedicab
##      ,sum([PickupTruck]) as Pickuptruck
##      ,sum([Scooter]) as scooter
##      ,sum([SmallComVeh]) as smallcomveh
##      ,sum([SUV]) as suv
##      ,sum([Taxi]) as taxi
##      ,sum([Unknown_]) as unknown
##      ,sum([Van]) as van
##      
##     
## 
##  FROM [dbo].[ALLACCIDENTS2]
##  group by boro,[precinct]
##      ,[street_name]
##      ,[lon]
##      ,[lat]
##      order by  boro,[precinct]
##      ,[street_name]
##      ,[lon]
##      ,[lat]
      
class precinct:
    def __init__(self, row):
        self.precinct = row[0]
        self.precinctFull = row[1]
        self.boro = row[2]
        self.boroCode = row[3]
        
class exceptionList:
    def __init__(self, row):
        self.street = row[0]
        self.lon = row[1]
        self.lat = row[2]

        
class inRow:
    def __init__(self, row):
        self.year = row[0]
        self.month = row[1]
        self.precinct = row[2]
        self.street_name = row[3]
        self.lon = row[4]
        self.lat = row[5]
        self.accidents_with_injuries = row[6]
        self.accidents = row[7]
        self.involved = row[8]
        self.category = row[9]
        self.injured = row[10]
        self.killed = row[11]
        self.vehicle_type = row[12]
        self.vehicle_count = row[13]

class outRow:
    def __init__(self):
        self.year = ''
        self.month = ''
        self.precinct = ''
        self.street_name = ''
        self.lon = 0.0
        self.lat = 0.0
        self.accidents_with_injuries = 0
        self.accidents = 0
        self.involved = 0
        self.totalInjured = 0
        self.totalKilled = 0
        self.passengersInjured = 0
        self.passengersKilled = 0
        self.pedInjured = 0
        self.pedKilled = 0
        self.motoristInjured = 0
        self.motoristKilled = 0
        self.cyclistInjured = 0
        self.cyclistKilled = 0
        self.PassengerVehicle = 0
        self.Ambulance = 0
        self.Bicycle = 0
        self.Bus = 0
        self.FireTruck = 0
        self.LargeComVeh = 0
        self.Livery = 0
        self.Motorcycle = 0
        self.Other = 0
        self.Pedicab = 0
        self.PickupTruck = 0
        self.Scooter = 0
        self.SmallComVeh = 0
        self.SUV = 0
        self.Taxi = 0
        self.Unknown = 0
        self.Van = 0

def proc(r,o):
          
    if(o.year == ''):
       
        o.year = r.year
        o.month = r.month
        o.precinct = r.precinct
        o.street_name = r.street_name
        o.lon = r.lon
        o.lat = r.lat
        o.accidents_with_injuries = r.accidents_with_injuries
        o.accidents = r.accidents
        o.involved = r.involved

    if(o.totalInjured == 0 and r.category == 'Total'):
        o.totalInjured = r.injured
        o.totalKilled = r.killed

    elif(o.passengersInjured == 0 and r.category == 'Passengers'):    
        o.passengersInjured = r.injured
        o.passengersKilled = r.killed

    elif(o.pedInjured == 0 and r.category == 'Pedestr'):
        o.pedInjured = r.injured
        o.pedKilled = r.killed

    elif(o.motoristInjured == 0 and r.category == 'Motorists'):
        o.motoristInjured = r.injured
        o.motoristKilled = r.killed

    elif(o.cyclistInjured == 0 and r.category == 'Cyclists'):
        o.cyclistInjured = r.injured
        o.cyclistKilled = r.killed
   
# There was some random items in this field. I picked out the most prevalent items.
    elif(r.vehicle_type == 'Passenger vehicle'):
        o.PassengerVehicle = r.vehicle_count
    elif(r.vehicle_type == 'Sport utility / station wagon'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'Unknown'):
        o.Unknown = r.vehicle_count
    elif(r.vehicle_type == 'Van'):
        o.Van = r.vehicle_count
    elif(r.vehicle_type == 'Taxi vehicle'):
        o.Taxi = r.vehicle_count
    elif(r.vehicle_type == 'Other'):
        o.Other = r.vehicle_count
    elif(r.vehicle_type == 'Bus'):
        o.Bus = r.vehicle_count
    elif(r.vehicle_type == 'Small com veh(4 tires)'):
        o.SmallComVeh = r.vehicle_count
    elif(r.vehicle_type == 'Pick-up truck'):
        o.PickupTruck = r.vehicle_count
    elif(r.vehicle_type == 'Bicycle'):
        o.Bicycle = r.vehicle_count
    elif(r.vehicle_type == 'Large com veh(6 or more tires)'):
        o.LargeComVeh = r.vehicle_count
    elif(r.vehicle_type == 'Livery vehicle'):
        o.Livery = r.vehicle_count
    elif(r.vehicle_type == 'Motorcycle'):
        o.Motorcycle = r.vehicle_count
    elif(r.vehicle_type == 'Sport utility /'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'Ambulance'):
        o.Ambulance = r.vehicle_count
    elif(r.vehicle_type == 'Fire truck'):
        o.FireTruck = r.vehicle_count
    elif(r.vehicle_type == 'station wagon   Passenger vehicle'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'Scooter'):
        o.Scooter = r.vehicle_count
    elif(r.vehicle_type == 'station wagon Unknown'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'Small com veh(4'):
        o.SmallComVeh = r.vehicle_count
    elif(r.vehicle_type == 'station wagon    Passenger vehicle'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'station wagon Taxi vehicle'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'Large com veh(6 or'):
        o.LargeComVeh = r.vehicle_count
    elif(r.vehicle_type == 'more tires)'):
        o.Unknown = r.vehicle_count
    elif(r.vehicle_type == 'Large com veh(6 o'):
        o.LargeComVeh = r.vehicle_count
    elif(r.vehicle_type == 'station wagon Van'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'more tires) Passenger vehicle'):
        o.PassengerVehicle = r.vehicle_count
    elif(r.vehicle_type == 'station wagon  Passenger vehicle'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'tires) Sport utility / station wagon'):
        o.Unknown = r.vehicle_count
    elif(r.vehicle_type == 'station wagon   Sport utility / station wagon'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'station wagon Other'):
        o.SUV = r.vehicle_count
    elif(r.vehicle_type == 'Pedicab'):
        o.Pedicab = r.vehicle_count

   
    return o

def getOutStr(o):
    
    return o.year+','+o.month+','+o.precinct+','+o.street_name+','+str(o.lon)+','+ str(o.lat)+','+str(o.accidents_with_injuries)+','+str(o.accidents)+','+ \
                       str(o.involved)+','+str(o.totalInjured)+','+str(o.totalKilled)+','+str(o.passengersInjured)+','+str(o.passengersKilled)+','+str(o.pedInjured)+','+ \
                       str(o.pedKilled)+','+str(o.motoristInjured)+','+str(o.motoristKilled)+','+str(o.cyclistInjured)+','+str(o.cyclistKilled)+','+str(o.PassengerVehicle)+','+ \
                       str(o.Ambulance)+','+str(o.Bicycle)+','+str(o.Bus)+','+str(o.FireTruck)+','+str(o.LargeComVeh)+','+str(o.Livery)+','+str(o.Motorcycle)+','+str(o.Other)+','+ \
                       str(o.Pedicab)+','+str(o.PickupTruck)+','+str(o.Scooter)+','+str(o.SmallComVeh)+','+str(o.SUV)+','+str(o.Taxi)+','+str(o.Unknown)+','+str(o.Van)

def createPrecinctLookup(dir):
    f = open(dir+'precinct.csv', 'r')
    lookup = {}
    try:
        reader = csv.reader(f)
        for row in reader: 
            r = precinct(row)
            lookup[r.precinctFull] = "%s,%s" % (r.boro, r.boroCode)
    except:
        print 'Error opening '+dir+'precinct.csv', sys.exc_info()[0]
    
    return lookup

def createExceptionLookup(dir):
    f = open(dir+'exception.csv', 'r')
    elookup = {}
    try:
        reader = csv.reader(f)
        for row in reader: 
            r = exceptionList(row)
            elookup[r.street] = "%s,%s" % (r.lon, r.lat)
    except:
        print 'Error opening '+dir+'exception.csv', sys.exc_info()[0]
    
    return elookup

headerOut = "fdate,year,month,precinct,street_name,lon,lat,accidents_with_injuries,accidents,involved,totalInjured,totalKilled,passengersInjured,passengersKilled,pedInjured,pedKilled,motoristInjured,motoristKilled,cyclistInjured,cyclistKilled,PassengerVehicle,Ambulance,Bicycle,Bus,FireTruck,LargeComVeh,Livery,Motorcycle,Other,Pedicab,PickupTruck,Scooter,SmallComVeh,SUV,Taxi,Unknown,Van,boro,borocode\n"

try:

    dir = os.path.dirname(os.path.realpath(__file__))+"\\"

    # all_accidents.csv
    f = open(dir+'all_accidents.csv', 'rb') 
    #f = open(sys.argv[1], 'rb') # opens the csv file
    ofile  = open(dir+'all_accidents_scrubbed.csv', "wb")
    lookup = createPrecinctLookup(dir)
    elookup = createExceptionLookup(dir)
    month_dict = {"month":-1,"":'0',"January":1,"February":2,"March":3,"April":4, "May":5, "June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

    reader = csv.reader(f)  
    x = 0
    previous = ""
    current = ""
    o = outRow()
    i = 0
    boro = ""
    exceptionStreet =""
    ofile.writelines(headerOut)
    for row in reader:   
        current = row[0]+row[1]+row[3]
        r = inRow(row)

        try:
            int(r.vehicle_count)
        except ValueError:                      
            if(r.vehicle_count != ''):
                print "datatype error for vehicle_count.  Row: "+str(i)+" Value: "+r.vehicle_count
                r.vehicle_count = 0
            
            
        if(previous != current):
            try:
                if(o.precinct == "Midtown North Precinct"):
                   o.precinct = "18th Precinct"
                elif(o.precinct == "Midtown South Precinct"):
                   o.precinct = "14th Precinct"
                elif(o.precinct == "Central Park Precinct (022)"):
                   o.precinct = "22nd Precinct"
                elif(o.precinct == "Central Park Precinct"):
                   o.precinct = "22nd Precinct"
                   
                boro = lookup[o.precinct]
                
                             
            except:
                boro = " , "

            default = '0'
            a = elookup.get(o.street_name, default)
            if(a != '0'):
                print "line:"+str(i)+" Missing Intersection - "+o.street_name
                ack = a.split(',')
                o.lon = ack[0]
                o.lat = ack[1]
                
                
           

            monthNum =  month_dict[o.month]
            fulldate = "%s/1/%s" % (monthNum,o.year)
            
                                   
            outprint = getOutStr(o)

                          
            if(i >1):
                ofile.writelines(fulldate+","+outprint+","+boro+'\n')
            
            o = outRow()
        o = proc(r,o)
        previous = current
        i = i+1
        
    print str(i)+' records processed'
    f.close()      # closing
    ofile.close()
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise



 

