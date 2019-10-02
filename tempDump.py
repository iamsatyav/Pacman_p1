exploredList = []
    pathSteps = []
    myQueue = util.Queue()
    rootNode = problem.getStartState()
    cornersReached = 0
    if problem.isGoalState(rootNode):
        return pathSteps
    # if rootNode['node'] in rootNode['corners']:
    #     rootNode['cornersReached'].append(rootNode['node'])
    #     rootNode['corners'].remove(rootNode['node'])
    myQueue.push((rootNode, pathSteps))
    print('+++++++++++++++++++++++++++++++')
    print(rootNode)
    while not myQueue.isEmpty():
        print('In while loop ----------------------->')
        print()
        currentNode, pathSteps = myQueue.pop()
        print(currentNode, pathSteps)
        print('Explored list: ------------------>', exploredList)
        if currentNode['node'] not in exploredList:
            #here i check if node is corner
            if currentNode['node'] in currentNode['corners']:
                print('In corner check case %%%%%%%%%%%%%%%%%%%%%%%%')
                while not myQueue.isEmpty():
                    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^Emptying the queue')
                    print(myQueue.pop())
                currentNode['cornersReached'].append(currentNode['node'])
                currentNode['corners'].remove(currentNode['node'])
                exploredList = []
            if problem.isGoalState(currentNode):
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', pathSteps)
                return pathSteps
            exploredList.append(currentNode['node'])
            for childNode, step, _ in problem.getSuccessors(currentNode):
                myQueue.push((childNode, pathSteps + [step]))