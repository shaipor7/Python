def main():
    Input = input("")
    print(convert(Input))

def convert(text):
    A = text.replace(":)" , "🙂").replace(":(" ,"🙁")
    return A

main()
