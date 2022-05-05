import sys, os, glob
from PIL import Image


path = 'C:\\Users\\drale\\Documents\\GitHub\\test-website\\assets\\img\\posts'
sizes = {
    "lg" : (1920, 1080),
    "md" : (991, 557),
    "sm" : (767, 431),
    "xs" : (575, 323),
    "placehold" : (230, 129),
    "thumb" : (535, 301),
    "thumb@2x" : (1070, 602),
}
for file in glob.glob(path + '\\*.jpg'):
    # get filename and path of each file
    filename = os.path.basename(file)
    filepath = os.path.dirname(file)
    size_name = filename.split("_")

    if len(size_name) >= 2:
        if size_name[-1].split(".")[0] in sizes.keys():
            print("File {} already exists".format(filename))
            continue
#   # for each size in sizes, append the size name to the filename and check if the file exists
#   # if it does, resize the image and save it
    for size in sizes.keys():
        # check if the file at given size exists
        new_file_name = filename.replace('.jpg', '_' + size + '.jpg')

        if not os.path.isfile(filepath + '\\' + new_file_name):
            new_file_name = filename.replace('.jpg', '_' + size + '.jpg')
            im = Image.open(file)
            im.thumbnail(sizes[size])
            im.save(new_file_name)
            print ("file {} created".format(new_file_name))



