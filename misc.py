def average(data):
    total = 0
    for i in range(len(data)):
        total += data[i]
    
    return(total/len(data))