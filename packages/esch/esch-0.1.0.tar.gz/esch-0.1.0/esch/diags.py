# diags.py
#   esch diagrams
# by: Noah Syrkis

# imports
import numpy as np
import tikz


# functions
def box_fn(x, y, w, h, text):
    return tikz.node(x, y, w, h, text)


# main
def main():
    coords = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    pic = tikz.Picture()
    pic.draw(poly=coords, color="red")
    # save to png and pdf
    pic.write_image("test.pdf")


if __name__ == "__main__":
    main()
