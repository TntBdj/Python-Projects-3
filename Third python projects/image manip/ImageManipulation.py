from PIL import Image, ImageFilter, ImageEnhance
import os, sys

j_List = ["arch", "balloons", "dubai", "ems", "helix", "kcm", "landscape", "palace", "rio", "trees"]
a_List = ["rotate", "resize", "png", "black+white", "blur", "contrast"]
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
        userImageChoice = None
        print("Saved images: ")
        displayList(j_List)
        userImageChoice = input("Which image would u like to open? or (q) to quit: ")
        userImageChoice.lower()  
        if userImageChoice == "q":
            break     
        elif userImageChoice in j_List:
            userImage = Image.open(f"{userImageChoice}.jpg")
            userImage.show()
            x = userConfirm()
            if x == False:
                continue
            elif x == True:
                alterUserImage()
        else:
            print("Invalid input\n")
    
def userConfirm():
    while True:
        userChoice = input("do you want to alter the image? (y/n): ")
        if userChoice.lower() == "y":
            break
        elif userChoice.lower() == "n":
            userImageChoice = None
            return False
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
                elif userChoice == a_List[5]:
                    contrast() 
                    break
        else:
            print("Invalid input\n")

def rotate():
    while True:
        try:
            userDegrees = int(input("How many degrees would you like to rotate?: "))
            break
        except ValueError:
            print("Invalid input\n")
    im = Image.open(f"{userImageChoice}.jpg")
    im.rotate(userDegrees).save('rotation folder/'+userImageChoice+'Rotated.jpg')
    print("Saved in rotation folder\n")

def resize():
    while True:
        userChoice = int(input("Do you want it to be 200, 400, 600: "))
        im = Image.open(f"{userImageChoice}.jpg")
        if userChoice == 200:
            im.thumbnail(size200)
            im.save('200 jpeg/'+userImageChoice+'200.jpg')
            print("Saved in 200 jpeg folder\n")
            break
        elif userChoice == 400:
            im.thumbnail(size400)
            im.save('400 jpeg/'+userImageChoice+'400.jpg')
            print("Saved in 400 jpeg folder\n")
            break
        elif userChoice == 600:
            im.thumbnail(size600)
            im.save('600 jpeg/'+userImageChoice+'600.jpg')
            print("Saved in 600 jpeg folder\n")
            break
        else:
            print("Invalid input")

def png():
    im = Image.open(f"{userImageChoice}.jpg")
    fn, fext = os.path.splitext(f"{userImageChoice}.jpg")
    im.save('png folder/{}.png'.format(fn))
    print("Saved in png folder\n")

def blackWhite():
    im = Image.open(f"{userImageChoice}.jpg")
    im = im.convert("L")
    im.save('bw folder/'+userImageChoice+'BW.jpg')
    print("Saved in bw folder\n")
    
def blur():
    while True:
        try:
            userBlur = float(input("How much would you like to blur (Choose a number)?: "))
            break
        except ValueError:
            print("Invalid input\n")
    im = Image.open(fr"{userImageChoice}.jpg")    
    im1 = im.filter(ImageFilter.GaussianBlur(userBlur))
    im1.save('blur folder/'+userImageChoice+'Blur.jpg')
    print("Saved in blur folder\n")

def contrast():
    im = Image.open(f"{userImageChoice}.jpg")
    im.save('contrast folder/'+userImageChoice+'Contrast.jpg')
    im1 = ImageEnhance.Contrast(im)
    con_im = im1.enhance(1.3).show("30% more contrast")
    con_im.save('contrast folder/'+userImageChoice+'Contrast.jpg')

main()
