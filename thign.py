def line(m, x, b):
    return((m*x)+b)

def predictions(m, b):
    six = line(m, 6, b)
    twenty = line(m, 20, b)
    thirty = line(m, 30, b)
    return(f'6: {six}\n20: {twenty}\n30: {thirty}')

print(predictions(-14.3, 282))