class LayerCalc:
     
    def __init__(self, inlen):
        self.INLEN = inlen
        
        # Error correction applied to this numbers is likely to lead to an overestimation of the actual surface area

        self.ENDS = 291 # the surface area of the vertical and horizontal 0.5mm slices at each end of the scaffold

        self.INNER = 216 # the surface area inside the channels per 1mm slice

        self.OUTER = 37 # the surface area on the outer surface per 1mm slice
        
        self.PLEN = 90.3/(10**7) # length of protein
        
        self.PWID = 47.6/(10**7) # width of protein
        
        self.PHIG = 33.7/(10**7) # hight of protein

        self.PRMW = 14008.9221 # molecular weight of protein (g/mol)

        self.AVGC = 6.02214076 * (10**23)  # avogadro constant
        
        # results of calculations 
        
        self.surface_area = self.Scalc()[0]
        self.protein_units = self.Pcalc()
        self.protein_moles = self.chemcalc()[0]
        self.protein_grams = self.chemcalc()[1]
    
    
    def Scalc(self):
        
        scaffold_len = self.INLEN
        
        surface_area_channel = (scaffold_len-1)*(self.INNER + self.OUTER) + self.ENDS

        surface_area_simple = (scaffold_len-1)*(self.OUTER) + self.ENDS

        output = "The surface area of the scaffold is: \n   -with channels: {} mm^2 \n   -without channels: {} mm^2".format(str(surface_area_channel), str(surface_area_simple))

        return(surface_area_channel, output, surface_area_simple)


    def Pcalc(self):
        
        Scalc = self.Scalc()[0]
        
        protein_area = self.PLEN*self.PWID
        
        protein_units = Scalc//protein_area
        
        return(protein_units)
    

    def chemcalc(self):
        
        Punits = self.Pcalc()
        
        Pmoles = Punits / self.AVGC
        
        Pweight = Pmoles * self.PRMW
        
        return(Pmoles, Pweight)
    
    def print_output(self):
        
        line1 = self.Scalc()[1]
        line2 = "Units of protein needed = " + str(self.Pcalc())
        line3 = "Moles of protein needed = " + str(self.chemcalc()[0])
        line4 = "Grams of protein needed = " + str(self.chemcalc()[1])
        
        result = line1+'\n'+line2+'\n'+line3+'\n'+line4
        
        print(result)