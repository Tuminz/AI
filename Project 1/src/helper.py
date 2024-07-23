from Node import *

# Read input

def readInput(filepath):
    map = []
    f = open(filepath)
    row, col = f.readline().split()
    try:
        row = int(row)
        col = int(col)
        for i in range (0, row):
            line = f.readline()
            newRow = line.split()
            map.append(newRow)
    except:
        print('The number of row or column is invalid')
    return row, col, map

# Getting path from explored set

def reconstructPath(exploredSet, startPos, goalPos, isGinE):
    path = []
    i = len(exploredSet) - 1
    if not isGinE:
        path.append(goalPos)
    while True:
        path = [exploredSet[i].position] + path
        if exploredSet[i].position == startPos:
            break
        i = [node.position for node in exploredSet].index(exploredSet[i].parent)
    return path

'''
def reconstructPath(exploredSet, startPos, goalPos, isGinE):
    path = []
    
    # Nếu không phải là trường hợp đặc biệt, tìm điểm đích trong exploredSet
    if not isGinE:
        if any(node.position == goalPos for node in exploredSet):
            currentNode = next(node for node in exploredSet if node.position == goalPos)
        else:
            return []  # Không tìm thấy đường đến điểm đích
    else:
        # Thay đổi nếu là một trường hợp khác, ví dụ, trong A* hoặc thuật toán khác.
        currentNode = next(node for node in exploredSet if node.position == goalPos)
    
    while currentNode:
        path.append(currentNode.position)
        if currentNode.position == startPos:
            break
        currentNode = next((node for node in exploredSet if node.position == currentNode.parent), None)
    
    path.reverse()
    return path
'''
