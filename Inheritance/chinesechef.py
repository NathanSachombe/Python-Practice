from chef import Chef 

class ChineseChef(Chef):    #Inheritance

    def make_special_dish(self):            #Overriding the make special dish method from the chef class
        print("The chef makes  dumplings")

    def make_fried_rice(self):
        print("The chef makes fried rice")

