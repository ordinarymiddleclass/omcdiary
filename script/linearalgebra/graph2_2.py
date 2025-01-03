"""
    Graphing of linear algebra, exercise 2.2
"""
import numpy as np
import matplotlib.pyplot as plt
#change to the directory of the script
import os
#import a module to convert png files to pdf
from PIL import Image

def plot_vector(v, title, start=(0, 0), exportfile = "temp.png"):
    """
        Plot a vector
    """
    plt.title(title)
    plt.quiver(start[0], start[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.savefig(exportfile)

os.chdir(os.path.dirname(__file__))
list_of_vectors = [(1, 2), (2, 1), (3, 3), (1, 3), (3, 1)]
list_of_start = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
list_of_titles = ["exercise 2.2a", "exercise 2.2b", "exercise 2.2c", "exercise 2.2d", "exercise 2.2e"]
list_of_exportfiles = ["exercise_2_2a.png", "exercise_2_2b.png", "exercise_2_2c.png", "exercise_2_2d.png", "exercise_2_2e.png"]
#plot all vectors
for i in range(5):
    plot_vector(list_of_vectors[i], list_of_titles[i], list_of_start[i], list_of_exportfiles[i])
    plt.show()

#convert all png files to pdf
images = [Image.open(x) for x in list_of_exportfiles]
images[0].save("exercise_2_2.pdf", save_all=True, append_images=images[1:])
#remove all png files
for file in list_of_exportfiles:
    os.remove(file)
print("exercise_2_2.pdf is created")

