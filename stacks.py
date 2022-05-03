stack = []


def enqueue(value):
    stack.append(value)
    return


def dequeue():
    if len(stack) != 0:
        del stack[0]
    else:
        print("Stack empty")


def peek():
    if len(stack) != 0:
        print(stack[0])


def main():
    enqueue("google")
    enqueue("microsoft")
    enqueue("netflix")
    enqueue("twitter")
    enqueue("meta")
    peek()
    dequeue()
    peek()
    dequeue()
    peek()
    dequeue()
    peek()
    dequeue()
    peek()
    dequeue()
    peek()
    dequeue()


main()
