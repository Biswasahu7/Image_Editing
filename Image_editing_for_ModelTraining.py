import os
import glob

# *********************************************
# Change inside txt file for model training
# *********************************************

# import glob
# print("Process Start.....!")
# #
# # # Give the txt file fully path
# files=glob.glob("/media/root1/data/01_Images/Shell2/00_Shell_2_Front_Images/00_Raw_Images/26th_Aug/Bucket_Hook/Shell2_BH4/markedhook_Shell2_BH4/*.txt")
#
# # # EDITING txt FILES
# for file in files:
#
#     # lets read all file contents - imp
#     f=open(file)
#     content=f.read()
#     # print(content)
#     x = content[:1]
#     # print(x)
#     b = str(1)
#     content = (content.replace(x,b))
#     # print(content[0])- imp
#
#     # #  What need to change from txt file we need to edit here
#     content = content.replace('16 ', '7 ')
#
#     f.close()
#
#     # write new content into txt file - imp
#     f=open(file,"w")
#     # print(content)
#     f.write(content)
#     f.close()
#
# print("Text file has been changed ...!")


# **********************************
# Checking any value in txt file
# **********************************

# import glob
# print("Text verification is start...!")
#
# # Give the txt file fully path
# files = glob.glob("/media/root1/data/01_Images/Shell2/00_Shell_2_Front_Images/Model_Train_1/*.txt")
# # a = 0
# count = 0
#
# # EDITING txt FILES
# for file in files:
#     # lets read all file contents
#     f = open(file)
#     content = f.read()
#     digit = content[:2]
#     # print(digit)
#
# # Check if 15 is there in txt file or not.
#     if str('18') in str(digit):
#         count += 1
#         print(content)
#         print(f)
#         # print("y")
#     # else:
#     #     print("No")
# print("Text verification is done...{}".format(count))


# ******************************************************
# Change jpg file name & number according to your required
# ******************************************************
#
# import cv2
# import glob
#
# count = 0
# print("Image rename Start...! count starts-{}".format(count))
#
# # Give image folder path where you want to Rename images are available.
# # files=glob.glob("/home/vert/Documents/Code/i*.jpg")
# files=glob.glob("/home/vert/JSW_Project/01_WAGON_NUMBER_TRACKING_Vallari/Images_Videos/Cam_1_INFO/Images/Code_Images/Need Train/*.jpg")
# print("reading image")
#
# # This code will run one by one images from folder and making pari system ex:  1 imagename, 2 imagename
# for i,f in (enumerate(files)):
#
#     # Image Reading from folder
#     img=cv2.imread(f)
#
#     # Give new folder path where you want to save your rename images.
#     cv2.imwrite("/home/vert/Documents/Rename/img_{}.jpg".format(i+13428),img)
#     count += 1
#
# print("Image rename Done...! count-{}".format(count))


# # ***************************
# # Image and txt File count
# # ***************************

# Folder Path where jpg and txt files are there.
APP_FOLDER = ("/media/root1/data/01_Images/Shell4/01_Shell_4_Frontview_Images/02_Model_Train_7")

txtfileCounter = 0
jpgfileCount = 0

# Running for loop inside the folder to take txt and jpg file
for root, dirs, files in os.walk(APP_FOLDER):
    for file in files:

        # Checking txt file
        if file.endswith('.txt'):
            txtfileCounter += 1
        else:
            jpgfileCount += 1

print('Total number jpg of files',jpgfileCount)
print('Total number txt of files',txtfileCounter)

# ***************************************
# Rename any file name inside the folder
# ***************************************
#
# from os import rename, listdir
# print('Start Rename Process...!')
# #
# path = os.chdir("/media/root1/data/01_Images/Shell4/01_Shell_4_Frontview_Images/00_Raw_Images/27th_Aug_Image/person/Marked Person_shell4_Person1")
#
# badprefix = "image"
#
# for fname in os.listdir(path):
#
#     # print(fname)
#     if fname.startswith(badprefix):
#         rename(fname,fname.replace(badprefix,'image4'))
#
# print('File Rename Done...!')

# **********************************************
# Delete file from folder according to your wise
# **********************************************

# import os
# deletec = 0
#
# print("Start Delete process...!")
#
# # Give file path where u want to delete something
# dir_name = "/home/root1/CVML_2/Images/Marked_Images/05_Top lance"
# test = os.listdir(dir_name)
#
# for item in test:
#     # provide file extension to delete
#     if item.endswith(".txt"):
#         os.remove(os.path.join(dir_name, item))
#         deletec += 1
#
# print("File has been deleted...{}".format(deletec))
# *******************************************************************************

# ********************
# Delete jpg vile
# ********************
# import os
# from os import listdir
# # import listdir, remove
# labels = os.listdir("/media/root1/data/01_Images/Shell4/01_Shell_4_Frontview_Images/00_Raw_Images/27th_Aug_Image/person/Marked Person_shell4_Person1")
# images = os.listdir("/media/root1/data/01_Images/Shell4/01_Shell_4_Frontview_Images/00_Raw_Images/27th_Aug_Image/person/Marked Person_shell4_Person1")
# for image in images:
#     if '{}.{}'.format(image.split('.')[0],'txt') not in labels:
#         print('Going to remove %s' % image )
#         os.remove('/media/root1/data/01_Images/Shell4/01_Shell_4_Frontview_Images/00_Raw_Images/27th_Aug_Image/person/Marked Person_shell4_Person1/%s' % image)