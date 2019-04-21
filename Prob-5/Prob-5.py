# Module 2
#   Programming Assignment 3
#     Prob-5.py



# Cody Martin

# receipt details

#**The Problem: Print a Receipt**
#- You purchased the following:
 #   - 2 slices of pizza at $2.00 per slice
  #  - 1 large Coke at $1.50
   # - 2 donuts at $0.56 each
#- print the items purchased and their cost, one item per line
#- print the total of all items
#- print the sales tax (8.4% of the total)
#- print the grand total
#- ask the user to enter an amount
#- print the amount tendered
#- print the change due

def main():

# item cost

    pizza = 2.00
    coke = 1.59
    donuts = .56

# formatting header

    print("Quanity/Item", "Cost", sep = "     ")
    
    print("-------------------------------") #divider

    print()

# items cost multiplied by quanity purchased (item * quanity)

    ap = float(pizza * 2)
    print("(2) Pizza", ap, sep = "        $")

    ac = float(coke * 1)
    print("(1) Coke", ac, sep = "         $")

    ad = float(donuts * 2)
    print("(2) Donuts", ad, sep = "       $")

    print("-------------------------------") #divider

    print()

# Total/tax/tendered/change 

    subtotal = (ap + ac + ad)
    print("Subtotal", subtotal, sep = "         $")

    Tax = (subtotal * .084)
    print("Tax", ad, sep = "              $")

    print()

    Total = (subtotal + Tax)
    Tot = round(Total,2) #rounded 
    print("Total", Tot, sep = "            $")


    print("-------------------------------") #divider

    print()

    Cash = 10
    print("Tendered Amount", Cash, sep = "  $")

    change = (Cash - Tot)
    changes = round(change,2)
    print("Change", changes, sep = "           $")





main()