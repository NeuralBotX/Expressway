# -*- coding: utf-8 -*-

"""
File: apps/home.py
Author: Yunheng Wang
Begin Date: 2024/01/25
Description: This file is the main page of the application
"""


# 引入头文件
from PCUI.Head import Head_home


# 引入内部文件源码
from Expressway.Graph.Network import AboutNetwork
from Expressway.Tool.Buffer import SaveLoad


# 引入第三方库
import time
import tkinter as tk
from tkinterdnd2 import TkinterDnD
from tkinter import filedialog
from tkinter import ttk
import os


class HomePage:
    def __init__(self):

        # 初始化
        self.root = TkinterDnD.Tk()

        self.file_path = []
        self.file_path_var = tk.StringVar(value='None')

        self.Host_file_path = None
        self.folder_path_var = tk.StringVar(value='None')

        # 主页面
        self.root = self.home(self.root)

        # 运行主循环
        self.root.mainloop()


    def home(self,root):
        """
        :param root:

        :return:

        % function ->
        """

        # 窗口标题
        root.title("Expressway System")

        # 设置窗口图标
        icon_path = "apps/PCUI/image/logo/logo.ico"  # 替换成你的图标文件路径
        root.iconbitmap(icon_path)

        # 调整窗口大小
        width, height = 800, 600
        root.geometry(f"{width}x{height}")

        # 窗口在屏幕居中
        x,y = Head_home.home_centre_pos(root, width, height)
        root.geometry(f"+{x}+{y}")

        # 设置背景颜色
        canvas = tk.Canvas(root, width=70, height=height, bg="#333333", highlightthickness=0)
        canvas.place(x=0, y=0)
        canvas = tk.Canvas(root, width=200, height=height, bg="#373738", highlightthickness=0)
        canvas.place(x=70, y=0)
        canvas = tk.Canvas(root, width=530, height=height, bg="#1E1E1E", highlightthickness=0)
        canvas.place(x=270, y=0)

        # 创建按钮样式
        button_style = ttk.Style()
        button_style.configure("TButton", padding=(30, 2))

        # ===================== 创建打开文件按钮 =====================
        open_file_button = ttk.Button(root, text="打开数据文件", command=self.choose_file, style="TButton")
        open_file_button.place(x=100, y=50)

        # 显示选中的文件
        file_text = tk.Label(root, text="执行文件:  ", bg="#1E1E1E", fg="#3794FF", font=("Helvetica", 12))
        file_text.place(x=300, y=50)
        file_label = tk.Label(root, textvariable=self.file_path_var, bg="#1E1E1E", fg="#FFFFFF",font=("Helvetica", 12))
        file_label.place(x=370, y=50)
        # ==========================================================

        # ===================== 创建打开文件夹按钮 =====================
        open_folder_button = ttk.Button(root, text="打开文件夹", command=self.choose_folder, style="TButton")
        open_folder_button.place(x=100, y=10)

        # 显示选中的文件
        folder_text = tk.Label(root, text="宿主文件:  ", bg="#1E1E1E", fg="#3794FF", font=("Helvetica", 12))
        folder_text.place(x=300, y=10)
        folder_label = tk.Label(root, textvariable=self.folder_path_var, bg="#1E1E1E", fg="#FFFFFF",font=("Helvetica", 12))
        folder_label.place(x=370, y=10)
        # ==========================================================

        # 创建按钮样式
        run_button_style = ttk.Style()
        run_button_style.configure("Run.TButton", padding=(80, 2))

        # ===================== 创建生成网络按钮 =====================
        run_button = ttk.Button(root, text="生成网络", command=self.run, style="Run.TButton")
        run_button.place(x=400, y=500)
        # ==========================================================

        return root


    def choose_file(self):
        """
        :return:

        % function ->
        """
        file_path = list(filedialog.askopenfilenames(title="选择文件", filetypes=[("All Files", "*.*")]))
        self.file_path.extend(file_path)
        self.file_path_var.set("  ;  ".join([os.path.basename(path) for path in self.file_path]))
        print(self.file_path)


    def choose_folder(self):
        """
        :return:

        % function ->
        """
        folder_path = filedialog.askdirectory() + '/'
        self.Host_file_path = folder_path
        self.folder_path_var.set(folder_path)
        print(self.Host_file_path)


    def run(self):
        """
        :return:

        % function ->
        """
        all_file_name = Head_home.extract_filename(os.listdir(self.Host_file_path))

        name = '_'.join(sorted(Head_home.extract_filename(self.file_path)))

        file_name = [
            'Road_' + name + '_positions',
            'Point_' + name + '_positions',
            'Simplify_road_' + name + '_positions',
            'Composite_' + name + '_positions',
            'Road_' + name + '_graph',
            'Point_' + name + '_graph',
            'Simplify_road_' + name + '_graph',
            'Composite_' + name + '_graph'
        ]

        if name == '':
            error = tk.StringVar(value='The path of file cannot be empty')
            error_label = tk.Label(self.root, textvariable=error, bg="#1E1E1E", fg="red", font=("Helvetica", 8))
            error_label.place(x=440, y=530)
            return


        Generation = tk.StringVar(value='Generation...                      ')
        Generation_label = tk.Label(self.root, textvariable=Generation, bg="#1E1E1E", fg="red", font=("Helvetica", 8))
        Generation_label.place(x=440, y=530)

        if all(var in all_file_name for var in file_name):
            Saveclass= SaveLoad()
            G,pos = Saveclass.load_networkx(load_path = self.Host_file_path , load_name = 'Composite_' + name)

            image_name = str(int(time.time())) + '.png'
            Head_home.cache(G,pos, image_name)

            # 生成图像至界面
            Head_home.show_pic(root=self.root, image_name = image_name)

            # 删除缓存文件
            os.remove(image_name)

            Generation_label.place_forget()
            successful_var = tk.StringVar(value='successful ! ! ! ')
            successful_label = tk.Label(self.root, textvariable=successful_var, bg="#1E1E1E", fg="red", font=("Helvetica", 8))
            successful_label.place(x=440, y=530)

        else:
            build_road_networkx = AboutNetwork(file_path=self.file_path, Host_file_path = self.Host_file_path, Expressway=True)
            G_Point, G_Road, G_Simplify, G_Plus = build_road_networkx(combined_network=True, draw=True, save=True)

            # 图像名称
            image_name = str(int(time.time())) + '.png'
            Head_home.cache(G_Plus, build_road_networkx.G_Plus_pos, image_name)

            # 生成图像至界面
            Head_home.show_pic(root=self.root, image_name=image_name)

            # 删除缓存文件
            os.remove(image_name)

            Generation_label.place_forget()
            successful_var = tk.StringVar(value='successful ! ! ! ')
            error_label = tk.Label(self.root, textvariable=successful_var, bg="#1E1E1E", fg="red", font=("Helvetica", 8))
            error_label.place(x=440, y=530)
