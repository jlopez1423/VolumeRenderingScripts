#not all these modules are needed
#they are just there for my personal
#experimenting

import numpy as np
import matplotlib.pyplot as plt
import yt
import glob

fpath = '/zang/msoares/JLopez/'
ffiles= '50_hdf5_plt_cnt_[0-9][0-9][0][0]'

num_procs=20

# get the files to loop through
my_filenames = glob.glob(fpath+ffiles)
my_filenames.sort()

for f in yt.parallel_objects(my_filenames,num_procs):
    print f
    pf=yt.load(f)
    tf=yt.ColorTransferFunction((-29,-24))
    tf.add_layers(8,w=0.05, colormap="Hue Sat Value 2")
    cam = pf.camera([0.5, 0.5, 0.5], [1.0, 1.0, 1.0], (.5, 'pc'), 512, tf, fields=["d\
ensity"])
    frame = 0
    # Do a rotation over 5 frames
    for i, snapshot in enumerate(cam.rotation(np.pi, 5, clip_ratio=8.0)):
        snapshot.write_png('%s_camera_movement_%04i.png' % (pf,frame))
        frame += 1


