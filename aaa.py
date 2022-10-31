
R = 1
for x in range(1,100):
    for y in range(1, 100):
        normX = x / 100.0
        normY = y / 100.0
        
        print(R * R - normX * normX - normY * normY)