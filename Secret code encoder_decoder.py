# Writing a python program to translate a message into secret code language using the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Our program should ask whether we want to code or decode

def secret_language():
    try:
        a = (input("Tell us whether you want to CODE or DECODE (C/D): "))
        if a == "C":
            x = str(input("\nWrite the word you want to code: "))
            if len(x) >= 3:
                coded = "pqr" + x[1:] + x[0] + "dfg"
                print("Required CODED word is: ")
                return coded 
            else:
                coded = x[::-1]
                print("Required CODED word is: ")
                return coded
            
        elif a == "D":
            y = str(input("\nWrite the word you want to decode: "))
            if len(y) < 3:
                decoded = y[::-1]
                print("Required DECODED word is: ")
                return decoded
            else:
                decoded = y[3:-3]
                decoded = decoded[-1] + decoded[:-1]
                print("Required DECODED word is: ")
                return decoded
    
    except Exception:
        print("\nSome error has occured.")
        return "\nFAILURE"

    finally:
        print("\nThe program has ended successfully.")


print(secret_language())