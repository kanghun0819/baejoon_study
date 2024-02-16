def solution(sizes):

    temp_max = -1
    temp_min = -1

    for array_id in sizes:

        if(max(array_id)>temp_max):
            temp_max = max(array_id)
        if(temp_min<min(array_id)):
            temp_min=min(array_id)

    answer = temp_max*temp_min        
    return answer
