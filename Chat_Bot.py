print("------------Welcome to the Chat Bot!------------")
name = input("Enter your name : ")
print("Hello, " + name + "! I am here for you ?")

def Chat():
    pass
    while True:
        chat = input("Enter your message : ").lower()
        if(chat == "hi" or chat == "hello" or chat == "hey"):
            print("Hi there! How can I assist you today?")
        elif(chat == "how are you?"):
            print("I am doing well, thank you! How about you?")
        elif(chat == "what is chatgpt?"):
            print("ChatGPT is an AI language model developed by OpenAI. It can understand and generate human-like text based on the input it receives.")
        elif(chat == "what is your name?"):
            print("I am ChatGPT, your friendly AI assistant!")
        elif(chat == "bye" or chat == "by" or chat == "goodbye"):
            print("Goodbye! Thanks for using me!")
def calculator():
    pass
    while True:
        calculation = input("Enter your calculation : ")
        try:
            result = eval(calculation)
            print("The result is: ", result)
        except:
            print("Invalid calculation!")

print("1. Chat")
print("2. Calculator")
option = input("Enter your option (1/2): ")
if option == "1": 
    Chat()
elif option == "2":
    calculator()
else:
    print("Invalid option! Please choose either 1 or 2.")