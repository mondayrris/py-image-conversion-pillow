# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from PIL import Image


def convert_grey_black_write(name: str, output_ext: str):
    # read the image from path
    image = Image.open(f"./source/{name}")

    # Convert it into the grayscale image
    grayscale = image.convert('L')

    # Converting the same image to black and white mode
    # disable dithering, which is basically noise
    bwscale = image.convert('1', dither=Image.NONE)

    # Split String and Remove Last Element
    # https://blog.finxter.com/python-split-string-and-remove-last-element/
    filename = name.rsplit('.', 1)[0]

    # save both the images
    grayscale.save(f"./output/{filename}-grey.{output_ext}")
    bwscale.save(f"./output/{filename}-bw.{output_ext}")


def rotate_image(name: str, x1: int, y1: int, x2: int, y2: int, rotation: float):
    img = Image.open(f"./source/{name}")

    # Specify image filling color when rotating in python with PIL and setting expand argument to true
    # https://stackoverflow.com/a/61586840/18131146
    # white = (255, 255, 255)

    # TypeError: color must be int or single-element tuple
    # https://github.com/python-pillow/Pillow/issues/5892#issuecomment-995648400
    white = 255

    # Rotating image in python: extrapolate background color
    # https://stackoverflow.com/a/52163385/18131146
    sub_image = img.crop(box=(x1, y1, x2, y2)).rotate(angle=rotation, fillcolor=white)
    img.paste(sub_image, box=(x1, y1))

    filename = name.rsplit('.', 1)[0]
    fileext = name.rsplit('.', 1)[-1]
    img.save(f"./output/{filename}-rotated.{fileext}")


def convert_image_to_pdf(name: str):
    """
    Convert Images to PDF using Python
    https://datatofish.com/images-to-pdf-python/
    :param name:
    """
    image_1 = Image.open(f"./source/{name}")
    im_1 = image_1.convert('RGB')

    filename = name.rsplit('.', 1)[0]
    im_1.save(f"./output/{filename}.pdf")


def convert_images_to_pdf(output_name: str, source_dirname: str):
    """
    Convert Images to PDF using Python
    https://stackoverflow.com/a/74950182/18131146

    https://stackoverflow.com/a/47283224/18131146
    :param output_name:
    :param source_dirname:
    """
    import os

    images = []
    for filename in os.listdir(f"./source/{source_dirname}"):
        if not filename.endswith(".jpg") and not filename.endswith(".png"):
            continue
        path = os.path.join(source_dirname, filename)
        if os.path.isdir(path):
            continue

        image = Image.open(f"./source/{source_dirname}/{filename}").convert('RGB')
        images.append(image)

    images[0].save(
        f"./output/{output_name}", "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # grey black image
    # convert_grey_black_write('21042023162121-0001.jpg', 'jpg')

    # image size:                   1654x2340
    # image mis-rotated portion:    672(adjacent) x 14(opposite)
    # from math import degrees, atan
    #
    # rotate_image('18042023145020-0001-grey.jpg', 0, 0, 1654, round(2340/2), -degrees(atan(14/672)))

    # image to pdf
    # convert_image_to_pdf('21042023162121-0001-grey.jpg')
    convert_images_to_pdf('21042023162122-0001-grey.pdf', 'application-form-images')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
