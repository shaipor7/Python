def main():
    string = input("")
    print(convert(string))
def convert(text):
    text.replace(":)","🙂")
    text.replace(":(","🙁")
    return text
main()
