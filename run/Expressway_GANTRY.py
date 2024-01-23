


from Expressway.Graph.Network import AboutNetwork


path_road = 'E:/expressway project/Data/.sichuan/Graph/road/'
path_place = 'E:/expressway project/Data/.sichuan/Graph/place/'
Host_file_path = 'E:/expressway project/Data/Host file/'


# build_road_networkx = AboutNetwork( file_path = [path + 'Road_G.shp' ,path + 'Road_S.shp',path + 'Road_X.shp' ,path + 'GYJGP.shp'], Host_file_path = Host_file_path, Expressway = True)
build_road_networkx = AboutNetwork( file_path = [
                                                 path_place + 'GANTRY.shp',
                                                 path_road + 'Road_C.shp',
                                                 path_road + 'Road_G.shp',
                                                 path_road + 'Road_S.shp',
                                                 path_road + 'Road_W.shp',
                                                 path_road + 'Road_X.shp',
                                                 path_road + 'Road_Y.shp',
                                                 ], Host_file_path = Host_file_path, Expressway = True)


G_Point,G_Road,G_Simplify,G_Plus = build_road_networkx(combined_network = True, draw = True, save=True)