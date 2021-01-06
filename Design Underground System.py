class UndergroundSystem:
    def __init__(self):
        self.data = {}
        self.times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.data[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        newData = [stationName,t]
        oldData = self.data[id]
        
        del self.data[id]
        
        if oldData[0] not in self.times:
            self.times[oldData[0]] = {newData[0]: [float(newData[1]-oldData[1]),1]}
        elif newData[0] not in self.times[oldData[0]]:
            self.times[oldData[0]][newData[0]] = [float(newData[1]-oldData[1]),1]
        else:
            old_avg,scale = self.times[oldData[0]][newData[0]] 
            scale += 1
            new_avg = (old_avg*(scale-1)/scale) + float(newData[1]-oldData[1])/scale
            self.times[oldData[0]][newData[0]] = [new_avg,scale]
            
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.times[startStation][endStation][0]
        