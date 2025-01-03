"""
    Graphing of linear algebra, exercise 2.2
"""
import numpy as np
import matplotlib.pyplot as plt
#change to the directory of the script
import os
#import a module to convert png files to pdf
from PIL import Image

def plot_addition_two(u, v, title, start=(0, 0), exportfile = "temp.png"):
    """
        Plot the addition of two vectors
    """
    #plot the zero point first 
    plt.plot(0, 0, 'ko')
    plt.title(title)
    plt.quiver(start[0], start[1], u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r')
    plt.text(u[0]/2, u[1]/2, "u", color='r')
    plt.quiver(u[0], u[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b')
    plt.text(v[0]/2 + u[0], v[1]/2 + u[1], "v", color='b')
    plt.quiver(start[0], start[1], u[0] + v[0], u[1] + v[1], angles='xy', scale_units='xy', scale=1, color='g')
    plt.text(u[0]/2 + v[0], u[1]/2 + v[1], "u + v", color='g')  
    plt.xlim(min(start[0], start[0] + u[0], start[0] + u[0] + v[0], 0) - 1, max(start[0], start[0] + u[0], start[0] + u[0] + v[0], 0) + 1)
    plt.ylim(min(start[1], start[1] + u[1], start[1] + u[1] + v[1], 0) - 1, max(start[1], start[1] + u[1], start[1] + u[1] + v[1], 0) + 1)
    #add decription of three vectors and colored lines
    plt.grid()
    plt.savefig(exportfile)
    #clear the plot
    plt.clf()

def plot_addition_three (u, v, w, title, start=(0, 0), exportfile = "temp.png"):
    """
        Plot the addition of three vectors
    """
    #plot the zero point first 
    plt.plot(0, 0, 'ko')
    plt.title(title)
    plt.quiver(start[0], start[1], u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r')
    plt.text(u[0]/2, u[1]/2, "u", color='r')
    plt.quiver(u[0], u[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b')
    plt.text(v[0]/2 + u[0], v[1]/2 + u[1], "v", color='b')
    plt.quiver(u[0] + v[0], u[1] + v[1], w[0], w[1], angles='xy', scale_units='xy', scale=1, color='y')
    plt.text(w[0]/2 + u[0] + v[0], w[1]/2 + u[1] + v[1], "w", color='y')
    plt.quiver(start[0], start[1], u[0] + v[0] + w[0], u[1] + v[1] + w[1], angles='xy', scale_units='xy', scale=1, color='g')
    plt.text(u[0] + v[0]/2 + w[0], u[1] + v[1]/2 + w[1], "u + v + w", color='g')
    plt.xlim(min(start[0], start[0] + u[0], start[0] + u[0] + v[0], start[0] + u[0] + v[0] + w[0], 0) - 1, max(start[0], start[0] + u[0], start[0] + u[0] + v[0], start[0] + u[0] + v[0] + w[0], 0) + 1)
    plt.ylim(min(start[1], start[1] + u[1], start[1] + u[1] + v[1], start[1] + u[1] + v[1] + w[1], 0) - 1, max(start[1], start[1] + u[1], start[1] + u[1] + v[1], start[1] + u[1] + v[1] + w[1], 0) + 1)    
    plt.grid()
    plt.savefig(exportfile)
    #clear the plot
    plt.clf()


os.chdir(os.path.dirname(__file__))
#plot the addition of (0,1) + (1,0)
#use identical scale for both axes
#list of vector 1 
list_of_vectors1 = [(0,1), (6,-2), (2,1), (2,3), (2,3), (1,1), (4,2),
                    (-3, -5), (-5, -2)]
#list of vector 2
list_of_vectors2 = [(1,0), (2,-6), (1,2), (2,3), (-2,-3), (1,-1), (1,0),
                    (7, 3), (7, 5)]
list_of_exportfiles = ["vector_addition_2_5a.png", "vector_addition_2_5b.png", "vector_addition_2_5c.png", "vector_addition_2_5d.png", "vector_addition_2_5e.png",  "vector_addition_2_5f.png", "vector_addition_2_5g.png", "vector_addition_2_5h.png", "vector_addition_2_5i.png"]
list_of_titles = ["exercise 2.5 a", "exercise 2.5 b", "exercise 2.5 c", "exercise 2.5 d", "exercise 2.5 e", "exercise 2.5 f", "exercise 2.5 g", "exercise 2.5 h", "exercise 2.5 i"]

list_of_three_vectors1 = [(1,2), (-2, -5), (0,1)]
list_of_three_vectors2 = [(1,3), (7, 6), (-3,-3)]
list_of_three_vectors3 = [(-3,2), (0,-4), (1,2)]
list_of_titles_three = ["exercise 2.5 j", "exercise 2.5 k", "exercise 2.5 l"]
list_of_exportfiles_three = ["vector_addition_2_5j.png", "vector_addition_2_5k.png", "vector_addition_2_5l.png"]

#plot all vectors
for i in range(len(list_of_vectors1)):
    plot_addition_two(list_of_vectors1[i], list_of_vectors2[i], list_of_titles[i], (0,0), list_of_exportfiles[i])
for i in range(len(list_of_three_vectors1)):
    plot_addition_three(list_of_three_vectors1[i], list_of_three_vectors2[i], list_of_three_vectors3[i], list_of_titles_three[i], (0,0), list_of_exportfiles_three[i])

list_of_exportfiles += list_of_exportfiles_three
#convert all png files to pdf
images = [Image.open(x) for x in list_of_exportfiles]
images[0].save("exercise_2_5.pdf", save_all=True, append_images=images[1:])
#remove all png files
for file in list_of_exportfiles:
    os.remove(file)
print("exercise_2_5.pdf is created")