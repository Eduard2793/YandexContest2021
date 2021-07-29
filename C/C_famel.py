
class Room():
    def __init__(self,timetable,name):
        self.timetable = timetable
        self.name = name

class Town():
    def __init__(self,name):
        self.name = name
        self.rooms = []
        
    def addRoom(self,room):
        self.rooms.append(room)

def findRooms(request): # len = l (л городов хотят созвониться)
    for hour in range(24):
        # если в заданный час какойто город не имеет свободной комнаты то решения не найдется
        chainOfrooms_in_this_hour = []
        for T in request:
            # есть ли в этот час в этом городе своббодная комната?
            for room in T.rooms:
                if room.timetable[hour] == ".":
                    # есть свободная комната
                    # закончили искать свободную комнату
                    # если в следующих городах не будет свободной комнаты то 
                    # не получится в независимости о того какую мы тут выбрали
                    chainOfrooms_in_this_hour.append([T.name,room.name])
                    break
                    # идем к следующему городу
            # и так пройдем по всем городам и если в очередном городе нашлась в этот час свободная комната
            # то записываем ее в решение
        # закончили обход городов в этот час
        # если в решении собралось столько же комнат сколько было городов в запросе
        # значит в этот час может произойти созвон между этими городами
        # то есть задача решена

        if len(chainOfrooms_in_this_hour) == len(request):
            # потому что в каждом городе беру только первую попавшуюся комнату
            ans = "Yes "
            for i in range(len(chainOfrooms_in_this_hour)):
                t = chainOfrooms_in_this_hour[i][0]
                r = chainOfrooms_in_this_hour[i][1]
                ans += (r + " ")
            return ans
    return "No"

c = int(input()) # number of towns
townsDict = {}
for i in range(c):
    town_rooms = input().split()
    T = Town(town_rooms[0])
    for j in range(int(town_rooms[1])):
        time_name = input().split()
        room = Room(time_name[0],time_name[1])
        T.addRoom(room)
    townsDict[town_rooms[0]] = T
        
m = int(input()) # number of requestes
for i in range(m):
    request = []
    l_request = input().split()
    for j in range(1,int(l_request[0])+1):
        request.append(townsDict[l_request[j]])
    print(findRooms(request))

