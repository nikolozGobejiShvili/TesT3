def main():
    fraction=input("fraction: ").split("/")
    print(gauge(convert(fraction)))


def convert(fraction):
    x= int(fraction[0])
    y= int(fraction[1])

    return int((x * 100 / y))


def gauge(percentage):

    if percentage  != 100 and percentage != 0 and percentage < 100:
        return str(percentage) + "%" 
                  
    elif   percentage == 100:
        return  "F" 
                  
            
    elif  percentage == 0:
        return "E"
                  

                  

if __name__ == "__main__":
    main()