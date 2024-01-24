import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog
import Head_home
from tkinter import ttk
import os
from PIL import Image, ImageTk

from Expressway.Graph.Network import AboutNetwork


class FileDragDropApp:
    def __init__(self):

        # 初始化
        self.root = TkinterDnD.Tk()

        self.file_path_var = tk.StringVar(value='None')
        self.folder_path_var = tk.StringVar(value='None')
        self.choice_var = tk.StringVar(value='True')

        self.file_path = None
        self.Host_file_path = None


        # 主页面
        self.root = self.home(self.root)

        # 运行主循环
        self.root.mainloop()


    def home(self,root):


        # 窗口标题
        root.title("Expressway System")

        # 设置窗口图标
        icon_path = "image/logo/logo.ico"  # 替换成你的图标文件路径
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

        # 创建打开文件按钮
        open_file_button = ttk.Button(root, text="打开数据文件", command=self.choose_file, style="TButton")
        open_file_button.place(x=100, y=50)

        # 显示选中的文件
        file_text = tk.Label(root, text="执行文件:  ", bg="#1E1E1E", fg="#3794FF", font=("Helvetica", 12))
        file_text.place(x=300, y=50)
        file_label = tk.Label(root, textvariable=self.file_path_var, bg="#1E1E1E", fg="#FFFFFF",font=("Helvetica", 12))
        file_label.place(x=370, y=50)


        # 创建打开文件夹按钮
        open_folder_button = ttk.Button(root, text="打开文件夹", command=self.choose_folder, style="TButton")
        open_folder_button.place(x=100, y=10)

        # 显示选中的文件
        folder_text = tk.Label(root, text="宿主文件:  ", bg="#1E1E1E", fg="#3794FF", font=("Helvetica", 12))
        folder_text.place(x=300, y=10)
        folder_label = tk.Label(root, textvariable=self.folder_path_var, bg="#1E1E1E", fg="#FFFFFF",font=("Helvetica", 12))
        folder_label.place(x=370, y=10)


        # 创建按钮样式
        run_button_style = ttk.Style()
        run_button_style.configure("Run.TButton", padding=(80, 2))


        # 创建生成网络按钮
        run_button = ttk.Button(root, text="生成网络", command=self.run, style="Run.TButton")
        run_button.place(x=400, y=500)


        return root


    def choose_file(self):
        file_path = list(filedialog.askopenfilenames(title="选择文件", filetypes=[("All Files", "*.*")]))
        self.file_path = file_path
        self.file_path_var.set("  ;  ".join([os.path.basename(path) for path in file_path]))
        print(self.file_path)


    def choose_folder(self):
        folder_path = filedialog.askdirectory()
        self.Host_file_path = folder_path
        self.folder_path_var.set(folder_path)
        print(self.Host_file_path)


    def run(self):

        image_path = "image/2022-11-25.png"

        if image_path:
            # 使用Pillow加载图像
            image = Image.open(image_path)
            image = image.resize((470, 330))
            # 将图像转换为Tkinter PhotoImage
            tk_image = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.root, bg="#1E1E1E")
            image_label.place(x=300, y=130)
            # 更新Label中的图像
            image_label.config(image=tk_image)
            # 保留对图像对象的引用，以避免垃圾回收
            image_label.image = tk_image


        # AboutNetwork(file_path=self.file_path, Host_file_path = self.Host_file_path, Expressway=True)




if __name__ == "__main__":
    FileDragDropApp()

