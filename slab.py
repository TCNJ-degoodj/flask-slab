# Calculate the maximum wall load (in pounds per linear square foot)
# that the edge of a concrete slab-on-grade floor can support
# by providing the following inputs:
#   fc = Compressive strength in pounds per square inch or kiloPascals
#   k = Modulus of subgrade reaction in picocurie or MegaPascals
#   te = Slab thickness in inches or millimeters

def concreteSlabMaxWallLoad(fc, k, te):
    # implements the formula at
    # https://www.easycalculation.com/engineering/civil/concrete-slab-maximum-wall-load.php

    # FIXME - replace this stub with the correct formula
    p = fc + k + te
    return p

# simple unit test
# usage: python slab.py 3000 150 12

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    print(concreteSlabMaxWallLoad(float(args[0]), float(args[1]), float(args[2])))
