from akaze import Akaze

if __name__ == "__main__":
    fileList = ["c++","python","rust"]

    for file in fileList:
        c = Akaze(file=file, out="random")
        c.random()
        c.run()
        c.output()
