def main():

    def do_important():
        """This function does something very important"""
        print("I'm doing some important stuff here!")
    do_important()    
        
print("Called from important_new.py, __name__ has value?:", __name__)
if __name__ == "__main__":
    main()