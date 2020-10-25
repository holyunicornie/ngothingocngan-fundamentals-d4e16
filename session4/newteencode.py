dictionary = {
    "hc" : "học",
    "any" : "anh người iu",
    "hk" : "không"
}
#mapping = {
    #"018" : "03"
#}
while True:
    for key in dictionary:
        print(key, end="\t") #n ở đây = enter (xuống dòng), \t = 1 tab
    print()
    input_key = input("your code?")
    if input_key in dictionary:
        print("it means:", dictionary[input_key])
    else:
        choice = input("Not found your word, wanna contrib? [Y/N]").upper()
        if choice == "Y":
            dictionary[input_key] = input("enter its meaning")
        else:
            print("bye")
            break