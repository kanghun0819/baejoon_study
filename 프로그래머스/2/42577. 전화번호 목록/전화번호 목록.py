def solution(phone_book):
    answer = True

  
    phone_book.sort()

    
    

    temp = ''

    for i in range(len(phone_book)-1):
        if(phone_book[i]==phone_book[i+1][:len(phone_book[i])]):
            return False
 


    return answer


