import searfer

service = searfer.Searfer(threads=int(input('Threads quantity: ')))

while True:
    service.run()