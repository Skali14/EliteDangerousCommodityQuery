import getCommodityID
import getStation

whatToDo = input('Do you want to find a commodity or a station? ')

if whatToDo == 'Commodity':
    getCommodityID.getCommodityID()
elif whatToDo == 'Station':
    getStation.getStationByID()