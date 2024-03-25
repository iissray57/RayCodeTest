## Concept
## 데이터가 string 조합 형태의 데이터로 split으로 분할 해야함
## 기준이 분이기때문에 주어진 시간형태의 단위를 분으로 변경
## 동일한 차번호가 2번 입차 출차 할 수도 있기 떄문에 Dictionary를 사용하여 값을 업데이트
## Dictionary Key 기준으로 내림 차순 정렬

## Error
## 2번 입차 출차를 진행 한 경우 별도의 계산을 했음.. 누적 주차시간으로 수정
## 시간 누적으로 마지막에 연산하는 방법으로 변경
import math
def hourToMinute(time) :
    data = time.split(':')
    time = int(data[0])*60 + int(data[1])
    return time

def calculateFee(fees, parkingTime) :
    if parkingTime <= fees[0] :
        return fees[1]
    elif parkingTime > fees[0] :
        countingFee = math.ceil((parkingTime - fees[0])/fees[2])
        return fees[1] + countingFee * fees[3]

def solution(fees, records):
    carFee = {}
    parkingCar = {}
    for record in records :
        data = record.split(" ")
        if data[2] == 'OUT' :
            time = hourToMinute(data[0])-parkingCar[data[1]]
            carFee[data[1]] = (carFee[data[1]] + time) if data[1] in carFee else time
            parkingCar.pop(data[1])
        else :
            parkingCar[data[1]] = hourToMinute(data[0])
    if len(parkingCar) != 0:
        for car in parkingCar :
            time = hourToMinute('23:59')-parkingCar[car]
            carFee[car] = (carFee[car] + time ) if car in carFee else time
    sorted_keys = sorted(carFee.keys())
    return [calculateFee(fees,carFee[key]) for key in sorted_keys]

print(solution(

    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
     "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
     "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
))