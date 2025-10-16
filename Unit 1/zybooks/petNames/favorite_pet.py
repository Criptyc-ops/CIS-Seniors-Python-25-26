# a script favorite_pet.py that imports and uses the pet_names module
import pet_names #imports the pet_names module

print("my favorite pet is", pet_names.pet_name2)
print("I remember when he weighed only", pet_names.pet_weight2, "pounds")
print("I love", pet_names.pet_name1, "too of course!")

if __name__ == "__main__":
    print("This is the __main__ code from favorite_pet.py")