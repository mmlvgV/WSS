import surfer

service = surfer.Surfer(threads=int(input('Threads quantity: ')))

while True:
    service.run()