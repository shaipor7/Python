string = input("File name: ")

string = string.strip().casefold()
end = string.split(".")
if string.endswith((".gif",".png")):
    print("image/"+ end[-1])
elif string.endswith((".jpg",".jpeg")):
    print("image/jpeg")
elif string.endswith((".pdf", ".zip")):
    print("application/"+end[-1])
elif string.endswith(".txt"):
    print("text/plain")
else: print("application/octet-stream")
