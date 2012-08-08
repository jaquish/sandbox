import sys

f = open("matrix.txt")

infinity = sys.maxint

# store all node info in 80x80 array
nodes = []

values = []
for line in range(80):
    values = ( map(lambda x: int(x), f.readline().rstrip('\r\n').split(',')))
    for x in range(80):
        nodes.append({ 'id' : line*80 + x, 'value' : -1,'distance' : infinity, 'prev' : 'undefined'})
                    
f.close()

# store id's of unvisited
unoptimized = list(nodes)

# intialize origin node
nodes[0]['distance'] = 0

current = nodes[0]

while(len(unoptimized) > 0):

    # vertex with smallest distance
    current = min(unoptimized, key=(lambda n: n['distance']))
    if (current['distance'] == infinity):
        break

    unoptimized.remove(current)

    neighbors = []

    # check east neighbor if it exists
    if ( (current['id'] + 1) % 80 != 0):
        neighbors.append(nodes[current['id'] + 1])

    # check south neighbor if it exists
    if (current['id'] < 80*79):
        neighbors.append(nodes[current['id'] + 80])

    # calculate on neighbors
    for n in list(filter((lambda n: n in unoptimized ), neighbors)):
            new_distance = current['distance'] + n['value']

            if (new_distance < n['distance']):
                n['distance'] = new_distance
                n['prev'] = n['id']

    print "The minimum is:", nodes[80*80-1]['distance']