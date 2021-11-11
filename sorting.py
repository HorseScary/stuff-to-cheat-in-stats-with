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
