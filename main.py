from controller import Controller
from view import View

def main():
    view = View()
    administrator = Controller(view)
    administrator.run()
    
if __name__=="__main__":
    main()

