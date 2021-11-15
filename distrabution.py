def freqDistrabution(data):
    total = 0
    distrabution = []
    for i in range(len(data)):
        total += data[i]
    for i in range(len(data)):
        distrabution.append(data[i] / total)
    return(distrabution)