def average(data):
    total = 0
    for i in range(len(data)):
        total += data[i]
    
    return(total/len(data))

def quartile(data):

    if len(data)%2 == 1:
        a = int((len(data)/2)-.5)
        b = int((len(data)/4)-.5)
        q2 = data[a]
        q1 = data[b]
        q3 = data[a+b]
    
    else:
        a = int(len(data)/2)
        b = int(len(data)/4)
        q1 = (data[b] + data[b-1])/2
        q2 = (data[a] + data[a-1])/2
        q3 = (data[a+b] + data[a+b-1])/2

    return(f"First Quartile: {q1}\nSecond Quartile: {q2}\nThird Quartile: {q3}")