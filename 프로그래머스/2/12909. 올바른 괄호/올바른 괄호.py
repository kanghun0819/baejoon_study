def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    print('Hello Python')

    array = []

    for i in s:
        if(i=='('):
            array.append(i)
        elif(i==')'):
            if(len(array)==0):
                return False
            array.pop()
        

    if(len(array)>0):
        return False


    return True