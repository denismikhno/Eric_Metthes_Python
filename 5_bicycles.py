empty = []
print(empty)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[1].title())
print(bicycles[-1].title())

print('-------------------------')
for bicycle in bicycles:
    print(bicycle.title())

message = f"Велосипед моей мечты - это {bicycles[0].title()}"
print(message)
