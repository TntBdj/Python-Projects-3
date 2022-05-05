from PIL import Image
import os

j_List = ["arch", "balloons", "dubai", "ems", "kcm", "landscape", "palace", "rio", "trees"]
p_List = []
a_List = ["rotate", "resize", "png", "black+white", "blur"]


def displayList(x):
    for i in x:
        print (i)
    print("")
        
def main():
    while True:
        global userImageChoice
        userImageChoice = ""
        print("Saved images: ")
        displayList(j_List)
        userImageChoice = input("Which image would u like to open? or (q) to quit: ")
        userImageChoice.lower()
        if userImageChoice in j_List and userImageChoice in p_List:
            p_or_j = input("Would you like to open the png or jpg version?: ")
            p_or_j.lower()
            if p_or_j == "jpg":
                userImage = Image.open(f"{userImageChoice}.jpg")
                userImage.show()
            elif p_or_j == "png":
                userImage = Image.open(f"{userImageChoice}.png")
                userImage.show()
            
        elif userImageChoice in j_List:
            userImage = Image.open(f"{userImageChoice}.jpg")
            userImage.show()
            if userConfirm() == True:
                alterUserImage()
        elif userImageChoice == "q":
            break
        else:
            print("Invalid input\n")
    
def userConfirm():
    userChoice = input("do you want to alter this image? (y/n): ")
    if userChoice.lower() == "y":
        return True
    elif userChoice.lower() == "n":
        print("")
        main()
    else:
        print("Invalid input")

def alterUserImage():
    while True:
        print("Alter options: ")
        displayList(a_List)
        userChoice = input("How would you like to alter the image?: ")
        userChoice.lower()
        if userChoice in a_List:
            if userConfirm() == True:
                if userChoice == a_List[0]:
                    rotate()
                    break
                elif userChoice == a_List[1]:
                    resize()
                    break
                elif userChoice == a_List[2]:
                    png()
                    break
                elif userChoice == a_List[3]:
                    blackWhite()
                    break
                elif userChoice == a_List[4]:
                    blur()   
                    break
        else:
            print("Invalid input\n")

def rotate():
    return

def resize():
    return

def png():
    i = Image.open(f"{userImageChoice}.jpg")
    fn, fext = os.path.splitext(f"{userImageChoice}.jpg")
    i.save('png folder/{}.png'.format(fn))
    p_List.append(userImageChoice)
    print(p_List)

def blackWhite():
    return

def blur():
    return


main()
