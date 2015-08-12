import yt
import numpy as np

ds = yt.load("/zang/msoares/JLopez/50_hdf5_plt_cnt_0100")
ad = ds.all_data()


mi, ma = ad.quantities.extrema("density")

#Set up transfer function
tf = yt.ColorTransferFunction((-29, -24))
tf.add_layers(6, w=0.05, colormap = "Hue Sat Value 2")

v, max_c = ds.find_max('density')

#Initialize the Camera
cam = ds.camera([0.5, 0.5, 0.5], [1.0, 1.0, 1.0], (.5, 'pc'), 512, tf, fields = ["density"])
frame = 0

#Zoom in by a fact of 2.5  over 80 frames
for i, snapshot in enumerate(cam.zoomin(2.5, 80, clip_ratio = 8.0)):
    snapshot.write_png('camera_movement_%04i.png'%frame)
    frame += 1
