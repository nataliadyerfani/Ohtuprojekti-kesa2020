import argparse
import camera_node
import object_detection_node
from matplotlib import pyplot as plt
import cv2
from typing import List

DEFAULT_VIDEO_ID = 0
DEFAULT_MODEL = 'detect.tflite'
DEFAULT_LABELS = 'labelmap.txt'


def main():
    camera = camera_node.Camera(int(args.camera_id))
    detect_node = object_detection_node.ObjectDetectionNode(
        args.model_file, args.label_file)
    labels = detect_node.get_labels()
    while True:
        frame = camera.frameRGB()
        display_image(frame)
        results = detect_node.detect_objects_in_frame(frame)
        print_detected_classes(results, labels)
        #print_if_over(results, labels, 0.7)


def display_image(frame):
    cv2.imshow('frame', frame)
    cv2.waitKey(1)


def print_if_over(results: List, labels: List[str], x: float):
    """
    Print out an object when it is detected with over x% probability, 
    with values of x between 0 and 1.
    """
    for i in range(10):
        if results[2][0][i] > x:
            print(
                f'{labels[results[1][0][i].astype(int)]:15} {results[2][0][i]}'
            )
        else:
            break


def print_detected_classes(results: List, labels: List[str]):
    """
    Print out all 10 possible detected objects and their probabilities.
    """
    print(chr(27) + "[2J")
    print("Classes and scores:")
    print("")
    for i in range(10):
        print(f'{labels[results[1][0][i].astype(int)]:15} {results[2][0][i]}')


if __name__ == '__main__':
    """
    Take possible command line arguments for camera id, model file etc.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',
                        '--model_file',
                        default=DEFAULT_MODEL,
                        help='.tflite model to be executed')
    parser.add_argument('-l',
                        '--label_file',
                        default=DEFAULT_LABELS,
                        help='name of file containing labels')
    parser.add_argument('--input_mean',
                        default=127.5,
                        type=float,
                        help='input_mean')
    parser.add_argument('--input_std',
                        default=127.5,
                        type=float,
                        help='input standard deviation')
    parser.add_argument('-c',
                        '--camera_id',
                        default=DEFAULT_VIDEO_ID,
                        help='number of the a webcamera')

    args = parser.parse_args()

    main()
