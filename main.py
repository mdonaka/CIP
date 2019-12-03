from akaze import Akaze

if __name__ == "__main__":
    fileList = ["c++", "python", "rust"]

    # random
    for file in fileList:
        c = Akaze(file=file, out="random")
        c.kp = c.random()
        c.run()
        c.output()

    # sort
    for file in fileList:
        c = Akaze(file=file, out="sort")
        c.kp = c.sortting()
        c.run()
        c.output()

    # sort and random
    for file in fileList:
        c = Akaze(file=file, out="sort+random")
        c.kp = c.sorttingAndRandom()
        c.run()
        c.output()

    # cov
    for file in fileList:
        c = Akaze(file=file, out="cov")
        c.kp = c.cov()
        c.run()
        c.output()

    # sort and random
    for file in fileList:
        c = Akaze(file=file, out="sort+cov")
        c.kp = c.sorttingAndCov()
        c.run()
        c.output()

    # long
    for file in fileList:
        c = Akaze(file=file, out="long")
        c.kp = c.long()
        c.run()
        c.output()

    # sort and long
    for file in fileList:
        c = Akaze(file=file, out="sort+long")
        c.kp = c.sorttingAndlong()
        c.run()
        c.output()
