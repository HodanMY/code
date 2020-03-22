print("Welcome to your Horoscope Online!")

name = input("\nWhat is your name? :")

print( "Hi " + name.title() + "\nPlease complete the following questions.")


while True: 
        day = int(input("\nWhat day were you born? i.e 1-30: "))
        month = input("What month were you born in? i.e May, July etc: ").lower()
            

        cancer = "Cancer"
        scorpio = "Scorpio"
        pisces = "Pisces"

        aries = "Aires"
        leo = "Leo"
        sagittarius = "Sagittarius"

        taurus = "Taurus"
        virgo = "Virgo"
        capricorn = "Capricorn"

        gemini = "Gemini"
        libra = "Libra"
        aquarius = "Aquarius"

        

        def zodiac_element(x):
                print("\nYour zodiac element is " + x.title())
                return
                
        if month == 'december':
                star_sign = sagittarius if (day < 22) else capricorn
                if star_sign == sagittarius:
                        zodiac_element('fire')
                elif star_sign == capricorn:
                        zodiac_element('earth')
                              
        elif month == 'january':
                star_sign = capricorn if (day < 20) else aquarius

                if star_sign == capricorn:
                        zodiac_element('earth')
                elif star_sign == aquarius:
                        zodiac_element('air')
                               
        elif month == 'february':
                star_sign = aquarius if (day < 19) else pisces

                if star_sign == aquarius:
                        zodiac_element('air')
                elif star_sign == pisces:
                        zodiac_element('water')
                              
        elif month == 'march':
                star_sign = pisces if (day < 21) else aries

                if star_sign == pisces:
                        zodiac_element('water')
                elif star_sign == aries:
                        zodiac_element('fire')
       
        elif month == 'april':
                star_sign = aries if (day < 15) else taurus

                if star_sign == aries:
                        zodiac_element('fire')
                elif star_sign == taurus:
                        zodiac_element('earth')
                              
        elif month == 'may':
                star_sign = taurus if (day < 21) else  gemini

                if star_sign == taurus:
                        zodiac_element('earth')
                elif star_sign == gemini:
                        zodiac_element('air')
          
        elif month == 'june':
                star_sign = gemini if (day < 21) else cancer                    

                if star_sign == gemini:
                        zodiac_element('air')
                elif star_sign == cancer:
                        zodiac_element('water')
                                
        elif month == 'july':
                star_sign = cancer if (day < 23) else leo

                if star_sign == cancer:
                        zodiac_element('water')
                elif star_sign == leo:
                        zodiac_element('fire')
                  
        
        elif month == 'august':
                star_sign = leo if (day < 23) else virgo

                if star_sign == leo:
                        zodiac_element('fire')
                elif star_sign == virgo:
                        zodiac_element('earth')
                 
        elif month == 'september':     
                star_sign = virgo if (day < 23) else libra
                
                if star_sign == virgo:
                        zodiac_element('earth')
                elif star_sign == libra:
                        zodiac_element('air')                   
        
        elif month == 'october':
                star_sign = libra if (day < 23) else scorpio
                
                if star_sign == libra:
                        zodiac_element('air')
                elif star_sign == scorpio:
                        zodiac_element('water')                  
        elif month == 'november':
                star_sign = scorpio if (day < 22) else sagittarius
                
                if star_sign == scorpio:
                        zodiac_element('water')
                elif star_sign == sagittarius:
                        zodiac_element('fire')


        print("Your Astrological Sign is " + star_sign)

        restart = input("Would you like to try again? (y/n)")

        if restart == 'y':
                continue 
        elif restart == 'n':
                break 