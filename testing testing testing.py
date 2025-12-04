# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        print('Hello!')
        print('Welcome to Python')
        print('Lets learn together')
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [Nuclear reactor temperature check]
def check_temperature(temp_celsius):
    try:
        temp=temp_celsius
        if temp <= 300:
            print('The temperature is safe')
        elif temp > 300 and temp <400:
            print('Warning Yhe temperature is unsafe')
        else:
            print('The temperature is critically unsafe')
        pass   
    except Exception as e:
        print("Error occurred:", e )

# Drama school audition scoring
def calculate_avg_score(acting, voice, movement):
    try:
        total=acting+voice+movement
        average= total // 3
        if average >= 70:
            print('Pass')
        else:
            print('fail')
        pass   
    except Exception as e:
        print("Error occurred:", e )
# [comment]
def nothing():
    try:
        
        temp_celsius=int(input('Whats the temperature of the nuclear reactor:  '))
        check_temperature(temp_celsius)

        acting=int(input('Submit acting score gotten during audition: '))
        voice=int(input('Submit voice score gotten during audition: '))
        movement=int(input('Submit movement score gotten during audition: '))
        calculate_avg_score(acting, voice, movement)
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def Passwordgen():
    try:
        import string, random
        
        pass   
    except Exception as e:
        print("Error occurred:", e )


# [comment]
def Questions(up, low, sym):
    try:
        up=False
        low=False
        sym=False
        if u==1:
            up = True
            return up
        if l==1:
            low = True
            return low
        if s==1:
            sym = True
            return sym
        return length
   
    except Exception as e:
        print("Error occurred:", e )
# [comment]
def Strength_check():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        u=int(input('Would you like there to be uppercase?: 1 = yes, 0 = no'))
        l=int(input('Would you like there to be lowercase?: 1 = yes, 0 = no'))
        s=int(input('Would you like there to be symbols?: 1 = yes, 0 = no'))
        length=int(input('How long would you like this password to be?: 8, 12, 20  '))
        ups, los, sos, hos = Questions(up, low, sym)
        print()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
