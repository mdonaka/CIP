import cv2
import pickle
import random
import numpy as np


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
    def random(self, k=30, kp=None):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        return random.sample(kp, k=30)

    def sortting(self, k=30, kp=None, rev=False):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        return kp[-50:] if not rev else kp[:50]

    def sorttingAndRandom(self, k=30, kp=None):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        tmp = self.sortting(k=min(len(kp), 4*k))
        return self.random(kp=tmp)

    def cov(self, k=30, kp=None, rev=True):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        mx = 0 if rev else 1e30
        now = self.random()
        for _ in range(1000):
            tmp = self.random(kp=kp)
            data = [[p.pt[0], p.pt[1]] for p in tmp]
            mcov = np.cov(data, rowvar=0)
            val = mcov[0][0]*mcov[1][1]
            if (rev and val > mx) or (not rev and val < mx):
                now = tmp
                mx = val
        return now

    def sorttingAndCov(self, k=30, kp=None):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        tmp = self.sortting(k=min(len(kp), 4*k))
        return self.cov(kp=tmp)

    def long(self, k=30, kp=None):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        mx = 0 
        now = self.random()
        for _ in range(5):
            tmp = self.random(kp=kp)
            data = [np.array([p.pt[0], p.pt[1]]) for p in tmp]
            sum = 0
            for i in range(len(data)):
                mnN = 1e20
                for j in range(len(data)):
                    if i==j:
                        continue
                    norm = np.linalg.norm(data[i]-data[j])
                    if norm < mnN:
                        mnN = norm
                sum += mnN
            if sum > mx:
                now = tmp
                mx = sum
        return now


    def sorttingAndlong(self, k=30, kp=None):
        if kp == None:
            kp = self.kp
        if len(kp) < k:
            return
        tmp = self.sortting(k=min(len(kp), 4*k))
        return self.long(kp=tmp)
