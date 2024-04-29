# burrito - 7, time - 9min, 2 burritos can be prepared at the same time.
# fries - 4, 
# sodas - 2.50 

print('a) Orders\nb) Show sales report\nc) Updated Prices\nd) Exit')

firstSelection = input('Enter your selection - a, b, c or d: ')

match firstSelection:
    case "a":   # order
        print("1. Select the food item\n2. Enter amount\n3. Show the returned change")
        orderSelection = input('Enter your selection - 1, 2 or 3: ')    
        match orderSelection:
            case 1:
                for _ in range(10):
                    print('1. Burrito\n2. Fries\n3. Soda\n4. No more')
                    foodSelection = input('Select the food item - 1, 2, 3 or 4')
                    match foodSelection:
                        case 1:
                            noOfBurritos = input('How many burritos ($7) would you like to buy: ')
                            priceOfBurritos = noOfBurritos * 7
                            timeOfBurritos = 9
                            if noOfBurritos == 1 or 2:
                                print(f'{timeOfBurritos} mins is required to prepare')
                            else:     
                                print('please wait!')

                        
                        case 2:
                            noOfFries = input('How many serves of fries ($4) would you like to buy: ')
                            print('Cooking fries, please be patient')
                            timeOfFries = 8
                            serveOfOneFries = 4
                            batchOfFries = 5
                            priceOfFries = noOfFries * serveOfOneFries
                            print(f'{batchOfFries-noOfFries}  serves of fries left for next order
')
                            
                        case 3:
                            noOfSodas = input('How many sodas ($2.50) do you require: ')
                            priceOfSodas = noOfSodas * 2.50

                        case 4:
                            break
                            
                                
                
        
    case "b":   # show sales report
        pass
    
    case "c":   # Updated Prices
        pass
    
    case "d":   # Exit
        pass
    
    case default:
        print("Invalid input")    