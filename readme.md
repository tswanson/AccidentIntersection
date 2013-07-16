python AccidentIntersection.py

INPUT:
   all_accidents.csv - from http://nypd.openscrape.com/data/all_accidents.csv.zip
   exception.csv
   precinct.csv
OUTPUT:
   all_accidents_scrubbed.csv

The intent is to take records that look like this:
year,month,precinct,street_name,lon,lat,accidents_with_injuries,accidents,involved,category,injured,killed,vehicle_type,vehicle_count
2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,,,,Sport utility / station wagon,1
2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Passengers,0,0,,
2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Pedestr,0,0,,
2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Total,0,0,,
2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Motorists,0,0,,
2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,Cyclists,0,0,,

and make them look like this:

fdate,year,month,precinct,street_name,lon,lat,accidents_with_injuries,accidents,involved,totalInjured,totalKilled,passengersInjured,passengersKilled,pedInjured,pedKilled,motoristInjured,motoristKilled,cyclistInjured,cyclistKilled,PassengerVehicle,Ambulance,Bicycle,Bus,FireTruck,LargeComVeh,Livery,Motorcycle,Other,Pedicab,PickupTruck,Scooter,SmallComVeh,SUV,Taxi,Unknown,Van,boro,borocode
2/1/2012,2012,February,1st Precinct,1 PLACE and BATTERY PLACE,-74.017929,40.706176,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,Manhattan,1


