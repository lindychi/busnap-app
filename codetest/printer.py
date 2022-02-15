import time 

def solution(priorities, location):
    index = 0
    period = 9
    count = 0
    start = 0
    end = 0
    reset = 0
    
    while len(priorities) - count and period > 0:
        print("index:"+str(index)+" count:"+str(count)+" period:"+str(period)+" stend:"+str(start)+"~"+str(end))
        print(priorities)
        if period == priorities[index]:
            count = count + 1
            end = index
            priorities[index] = 0
            print(priorities)
            if index == location:
                return count
        index = index + 1
        print("len"+str(len(priorities))+"<="+str(index))
        if len(priorities) <= index:
            index = 0
            reset = 1
        if index >= start and reset == 1:
            index = start = end
            reset = 0 
            period = period - 1
    
    return 1

def check(input, result):
    if input == result:
        print("테스트를 통과하였습니다.")
    else:
        print("실행한 결괏값 "+str(result)+"가 기댓값 "+str(input)+"과 다릅니다.")

check(1, solution([2, 1, 3, 2], 2))
check(5, solution([1, 1, 9, 1, 1, 1], 0))