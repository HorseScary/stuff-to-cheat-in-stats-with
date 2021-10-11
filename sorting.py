"""
i cant be asked to acutaly check if the thing is sorted so it just goes infinitly 
do control c to get out!
"""

def sort(data):
    while True:

        for i in range(len(data)):
            hold = 0
            if i == len(data) -1:
                break
#            check = data
            
            if data[i] > data[i+1]:
                hold = data[i+1]
                data[i+1] = data[i]
                data[i] = hold
                print(data)

#            print (f"data: {data}\ncheck:{check}")
        
#        if check == data:
#            break

    return(data)

def quartile(data):

    if len(data)%2 == 1:
        q2 = data[int((len(data)/2)-.5)]

    
    else:
        a = int(len(data)/2)
        b = int(len(data)/4)
        q1 = (data[b] + data[b-1])/2
        q2 = (data[a] + data[a-1])/2
        q3 = (data[a+b] + data[a+b-1])/2

    return(f"First Quartile: {q1}\nSecond Quartile: {q2}\nThird Quartile: {q3}")