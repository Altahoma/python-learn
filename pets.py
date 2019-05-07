def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name='tomas', animal_type='cat')
describe_pet(pet_name='Gav')
