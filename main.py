from akaze import Akaze

if __name__ == "__main__":
    fileList = ["c++","python","rust"]

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

    # reverse
    for file in fileList:
        c = Akaze(file=file, out="revease")
        c.kp = c.sortting(rev=True)
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

    # cov rev
    for file in fileList:
        c = Akaze(file=file, out="cov_rev")
        c.kp = c.cov(rev=True)
        c.run()
        c.output()
