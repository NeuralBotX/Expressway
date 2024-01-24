from tkinter import filedialog
from Expressway.Graph.Network import AboutNetwork



def home_centre_pos(root,width, height):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算窗口左上角坐标使其居中
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    return x,y


def choose_file(self):
    file_path = list(filedialog.askopenfilenames(title="选择文件", filetypes=[("All Files", "*.*")]))
    self.file_path = file_path
    return file_path

