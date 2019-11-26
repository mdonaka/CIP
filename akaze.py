import cv2
import pickle


def akaze(file,dir="./fig"):
    img = cv2.imread(f"{dir}/{file}.jpg")
    img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    akaze = cv2.AKAZE_create()
    kp= akaze.detect(img_g)
    img_akaze = cv2.drawKeypoints(img_g, kp, None, flags=4)
    cv2.imwrite(f"{dir}/{file}_g.png", img_g)
    cv2.imwrite(f"{dir}/kp/{file}_kp.png", img_akaze)

    with open(f"{dir}/points/{file}.csv", "w") as f:
        for p in kp:
            f.write(f"{p.pt[0]},{p.pt[1]},{p.size}\n")


if __name__ == '__main__':
    akaze(file="ff")
