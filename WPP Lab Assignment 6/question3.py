class Converter:
    def __init__(self,lenght,unit):
        self.length=lenght
        self.unit=unit
    def inches(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length,"inches")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*12,"inches")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*36,"inches")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*63360,"inches")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*39370.0787,"inches")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*39.3700787,"inches")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*0.393700787,"inches")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.0393700787,"inches")        
        else:
            print("not possible by this code")        
    def feet(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*0.083333,"feet")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length,"feet")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*3,"feet")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*5280,"feet")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*3280.8399,"feet")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*3.2808399,"feet")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*0.032808399,"feet")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.0032808399,"feet")        
        else:
            print("not possible by this code")
    def yards(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*0.027778,"yards")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*0.333333,"yards")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length,"yards")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*1760,"yards")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*1093.6133,"yards")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*1.0936133,"yards")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*0.010936133,"yards")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.0010936133,"yards")        
        else:
            print("not possible by this code") 
    def miles(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*0.00001578,"miles")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*0.0001893939,"miles")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*0.0005681818181,"miles")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length,"miles")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*0.621371192,"miles")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*0.000621371192,"miles")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*0.00000621371192,"miles")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.000000621371192,"miles")        
        else:
            print("not possible by this code")
    def kilometers(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*0.0000254,"kilometers")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*0.0003048,"kilometers")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*0.0009144,"kilometers")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*1.609344,"kilometers")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length,"kilometers")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*0.001,"kilometers")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*0.00001,"kilometers")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.000001,"kilometers")        
        else:
            print("not possible by this code") 
    def meters(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*0.0254,"meters")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*0.3048,"meters")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*0.9144,"meters")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*1609.344,"meters")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*1000,"meters")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length,"meters")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*0.01,"meters")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.001,"meters")        
        else:
            print("not possible by this code")
    def centimeters(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*2.54,"centimeters")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*30.48,"centimeters")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*91.44,"centimeters")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*160934.4,"centimeters")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*100000,"centimeters")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*100,"centimeters")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length,"centimeters")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length*0.1,"centimeters")        
        else:
            print("not possible by this code")  
    def millimeters(self):
        if self.unit=="inches":
            print(self.length,self.unit,"converted to",self.length*25.4,"millimeters")
        elif self.unit=="feet":
            print(self.length,self.unit,"converted to",self.length*304.8,"millimeters")
        elif self.unit=="yards":
            print(self.length,self.unit,"converted to",self.length*914.4,"millimeters")
        elif self.unit=="miles":
            print(self.length,self.unit,"converted to",self.length*1609344,"millimeters")
        elif self.unit=="kilometers":
            print(self.length,self.unit,"converted to",self.length*1000000,"millimeters")
        elif self.unit=="meters":
            print(self.length,self.unit,"converted to",self.length*1000,"millimeters")
        elif self.unit=="centimeters":
            print(self.length,self.unit,"converted to",self.length*10,"millimeters")
        elif self.unit=="millimeters":
            print(self.length,self.unit,"converted to",self.length,"millimeters")        
        else:
            print("not possible by this code")

length=int(input("enter length:\t"))
unit=input("enter units like inches/feet/yards/miles/kilometers/meters/centimeters/millimeters:\t")   
S=Converter(length,unit)
choice=1
while choice!=0:
    print("1 for inches")
    print("2 for feet")
    print("3 for yards")
    print("4 for miles")
    print("5 for kilometers")
    print("6 for meters")
    print("7 for centimeters")
    print("8 for millimeters")
    print("0 for exit")
    choice=int(input("enter your choice:\t"))
    if choice==1:
        S.inches()
    elif choice==2:
        S.feet()
    elif choice==3:
        S.yards()
    elif choice==4:
        S.miles()
    elif choice==5:
        S.kilometers()
    elif choice==6:
        S.meters()
    elif choice==7:
        S.centimeters()
    elif choice==8:
        S.millimeters() 
print("thankyou...")        



                                                                                                                              

                                                                                                                             

        
                                  
