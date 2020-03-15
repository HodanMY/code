print("Welcome to your Horoscope Online!\nPlease complete the following questions.")


while True: 
        day = int(input("\nWhat day were you born? i.e 1-30: "))
        month = input("What month were you born in? i.e May, July etc: ").lower()

        def earth_sign():
            print("Your zodiac element is Earth")
        def water_sign():
            print("Your zodiac element is Water")
        def air_sign():
            print("Your zodiac element is Air")
        def fire_sign():
            print("Your zodiac element is Fire")


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

        fire_element = "\nYour Zodiac element is Fire "
        water_element = "\nYour Zodiac element is Water"
        air_element = "\nYour Zodiac element is Air"
        earth_element = "\nYour Zodiac element is Earth"

        
                
        if month == 'december':
                                star_sign = sagittarius if (day < 22) else capricorn 
                              
        elif month == 'january':
                                star_sign = capricorn if (day < 20) else aquarius
                               
        elif month == 'february':
                                star_sign = aquarius if (day < 19) else pisces
                              
        elif month == 'march':
                                star_sign = pisces if (day < 21) else aries
                              
        elif month == 'april':
                                star_sign = aries if (day < 15) else taurus
                              
        elif month == 'may':
                                star_sign = taurus if (day < 21) else  gemini
                 
        elif month == 'june':
                                star_sign = gemini if (day < 21) else cancer                    
                                
        elif month == 'july':
                                star_sign = cancer if (day < 23) else leo
        
        elif month == 'august':
                                star_sign = leo if (day < 23) else virgo
                                
        elif month == 'september':
                                star_sign = virgo if (day < 23) else libra
                                
        elif month == 'october':
                                star_sign = libra if (day < 23) else scorpio
                              
        elif month == 'november':
                                star_sign = scorpio if (day < 22) else sagittarius
                               
                               
            

        print("Your Astrological Sign is " + star_sign)

        if star_sign == 'capricorn' or 'taurus' or 'virgo' :
            earth_sign()
        elif star_sign == 'cancer' or 'scorpio' or 'pisces':
            water_sign()
        elif star_sign == 'leo' or 'aires' or 'sagittarius':
            fire_sign()
        elif star_sign == 'gemini' or 'libra' or 'aquarius' :
            air_sign()



        restart = input("Would you like to try again? (y/n)")

        if restart == 'y':
            continue 
        elif restart == 'n':
            break
