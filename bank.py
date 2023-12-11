input = input("Greeting: ")

if "hello" in input.lower():
    print("$0")
elif "h" == input[0].lower():
    print("$20")
else:
    print("$100")