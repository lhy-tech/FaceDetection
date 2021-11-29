import detect_mask_video
import detect_mask_image
import argparse
from detect_mask_video import detect_and_predict_mask
import threading
import time

# # VS
#
# def detect1(ap, whm_list):
#         detect_mask_video.a(ap, whm_list)
#
# def detect2(whm_list):
#     print("detect2 start!!")
#     print("whm_list=", whm_list)
#
#     while(True):
#         print("whm_list =", whm_list)
#         time.sleep(3)
#
# if __name__ == "__main__":
#     whm_list = []
#     thread2 = threading.Thread(target=detect2, args=(whm_list,))
#     thread2.start()
#
# 	# detect_mask_video.a(argparse.ArgumentParser())
#     thread1 = threading.Thread(target=detect1, args=(argparse.ArgumentParser(), whm_list))
#     thread1.start()

# image

def detect1(ap, whm_list):
        detect_mask_image.mask_image(ap, whm_list)


def detect2(whm_list):
    print("detect2 start!!")
    print("whm_list=", whm_list)

    while (True):
        print("whm_list =", whm_list)
        time.sleep(3)


if __name__ == "__main__":
  
    whm_list = []
    thread2 = threading.Thread(target=detect2, args=(whm_list,))
    thread2.start()
    
    # detect_mask_video.a(argparse.ArgumentParser())
    thread1 = threading.Thread(target=detect1, args=(argparse.ArgumentParser(), whm_list))
    thread1.start()