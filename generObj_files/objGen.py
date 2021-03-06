#Inline comments coming soon
import yt

ds = yt.load("/zang/msoares/JLopez/50_hdf5_plt_cnt_1200")
rho = [2e-27, 1e-27]
trans = [1.0, 0.5]

filename = '/home/jlopez46/creating_objFiles/try4/surfaces'

sphere = ds.sphere("max", (0.5, "pc"))
for i, r in enumerate(rho):
    surf = ds.surface(sphere, 'density', r)
    surf.export_obj(filename, transparency = trans[i], color_field = 'temperature', plot_index = i)
