import numpy

H = 0.5 #diameter of a log

VF = vertical_face = {
    # format: short length , long length, side 
    # DO NOT FORGET ARRAYS START AT 0
    # DO NOT FORGET TO DOUBLE SIDES when getting perimeter
    "1": [3.5, 5.8, 1.3],
    "2": [7.4, 8.4, 0.7],
    "3": [9.4, 10, 0.6],
    "w1": [10.7, 11, 0.25],
    "w2": [3, 3, 0.25],
    "P": [3, 3, 0.5] # Capital P
}

HF = horizontal_face = {
    "1": [1.2, 1.75, 0.75],
    "2": [2.2, 2.7, 0.6],
    "3": [2.8, 3.1, 0.6],
    "w1": [11.6, 11.7, 0.25],
    "w2": [3.3, 3.3, 0.25],
    "L": [12, 12, 0.5]  # Capital L
}

VW = vertical_wedge = [1.75, 5, 1.75] # holes solid holes
HW = horizontal_wedge = [4, 2.5, 4] # solid holes solid

VO = vertical_edge = [VF['w1'][2], VF['3'][2], VF['2'][2], VF['1'][2], 0.5*(VF['1'][0])] # multiply by four for whole circle; (3.5 side/2 = 1.75)
HO = horizontal_edge = [HF['1'][0], HF['1'][2], HF['2'][2], HF['3'][2], HF['L'][2], HF['L'][2]] #top of shortest + side*5; again mutlipy by four


def S_trap (a, b, h = H):
    # formula for calculating surface area of a trapezoid
    return (a+b)*0.5*h


def S_face ( M ):
    # general calculation of a face
    result = 0

    result += S_trap(M['1'][0], M['1'][1])
    result += S_trap(M['2'][0], M['2'][1])
    result += S_trap(M['3'][0], M['3'][1])

    return result

def S_vertical_face (M = vertical_face):
    result = S_face(M) # irregular logs on one side
    result += S_trap(M['w1'][0], M['w1'][1])
    result = result*2 # double it
    result += 3*H*5 # regular logs between the wedge

    return result

def S_horizontal_face (M = horizontal_face):
    result = 2*(S_face(M)) # irregular logs on each side
    result += S_trap(M['w1'][0], M['w1'][1])*(H/2)
    result += 3.3*(H/2)*2 # the w2 bit
    result += 12*H # regular log
    result = result*2 # double it

    return result

print(S_vertical_face())
print(S_horizontal_face())
    

def S_wedge (M1 = vertical_wedge, M2 = horizontal_wedge):

    result = 0

    for ele in M1:
        result += ele*H

    for ele in M2:
        result += ele*H

    result = result*2 # double it because both wedges

    return result # for vertical + horizontal 


def S_edge (M1 = vertical_edge, M2 = horizontal_edge):

    result = 0

    for ele in M1:
        result += ele*H

    for ele in M2:
        result += ele*H

    result = result*4 # quadruple it

    return result


print(S_wedge())
print(S_edge())


def S_channel (a, b, across, full = True):
    """Calculates the inner area of a pore channel based on 
    a = side a = the left or top side length of the channel
    b = side b = the right or bottom side length of the channel
    across = how many logs come across the channel
    """
    if full:
        result = a*H + b*H + H*H*across*2     # last part assumes squares of exposed logs on both sides of the channel

    else:
        result = a*H + b*H + H*H*across       # assumes open on one side

    return result

def S_vertical_channels (M = vertical_face, full = True):

    result = 0
    result += S_channel(M['1'][1], M['2'][0], 6, full)
    result += S_channel(M['2'][1], M['3'][0], 9, full)
    result += S_channel(M['3'][1], M['w1'][0], 10, full)
    result = result*2
    result += 5*(S_channel(M['P'][0], M['2'][1], 3, full))

    return result

def S_horizontal_channels (M = horizontal_face, full = True):

    result = 0
    result += S_channel(M['1'][1], M['2'][0], 2, full)
    result += S_channel(M['2'][1], M['3'][0], 3, full)
    result += S_channel(M['3'][1], M['w2'][0], 4, full)
    result = result*4
    result += 2*(S_channel(M['w1'][1], M['L'][0], 12, full))
    result += S_channel(12, 12, 12, full)

    return result


print(S_vertical_channels())
print(S_horizontal_channels())


S_outside = S_vertical_face() + S_horizontal_face() + S_wedge() + S_edge() + S_vertical_channels (M = vertical_face, full = False) + S_horizontal_channels (M = horizontal_face, full = True)

print(S_outside)

S_inside = S_wedge() + S_edge() + S_vertical_channels() + S_horizontal_channels()

print(S_inside)