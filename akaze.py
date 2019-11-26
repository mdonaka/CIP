import cv2
import pickle


class Akaze:

    def __init__(self, file, out="all", dir="./fig"):
        self.dir = dir
        self.out = out
        self.file = file
        self.kp = self.calcKp()

    def calcKp(self):
        img = cv2.imread(f"{self.dir}/{self.file}.png")
        akaze = cv2.AKAZE_create(threshold=0.0)
        kp = akaze.detect(img)
        img_akaze = cv2.drawKeypoints(img, kp, None, flags=4)
        cv2.imwrite(f"{self.dir}/bef/{self.file}_{self.out}.png", img)
        cv2.imwrite(f"{self.dir}/kp/{self.file}_kp_{self.out}.png", img_akaze)
        lst = []
        for p in kp:
            lst.append([p.pt[0], p.pt[1], p.size])
        return lst

    def output(self):
        with open(f"{self.dir}/points/{self.file}_{self.out}.csv", "w") as f:
            for p in self.kp:
                f.write(f"{p[0]},{p[1]},{p[2]}\n")
