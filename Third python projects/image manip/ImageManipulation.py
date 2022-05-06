#Importing all these modules is required for the code to run completely
from PIL import Image, ImageFilter, ImageEnhance
import os, sys


#The two lists are used so repetition of typing the words is avoided
j_List = ["arch", "balloons", "dubai", "ems", "helix", "kcm", "landscape", "palace", "rio", "trees"]
a_List = ["rotate", "resize", "png", "black+white", "blur", "merge", "contrast"]


""" 
This is a simple for loop that displays the above lists 
because I don't like how lists are normally displayed
"""
def displayList(x):
    for i in x:
        print (i)
    print("")


""" 
Assures that the user wants to use the selected/shown image, if they select no they 
will be prompted to choose another image, if they select yes the program will continue
"""
def userConfirm():
    while True:
        userChoice = input("do you want to alter the image? (y/n): ")
        if userChoice.lower() == "y":
            print("")
            break
        elif userChoice.lower() == "n":
            userImageChoice = None
            return False
        else:
            print("Invalid input\n")
    return True


#This is the primary function that eventually leads to every other function being called        
def main():
    while True:
        #This makes the userImageChoice var global while still being intially declared in this function
        global userImageChoice
        #Assures the var never is an unintended value
        userImageChoice = None
        print("Saved images: ")
        #This displays the contents of the j(peg) list how I previously mentioned
        displayList(j_List)
        #Asks for the image the user wants to use for the rest of the program
        userImageChoice = input("Which image would u like to open? or (q) to quit: ")
        userImageChoice.lower()  
        #This q/break will end the entire program
        if userImageChoice == "q":
            break     
        #Shows the user the image they selected
        elif userImageChoice in j_List:
            userImage = Image.open(f"{userImageChoice}.jpg")
            userImage.show()
            x = userConfirm()
            if x == False:
                continue
            elif x == True: 
                alterUserImage()
        #Any invalid user inputs will be caught by this else statement
        else:
            print("Invalid input\n")
    
    
#This function asks the user for the alteration they would like to make to their selected image
def alterUserImage():
    while True:
        print("Alter options: ")
        #Displays the a(lteration) list just liek the j_List
        displayList(a_List)
        userChoice = input("How would you like to alter the image?: ")
        userChoice.lower()
        #The user's choice will be compared to the a list to see which alteration is selected 
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
                    #If the user chooses to merge images, they will be asks to choose another image which is saved in a list
                    while True:
                        displayList(j_List)
                        userImageChoice2 = input("Which image would u like to merge with your orginal choice?: ")
                        userImageChoice2.lower()  
                        if userImageChoice2 in j_List:
                            m_list = [f"{userImageChoice}.jpg",f"{userImageChoice2}.jpg"]
                            break
                        else:
                            print("Invalid input\n")  
                    #The saved list is then used as a parameter to merge the images
                    merge(m_list)
                    break
                elif userChoice == a_List[6]:
                    contrast()   
                    break
        #If the user's input is not in the a list they will be told it is an invalid input and prompted again
        else:
            print("Invalid input\n")


#This function will rotate the image to how many degrees the user inputs then save it in the corresponding folder
def rotate():
    while True:
        #This asks the user for how many degrees they want the picture to rotate
        try:
            userDegrees = int(input("How many degrees would you like to rotate?: "))
            break
        except ValueError:
            print("Invalid input\n")
    im = Image.open(f"{userImageChoice}.jpg")
    #This rotates the picture the user inputed degrees
    im.rotate(userDegrees).save('rotation folder/'+userImageChoice+'Rotated.jpg')
    print("Saved in rotation folder\n")


#This function will create a thumbnail to the size(200/400/600) the user chooses then save it in the corresponding folder
def resize():
    size200 = (200,200)
    size400 = (400,400)
    size600 = (600,600)
    while True:
        #This asks the user for 1 of 3 sizes then saves a thumbnail of the chosen size
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


#This function will change the image file from a jpg to a png then save it in the corresponding folder
def png():
    im = Image.open(f"{userImageChoice}.jpg")
    fn, fext = os.path.splitext(f"{userImageChoice}.jpg")
    im.save('png folder/{}.png'.format(fn))
    print("Saved in png folder\n")


#This function will change the image to black and white then save it in the corresponding folder
def blackWhite():
    im = Image.open(f"{userImageChoice}.jpg")
    im = im.convert("L")
    im.save('bw folder/'+userImageChoice+'BW.jpg')
    print("Saved in bw folder\n")
    
  
#This function will blur the image how much the user wants then save it in the corresponding folder   
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


#This will merge the first and second chosen images together then save it in the corresponding folder
def merge(list):
    images = [Image.open(x) for x in list]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    im1 = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
        im1.paste(im, (x_offset,0))
        x_offset += im.size[0]
    im1.save('merge folder/'+userImageChoice+'Merge.jpg')
    print("Saved in merge folder\n")
   
  
#This function will greatly increase the contrast of an image then save it in the corresponding folder   
def contrast():
    im = Image.open(f"{userImageChoice}.jpg")
    enh = ImageEnhance.Contrast(im)
    enh.enhance(2.1).save('contrast folder/'+userImageChoice+'Contrast.jpg')
    print("Saved in contrast folder\n")


main()
