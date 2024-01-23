import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

class DragDropUploader:
    def __init__(self):
        self.root = TkinterDnD.Tk()
        # 初始化界面
        self.appearance()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = int((screen_width - 800) / 2)
        y_position = int((screen_height - 600) / 2)
        self.root.geometry(f"800x600+{x_position}+{y_position}")
        self.create_widgets()

    def appearance(self):
        self.root.title("Expressway")
        # 调节页面大小
        self.root.geometry("2000x830")
        # 调整界面大小至全屏
        # self.root.attributes('-fullscreen', True)


    def drop(self, event):
        file_paths = event.data
        if file_paths:
            print("用户上传的文件路径：", file_paths)

    def exit_app(self):
        self.root.destroy()  # 销毁窗口，结束应用程序

    def create_widgets(self):
        # Create a frame to contain the drop area
        drop_frame = tk.Frame(self.root, width=600, height=100)
        drop_frame.pack()

        # Create a drop area within the frame
        drop_area = tk.Label(drop_frame, text="拖拽文件至此处上传", font=("Arial", 14), bg="lightgray", padx=20, pady=20)
        drop_area.pack(fill=tk.BOTH, expand=True)

        # Register drop event
        drop_area.drop_target_register(DND_FILES)
        drop_area.dnd_bind('<<Drop>>', self.drop)

        exit_button = tk.Button(self.root, text="退出", command=self.exit_app)
        exit_button.pack()


    def run(self):
        self.root.mainloop()


# Instantiate and run the uploader
uploader = DragDropUploader()
uploader.run()


