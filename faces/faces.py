def main():
    string = input("")
    print(convert(string))
def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")
main()
