from PIL import Image


def merge_for_presentation(im1, im2, im3, im4, im5, im6, im7, im8):
    w = im1.size[0] + im2.size[0] + im3.size[0] + im4.size[0]
    h = im1.size[1] * 2
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    im.paste(im3, (im1.size[0] + im2.size[0], 0))
    im.paste(im4, (im1.size[0] + im2.size[0] + im3.size[0], 0))
    im.paste(im5, (0, im1.size[1]))
    im.paste(im6, (im1.size[0], im1.size[1]))
    im.paste(im7, (im1.size[0] + im2.size[0], im1.size[1]))
    im.paste(im8, (im1.size[0] + im2.size[0] + im3.size[0], im1.size[1]))

    return im


def merge(im1, im2, im3, im4, im5, im6, im7, im8, im9):
    w = im1.size[0] + im2.size[0] + im3.size[0]
    h = im1.size[1] + im4.size[1] + im7.size[1]
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    im.paste(im3, (im1.size[0] + im2.size[0], 0))
    im.paste(im4, (0, im1.size[1]))
    im.paste(im5, (im1.size[0], im1.size[1]))
    im.paste(im6, (im1.size[0] + im2.size[0], im1.size[1]))
    im.paste(im7, (0, im1.size[1] + im4.size[1]))
    im.paste(im8, (im1.size[0], im1.size[1] + im4.size[1]))
    im.paste(im9, (im1.size[0] + im2.size[0], im1.size[1] + im4.size[1]))

    return im

im1 = Image.open("C:/Users/eWX1279627/Downloads/02-3210.jpg")
im2 = Image.open("C:/Users/eWX1279627/Downloads/02-3209.jpg")
im3 = Image.open("C:/Users/eWX1279627/Downloads/02-4061.jpg")
im4 = Image.open("C:/Users/eWX1279627/Downloads/02-3176.jpg")
im5 = Image.open("C:/Users/eWX1279627/Downloads/18-4111.jpg")
im6 = Image.open("C:/Users/eWX1279627/Downloads/13-0358.jpg")
im7 = Image.open("C:/Users/eWX1279627/Downloads/18-3522.jpg")
im8 = Image.open("C:/Users/eWX1279627/Downloads/02-4047.jpg")
im9 = Image.open("C:/Users/eWX1279627/Downloads/02-4054.jpg")

im = merge(im1, im2, im3, im4, im5, im6, im7, im8, im9)
# im.show()

rgb_im = im.convert('RGB')
rgb_im.save(fp="results/for_presentation/merging.jpg")
