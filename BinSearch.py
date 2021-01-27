# coding: utf-8



''' find är funktionen som hittar vilket tal du söker i listan genom att halvera sig närmare och närmare det sökta talet tills den
    hittar den. '''
def find(numbers, n): 
    position = -1 # Detta gör så att ifall den inte hittar talet i listan så kan programet veta det
    higher = len(numbers) - 1
    lower = 0
    middle = 0 
    
    while higher >= lower: 
        middle = (higher + lower) // 2
        if numbers[middle] == n: # Kollar om talet är mitt i mellan higher och lower och ifall den är har man hittat var den är
            position = middle + 1
            return position
        elif numbers[middle] < n: # Kollar om numret är större än halva
            lower = middle + 1
        elif numbers[middle] > n: # Kollar om numret är mindre än halva 
            higher = middle - 1
            
    return position



''' Denna funktion genererar en slumpmäsig lista genom att ta hur många element man ska ha och hur stor variation med nummer man
    ska ha, genom att kolla vilket nummer som är skrivit i numberSpan. '''
def generateList(element, numberSpan):
    import random
    numbers = []
    
    for z in range(0,element):
        randomNumber = random.randint(0,numberSpan)
        numbers.append(randomNumber)
        
    numbers.sort() # Sorterar listan så att den binära sökningen kan hitta den.
    return numbers



''' Denna funktion är till för att göra det interaktivt och andvändarvänligt genom att fråga användaren vilket heltal dom vill söka,
    hur många olika heltal användaren vill ha i sin lista, och hur stort det slumpmässiga talen ska kunna bli. '''
def interactiv():
    print('-'*50)
    validInput = True
    errorText = 'Hoppsan! Det där var inte ett heltal, försök igen..'
    
    # Denna while loop loopar konstant tills den tar sig till en break, där den bara kan göra det ifall den hittar ett heltal.
    while not validInput:
        try:
            n = int(input('Skriv ditt heltal du vill hitta: '))
            break
        except ValueError:
            print(errorText) 
    print('-'*50)
    while not validInput:
        try:
            element = int(input('Skriv in hur många heltal du vill generera: '))
            break
        except ValueError:
            print(errorText)     
    print('-'*50)
    while not validInput:
        try:
            numberSpan = int(input('Skriv hur stort heltal du vill kunna generera: '))
            break
        except ValueError:
            print(errorText)      
    runTestCode(n, element, numberSpan) 
   


''' Denna funktion är test kod för att kolla att programet fungerar samt kod för att göra det mer användarvänligt
    och lättare att förstå vad som hände och ifall talet andvändaren sökte fanns med i listan. '''
def runTestCode(n, element, numberSpan):
    print('-'*50)
    numbers = generateList(element, numberSpan)
    print("Din lista: ",numbers)
    print("Det sökta talet :",n)
    position = find(numbers, n)
    
    if (position >= 0):
        print(n, "Finns på plats", position)
    else:
        print(n, "finns inte med i listan")



''' runTestCode(n, element, numberSpan) där n är numret du vill hitta, element är mängden element, 
    och numberSpan är variatoinen i nummer. '''
runTestCode(1, 20, 100)
runTestCode(9, 19, 99)
runTestCode(42, 14, 72)
interactiv()

''' Fråga: Hur många jämförelser krävs för binär sökning för en lista med 1000 element? 
    Svar: Binär sökning behöver 9 jämförelser med binär sökning  '''