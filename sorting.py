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
            
            if data[i] > data[i+1]:
                hold = data[i+1]
                data[i+1] = data[i]
                data[i] = hold
                print(data)


def sortRecursive(data):
    check = data[:]
    def sortReal(data, check, it):
        it +=1
        for i in range(len(data)):
            hold = 0
            if i == len(data) -1:
                break
            
            if data[i] > data[i+1]:
                hold = data[i+1]
                data[i+1] = data[i]
                data[i] = hold


        if check == data:
            return(f"[LIST SORTED]\n{data}\nIt took {it} tries to sort your list!")
        
        else:
            check = data[:]
            return(sortReal(data, check, it))
    
    return(sortReal(data, check, 0))