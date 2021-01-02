def simplify_seat(seatNo):
    simpleSeat = seatNo % 12
    if simpleSeat == 0:
        return 12
    return simpleSeat
 
def opposite_seat(seatNo):
    oppSeatNo = 13-seatNo
    return oppSeatNo
 
def seat_type(seatNo):
    if seatNo in [1,6,7,12]:
        return "WS"
    elif seatNo in [2,5,8,11]:
        return "MS"
    else:
        return "AS"
 
test_cases = int(input())
 
for test_case in range(test_cases):
    seatNo = int(input())
    if (seatNo % 12) == 0:
        compartment = seatNo // 12 - 1
    else:
        compartment = seatNo // 12
 
    simplifiedSeat = simplify_seat(seatNo)
    oppositeSeat = opposite_seat(simplifiedSeat)
    seatType = seat_type(oppositeSeat)
    print(oppositeSeat+(compartment*12),seatType)