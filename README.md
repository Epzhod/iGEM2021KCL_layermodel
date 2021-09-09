# PVFP5 to PCL amount binding model

## Files:
 - surface_area_static.py: the calculations of the surface area of the elements of the scaffold
 - legend.png: a guide to the naming conventions in the measurement dictionary at the top in surface_area_static.py
 - constants.py: the constants and functions used to calculate the different variables dependant on scaffold length; now outdated, kept for reference
 - dimensions.png: measurments of a unit of Pvfp-5
 - calcer.py: improvement upon constats.py, same functions but in the form of a class
 - graphing.ipynb: Jupyter Notebook to plot things as needed
 - calcer.html: same as calcer.py, but html+javascript so its more accessible
 
 ## Constants used:
 - ENDS = 291 : the surface area of the vertical and horizontal 0.5mm slices at each end of the scaffold [calculated by surface_area_static.py]
 - INNER = 216 : the surface area inside the channels per 1mm slice [calculated by surface_area_static.py]
 - OUTER = 37 : the surface area on the outer surface per 1mm slice [calculated by surface_area_static.py]
 - PLEN = 90.3/(10**7) : length of protein in mm [calculated in PyMOL, see dimesions.png]
 - PWID = 47.6/(10**7) : width of protein in mm [calculated in PyMOL, see dimesions.png]
 - PHIG = 33.7/(10**7) : hight of protein in mm [calculated in PyMOL, see dimesions.png]
 - PRMW = 14008.9221 : molecular weight of protein (g/mol) [calculated in PyMOL]
 - AVGC = 6.02214076 * (10**23)  : avogadro constant [referenced from Encyclopedia Britannica]

### Protein Dimensions
In order to create dimensions.png PyMOL was used with this script: https://pymolwiki.org/index.php/Draw_Protein_Dimensions <br/>
Credit goes to Pablo Guardado Calvo as the creator of the script
