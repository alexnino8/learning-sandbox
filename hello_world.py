def greet(name: str) -> str: #Defines a function called greet that takes a single parameter name, which should be a string (str). The -> str means the function will return a string. This is type hinting, which is optional in Python but good practice for clarity.
   return f"Hello, {name}! Welcome to the learning sandbox." #This line returns a formatted string using an f-string, inserting the value of name into the greeting message.

if __name__ == "__main__": #This line ensures that the code inside this block only runs when the script is executed directly, not when it’s imported as a module in another script.
  user_name = input("Enter your name: ") #Prompts the user to type their name. The input() function captures what the user types and stores it in the variable user_name.
  message = greet(user_name) #Calls the greet() function with the user's name and stores the returned greeting in the variable message.
  print(message) #Displays the greeting message to the user in the terminal or console.
  

      

  


