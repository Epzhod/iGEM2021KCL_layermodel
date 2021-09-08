    # Error correction applied to this numbers is likely to lead to an overestimation of the actual surface area

ENDS = 291 # the surface area of the vertical and horizontal 0.5mm slices at each end of the scaffold

INNER = 216 # the surface area inside the channels per 1mm slice

OUTER = 37 # the surface area on the outer surface per 1mm slice
    
PLEN = 90.3/(10**7) # length of protein
    
PWID = 47.6/(10**7) # width of protein
    
PHIG = 33.7/(10**7) # hight of protein

PrMW = 14008.9221 # molecular weight of protein (g/mol)

avogadro_constant = 6.02214076 * (10**23) 



def Input():
    
    print("Please enter lenght of the scaffold in milimeters :")

    scaffold_len = input(int)

    if "." or "," not in scaffold_len:
        scaffold_len = int(scaffold_len)
    else:
        print("This calculater only accepts integer values!")
        
    return(scaffold_len)

INLEN = Input()

def Scalc(scaffold_len = INLEN):
    
    surface_area_channel = (scaffold_len-1)*(INNER + OUTER) + ENDS

    surface_area_simple = (scaffold_len-1)*(OUTER) + ENDS

    result = "The surface area of the scaffold is: \n   -with channels: {} mm^2 \n   -without channels: {} mm^2".format(str(surface_area_channel), str(surface_area_simple))

    return(result, surface_area_channel, surface_area_simple)


def Pcalc(Scalc = Scalc()[1]):
    
    protein_area = PLEN*PWID
    
    protein_units = Scalc//protein_area
    
    return(protein_units)

def chemcalc(Punits = Pcalc()):
    
    Pmoles = Punits / avogadro_constant
    
    Pweight = Pmoles * PrMW
    
    return(Pweight, Pmoles)

if __name__ == "__main__":
    print(Scalc()[0])
    print("Units of protein needed = " + str(Pcalc()))
    print("Moles of protein needed = " + str(chemcalc()[1]))
    print("Grams of protein needed = " + str(chemcalc()[0]))