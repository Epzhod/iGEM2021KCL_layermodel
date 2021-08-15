def main():

    # Error correction applied to this numbers is likely to lead to an overestimation of the actual surface area

    ENDS = 291 # the surface area of the vertical and horizontal 0.5mm slices at each end of the scaffold

    INNER = 216 # the surface area inside the channels per 1mm slice

    OUTER = 37 # the surface area on the outer surface per 1mm slice

    print("Please enter lenght of the scaffold in milimeters :")

    scaffold_len = input(int)

    if "." or "," not in scaffold_len:
        scaffold_len = int(scaffold_len)
    else:
        print("This calculater only accepts integer values!")


    surface_area_channel = (scaffold_len-1)*(INNER + OUTER) + ENDS

    surface_area_simple = (scaffold_len-1)*(OUTER) + ENDS

    result = "The surface area of the scaffold is: \n   -with channels: {} mm^2 \n   -without channels: {} mm^2".format(str(surface_area_channel), str(surface_area_simple))

    print(result)

if __name__ == "__main__":
    main()
