from src.Graph.Network import AboutNetwork

G = AboutNetwork([
        'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/CRKP.shp',
        'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_G.shp',
    ], 'E:/expressway project/Data/Host file/')

G_Point,G_Road,G_Simplify,G_Plus = G(combined_network = True, draw_composite = True, save_point = True,save_road = True,save_simplify_road = True,save_composite = True)
