import cv2
import pickle
import random


class Akaze:

    def __init__(self, file, out="all", dir="./fig"):
        self.dir = dir
        self.out = out
        self.file = file
        self.img = cv2.imread(f"{self.dir}/{self.file}.png")
        self.kp = self.__calcKp()
        cv2.imwrite(f"{self.dir}/bef/{self.file}_{self.out}.png", self.img)

    def __calcKp(self):
        akaze = cv2.AKAZE_create(threshold=0.0)
        return akaze.detect(self.img)

    def run(self):
        img_akaze = cv2.drawKeypoints(self.img, self.kp, None, flags=4)
        cv2.imwrite(f"{self.dir}/kp/{self.file}_kp_{self.out}.png", img_akaze)

    def output(self):
        with open(f"{self.dir}/points/{self.file}_{self.out}.csv", "w") as f:
            for p in self.kp:
                f.write(f"{p.pt[0]},{p.pt[1]},{p.size}\n")

    ######### select kp ##########
    def random(self, k=50, kp=None):
        if kp ==None:
            kp = self.kp
        if len(kp) < k:
            return
        return random.sample(kp, k=50)

    def sortting(self, k=50, kp=None):
        if kp ==None:
            kp = self.kp
        if len(kp) < k:
            return
        return self.kp[-50:]


    def sorttingAndRandom(self, k=50, kp=None):
        if kp ==None:
            kp = self.kp
        if len(kp) < k:
            return
        tmp = self.sortting(k=min(len(kp),4*k))
        return self.random(kp=tmp)
