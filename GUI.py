# import libraries
import Tkinter as tk
import os
import PIL.Image
import PIL.ImageTk

# this is the pathname to the folder containing all these images
# may need to change based on how we are traversing through the images
pathname = '/Users/rubabmalik786/Downloads/gui_images_initial_testing'
image_pair_dictionary = {}


# def findImage(self, pathname):
#     for image in os.listdir(pathname):
#         # for original images
#         if image[-12:] == 'maxP_fig.png':
#             # image_id is the 32 characters in its UUID
#             image_id = image[2:34]
#             print 'the image_id is', image_id
#
#             # need pathname for segmented version of the image to show it in a panel side by side
#             segmented_name_starts_with = image[0:2] + image_id + '_fig.png'
#             print "segmented starts with", segmented_name_starts_with
#
#             image_pair_dictionary[pathname + '/' + image] = pathname + '/' + segmented_name_starts_with
#             #     might need to add the image_id to the dictionary as well
#     print image_pair_dictionary
#     print
#     return image_pair_dictionary

class CellSegmentationGUI():

    # initialize class
    def __init__(self, master):
        self.image_pair_dictionary = {}
        root.title("Cell Segmenting")
        # self.master = master

        frame = tk.Frame(master)

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
        for orig, seg in image_pair_dictionary.iteritems():
            print 'starting for loop through dictionary'
            print orig
            print seg
            print

            # for the original image on the left
            # self.original_image_path = orig
            # self.segmented_image_path = seg
            self.original_image = PIL.Image.open(orig)
            self.render_original = PIL.ImageTk.PhotoImage(self.original_image)
            self.left_panel_original = tk.Label(frame, image=self.render_original)
            self.left_panel_original.pack(side='left')

            # for the segmented image on the right
            self.segmented_image = PIL.Image.open(seg)
            self.render_segmented = PIL.ImageTk.PhotoImage(self.segmented_image)
            self.right_panel_segmented = tk.Label(frame, image=self.render_segmented)
            self.right_panel_segmented.pack(side='right')
            pixels = list(self.segmented_image.getdata())
            # print pixels
            self.right_panel_segmented.bind('<Button-1>', self.click_event)


        # frame = tk.Frame(master)
        # frame.pack()
        #
        # self.printButton = tk.Button(frame, text = 'Begin', command = self.printMessage, width = 50, height = 50)
        # self.printButton.pack(side = 'left')
        #
        # self.quitButton = tk.Button(frame, text = 'Quit', command = frame.quit, width = 50, height = 50)
        # self.quitButton.pack(side = 'right')




        # itertae through the dictionary and display the images


    def click_event(self, event):
        global position
        print("clicked on image at")
        print (event.x, event.y)
        #   TODO: raise excpetion when click is outside the image region, prompt user to click again w/in image region
        position = (event.x, event.y)

    #     #         TODO: remove comments and make blocks to add readibility


    # def findImages(self, pathname):
    #     for image in os.listdir(pathname):
    #         # for original images
    #         if image[-12:] == 'maxP_fig.png':
    #             # image_id is the 32 characters in its UUID
    #             image_id = image[2:34]
    #             print 'the image_id is', image_id
    #
    #             # need pathname for segmented version of the image to show it in a panel side by side
    #             segmented_name_starts_with = image[0:2] + image_id + '_fig.png'
    #             print "segmented starts with", segmented_name_starts_with
    #
    #             image_pair_dictionary[pathname + '/' + image] = pathname + '/' + segmented_name_starts_with
    #             #     might need to add the image_id to the dictionary as well
    #     print image_pair_dictionary
    #     print
    #     return image_pair_dictionary




if __name__ == "__main__":
    root = tk.Tk()
    CellSegmentationGUI(root)
    root.mainloop()