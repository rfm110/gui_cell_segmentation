# import libraries
import Tkinter as tk
import os
import PIL.Image
import PIL.ImageTk
import sys
import scipy as Sci
from random import randint

# this is the pathname to the folder containing all these images
# may need to change based on how we are traversing through the images
pathname = '/Users/rubabmalik786/Downloads/gui_images_initial_testing'
# global position
# position = [event.x, event.y]
position_list = []
# x_click = 0
# y_click = 0

root = tk.Tk()
canvas = tk.Canvas(master=root, width = 200, height = 200, bg = 'black')

def tracking_list(position_list):
    def click_event(event):
        canvas = event.widget
        global x_click
        global y_click
        x_click = event.x
        y_click = event.y

        position_list.append((event.x, event.y))

    return click_event()


    print("clicked on image at")
    print (event.x, event.y)
    # root.bind("<Button 1>",)
    #   TODO: raise excpetion when click is outside the image region, prompt user to click again w/in image region




# all as one large  function?
# I am starting off with one main function, and will modularize later
# def traverse_to_find_matching_original_and_segmented_images(pathname):
    # are we asking the user for a specific file or what?
    # for now, I am assuming that all the pictures are in one folder

#     thought process: use  for loop to first iterate through the folder and
#      and find a maxP image(original), then find its matching fig image(segmented)
#     is for loop really a good option for a library this large? if not, what could be my other option for traversal
#     root = tk.Toplevel()


# store original image as key, and segmented image as value
image_pair_dictionary = {}

# traversal through the directory
for image in os.listdir(pathname):

    # for original images
    if image[-12:] == 'maxP_fig.png':


        # image_id is the 32 characters in its UUID
        image_id = image[2:34]
        print 'the image_id is', image_id

        # need pathname for segmented version of the image to show it in a panel side by side
        segmented_name_starts_with = image[0:2] + image_id + '_fig.png'
        print "segmented starts with", segmented_name_starts_with

        image_pair_dictionary[pathname + '/' + image] = pathname + '/' + segmented_name_starts_with
    #     might need to add the image_id to the dictionary as well
print image_pair_dictionary
print

# itertate through the dictionary and display the images
for orig, seg in image_pair_dictionary.iteritems():
    print 'starting for loop through dictionary'
    print orig
    print seg
    print

    # for the original image on the left
    original_image_path = orig
    segmented_image_path = seg
    original_image = PIL.Image.open(original_image_path)
    render_original = PIL.ImageTk.PhotoImage(original_image)
    left_panel_original = tk.Label(root, image = render_original)
    left_panel_original.pack(side = 'left')


    # for the segmented image on the right
    segmented_image = PIL.Image.open(segmented_image_path)
    render_segmented = PIL.ImageTk.PhotoImage(segmented_image)
    right_panel_segmented = tk.Label(root, image=render_segmented)
    right_panel_segmented.pack(side='right')
    pixels = list(segmented_image.getdata())
    mouse_tracking_function = tracking_list(position_list)
    right_panel_segmented.bind('<Button 1>', lambda event: tracking_list(event))
    # print position_list



    # segmented_button = tk.Button(root, image=render_segmented, command=click_event)

    # segmented_button.pack()

    # TODO make sure to add a conditional for when the pixel value is zero when image is clicked



    print 'ending for loop through dictionary'
    print
    print


    root.mainloop()
# traverse_to_find_matching_original_and_segmented_images(pathname)

# allow user to click, bind the click, and store pixel values

def mouse_click_and_bind(click):
    pass