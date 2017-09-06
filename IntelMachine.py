##rules - 1-10 operators, 10 Zones, temp between 12 and 50, 400 machines

allOnlineStatus = ["Online", "Online", "Online", "Online", "Online", "Online", "Online", "Online", "Offline", "Idle"]
allZoneNames = [1,2,3,4,5,6,7,8,9,10]
allTemperature = range(21,51)

itemNumber = 0;
for operatorNumber in range( 1, 11 ):
    for machineNumber in range( 0, 40 ):
        operatorName = "Operator " + str(operatorNumber)
        machineName = chr(ord('Z')-itemNumber % 26) + chr(ord('A')+itemNumber % 26) + " " + str(itemNumber).zfill(5)
        onlineStatus = allOnlineStatus[ itemNumber % len(allOnlineStatus) ]
        zoneName = allZoneNames[ itemNumber % len(allZoneNames) ]
        temperatureGauge = allTemperature[ itemNumber % len(allTemperature)]
        print str(itemNumber) + ": " + machineName + ", " + onlineStatus + ", " + "Zone " + str(zoneName) + ", " + str(temperatureGauge) + ", " + operatorName
        itemNumber += 1




wweqw