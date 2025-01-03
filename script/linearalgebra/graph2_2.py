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
    #plot the zero point first 
    plt.plot(0, 0, 'ko')
    plt.title(title)
    plt.quiver(start[0], start[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.savefig(exportfile)

os.chdir(os.path.dirname(__file__))
list_of_vectors = [(2,2), (6,12), (-1,0), (np.pi, np.e), (1,2), 
                   (1,2), (1,2), (-1,-2), (-3,0), (-4,-2), (8,4),
                   (-8,-4)]
list_of_start = [(0,0), (1,-2), (4,1), (0,0), (0,0),
                 (-3,0), (2,4), (0,0), (1,0), (0,3/2), (1,1),
                 (8,4)] 

list_of_titles = ["exercise 2.2 a", "exercise 2.2 b", "exercise 2.2 c", "exercise 2.2 d", "exercise 2.2 e",
                    "exercise 2.2 f", "exercise 2.2 g", "exercise 2.2 h", "exercise 2.2 i", "exercise 2.2 j", "exercise 2.2 k", "exercise 2.2 l"]
list_of_exportfiles = ["vector_a.png", "vector_b.png", "vector_c.png", "vector_d.png", "vector_e.png",
                       "vector_f.png", "vector_g.png", "vector_h.png", "vector_i.png", "vector_j.png", "vector_k.png",
                       "vector_l.png"]
#plot all vectors
for i in range(len(list_of_vectors)):
    plot_vector(list_of_vectors[i], list_of_titles[i], list_of_start[i], list_of_exportfiles[i])
    plt.show()

#convert all png files to pdf
images = [Image.open(x) for x in list_of_exportfiles]
images[0].save("exercise_2_2.pdf", save_all=True, append_images=images[1:])
#remove all png files
for file in list_of_exportfiles:
    os.remove(file)
print("exercise_2_2.pdf is created")

