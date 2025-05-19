
# create a function which line found the word
def find_the_line():
    data = True
    word = "learning"
    line_no = 1
    with open("sample.txt", "r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

print(find_the_line())
