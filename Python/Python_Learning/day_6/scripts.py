# here we will discuss 
# if __name__ == "__main__":
#     main()

# we write this nasty line of code because when we are writing a program
# and import from other modules(scripts) than we only want to borrow a function
# and do not want to whole body of the script to run thats why we write this
# other wise whole body of the script will start running

def fav_food(food):
    print(f"your favourite food is: {food}")
    
def main():
    print("script 1")
    fav_food("burger")
    print("good bye")
    
if __name__ == "__main__":
    main()
