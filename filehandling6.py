
# create a function to search a word
def check_the_word():
    with open("sample.txt", "r")as f:
        data = f.read()
    if(data.find("learning")!= -1):
        print("yes this word is exits in the file.")
    else:
        print("no learning word in the file")

check_the_word()