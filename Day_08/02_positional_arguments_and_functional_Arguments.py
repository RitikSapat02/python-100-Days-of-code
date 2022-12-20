def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?\n")

greet_with("Ritik","Nagpur")  #positional arguments

greet_with("Nagpur","Ritik")  #positional arguments

greet_with(location="Nagpur",name="Ritik") #keyword arguments 