def printPattern(p,r,c):
    weaving = []
    width = len(p.treadle)*len(p.treadle[0])

    for harness in p.harness:
        weft = [clr.blu+'+']*width
        for treadle in harness:
            for warp in p.treadle[treadle]:
                weft[warp] = clr.fal+'-'
        weaving.append(weft)

    for row in range(0,len(p.repeat)*r):
        weave = ""
        for col in range(0,width*c):
            the_weft = p.repeat[(row)%len(p.repeat)]
            the_warp = col%len(weaving[the_weft])
            weave += weaving[the_weft][the_warp]
        print(weave)

if __name__ == '__main__':
    import patterns
    import sys
    class clr:
        hed = '\033[95m'
        blu = '\033[94m'
        grn = '\033[92m'
        wrn = '\033[93m'
        fal = '\033[91m'
        end = '\033[0m'

        def disable(self):
            self.hed = ''
            self.blu = ''
            self.grn = ''
            self.wrn = ''
            self.fal = ''
            self.end = ''

    #  p = getattr(patterns,sys.argv[1])
    #  printPattern(p,int(sys.argv[2]),int(sys.argv[3]))

    # p4, p7, p8, p11, p12 are cool
    printPattern(patterns.p12,3,4)
