from queue import Queue

def hotPotato(nameList, num):
    queue = Queue()
    for name in nameList:
        queue.enqueue(name)
    while(queue.size()>1):
        for i in range(0,num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
