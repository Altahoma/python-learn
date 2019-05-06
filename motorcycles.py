motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'bmw')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

last_owned = motorcycles.pop(-1)
print(motorcycles)
print(last_owned)

removed_motorcycle = motorcycles.remove('bmw')
print(motorcycles)
print(removed_motorcycle)