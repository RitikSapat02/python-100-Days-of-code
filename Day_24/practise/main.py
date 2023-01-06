#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Day_24/practise/Input/Names/invited_names.txt","r") as data:
    NameList = data.readlines()
    
with open("./Day_24/practise/Input/Letters/starting_letter.docx") as data:
    letter = data.read()

    for name in NameList:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]",stripped_name)

        with open(f"./Day_24/practise/Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as data:
            data.write(new_letter)
