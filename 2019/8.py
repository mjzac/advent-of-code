from collections import Counter
import sys


def get_input():
    with open("8input.txt") as f:
        ip = list(f.readline())
    return ip


IMAGE_HEIGHT = 6
IMAGE_WIDTH = 25
stride = IMAGE_HEIGHT * IMAGE_WIDTH


def run(input):
    zeros_count = sys.maxsize
    min_zero_layer = None
    for idx in range(0, len(input), stride):
        layer = input[idx : idx + stride]
        c = Counter(layer)
        if zeros_count > c.get("0", 0):
            zeros_count = c.get("0", 0)
            min_zero_layer = layer
    return min_zero_layer.count("1") * min_zero_layer.count("2")


def run2(input):
    image = ["2"] * stride  # transparent layer as base
    # Construct visible layer by stacking up layers in reverse order
    for idx in reversed(range(0, len(input), stride)):
        layer = input[idx : idx + stride]
        for idx, pixel in enumerate(layer):
            if pixel != "2":
                image[idx] = pixel
    return "".join(image)


def format(message):
    message = message.replace("0", " ")
    message = message.replace("1", "#")
    message_list = list(message)
    for idx in range(0, len(message_list), IMAGE_WIDTH):
        print("".join(message_list[idx : idx + IMAGE_WIDTH]))


if __name__ == "__main__":
    print(run(get_input()))
    print(format(run2(get_input())))
