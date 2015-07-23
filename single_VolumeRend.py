import yt

#This is an example of where I get my data from
#You will have to substitute this to the filepath in which you
#have your data stored
ds = yt.load("/zang/msoares/JLopez/50_hdf5_plt_cnt_0900")


tf = yt.ColorTransferFunction((-29, -24)) #Read documentation on this function if your rendered images look a bit funky
tf.add_layers(8, w=0.05, colormap="Hue Sat Value 2") #You can mess with this to see how other colormaps work with your data
cam = ds.camera([0.5, 0.5, 0.5], [1.0, 1.0, 1.0], (.5, 'pc'), 512, tf, fields=["density"])
#cam.show() #You can uncomment this if you are using ipython notebooks and it will display image on your screen
cam.snapshot("%s_volume_rendered.png" % ds, clip_ratio=4.0) #outputs to same directory as python script
