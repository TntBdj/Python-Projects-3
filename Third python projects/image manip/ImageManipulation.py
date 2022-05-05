from PIL import Image
import os

j_List = ["arch", "balloons", "dubai", "ems", "helix", "kcm", "landscape", "palace", "rio", "trees"]
a_List = ["rotate", "resize", "png", "black+white", "blur"]
size200 = (200,200)
size400 = (400,400)
size600 = (600,600)

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
        if userImageChoice in j_List:
            userImage = Image.open(f"{userImageChoice}.jpg")
            userImage.show()
            if userConfirm() == True:
                alterUserImage()
        elif userImageChoice == "q":
            break
        else:
            print("Invalid input\n")
    
def userConfirm():
    while True:
        userChoice = input("do you want to alter this image? (y/n): ")
        if userChoice.lower() == "y":
            break
        elif userChoice.lower() == "n":
            print("")
            main()
        else:
            print("Invalid input\n")
    return True

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
    im = Image.open(f"{userImageChoice}.jpg")
    im.rotate(90).save('rotation folder/'+userImageChoice+'Rotated.jpg')
    p_List.append(userImageChoice)
    print("Saved in rotation folder")

def resize():
    while True:
    userChoice = input("Do you want it to be 200x200, 400x400, 600x600?: ")
    im = Image.open(f"{userImageChoice}.jpg")
    userChoice.lower()
    if userChoice == "200x200":
        im.thumbnail(size200)
        im.save('200 jpeg/'+userImageChoice+'200.jpg')
        p_List.append(userImageChoice)
        print("Saved in 200 jpeg folder")
        break
    elif userChoice == "400x400":
        im.thumbnail(size400)
        im.save('400 jpeg/'+userImageChoice+'400.jpg')
        p_List.append(userImageChoice)
        print("Saved in 400 jpeg folder")
        break
    elif userChoice == "600x600":
        im.thumbnail(size600)
        im.save('600 jpeg/'+userImageChoice+'600.jpg')
        p_List.append(userImageChoice)
        print("Saved in 400 jpeg folder")
        break
    else:
        print("Invalid input")

def png():
    im = Image.open(f"{userImageChoice}.jpg")
    fn, fext = os.path.splitext(f"{userImageChoice}.jpg")
    im.save('png folder/{}.png'.format(fn))
    print("Saved in png folder")
    p_List.append(userImageChoice)

def blackWhite():
    im = Image.open(f"{userImageChoice}.jpg")
    im = img.convert("L")
    im.save('bw folder/'+userImageChoice+'BW.jpg')
    p_List.append(userImageChoice)
    print("Saved in bw folder")
    return

def blur():
    return

main()
