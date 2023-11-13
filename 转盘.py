import tkinter as tk
import math

# 字典中的字符串
strings = ["白玉串城", "芥南", "脊骨土豆", "牛小烫", "蛙锅"]
num_strings = len(strings)

# 旋转指针
rotation_flag = False
rotation_speed = 25  # 旋转速度，可以根据需要调整

# 创建主窗口
root = tk.Tk()
root.title("吃什么")

# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 画圆的边界
radius = 150
center_x = 200
center_y = 200
canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black")

# 计算角度间隔
angle_interval = 360 / num_strings

# 创建文本标签和分割的黑线
labels = []
lines = []
for i in range(num_strings):
    start_angle = math.radians(i * angle_interval)
    end_angle = math.radians((i + 1) * angle_interval)

    label_angle = (start_angle + end_angle) / 2
    label_x = center_x + radius * 0.7 * math.cos(label_angle)
    label_y = center_y + radius * 0.7 * math.sin(label_angle)

    label = canvas.create_text(label_x, label_y, text=strings[i], font=("Arial", 12))
    labels.append(label)

    line_x1 = center_x + radius * math.cos(start_angle)
    line_y1 = center_y + radius * math.sin(start_angle)
    line_x2 = center_x
    line_y2 = center_y

    line = canvas.create_line(line_x1, line_y1, line_x2, line_y2, fill="black")
    lines.append(line)

# 创建红色指针
pointer = canvas.create_line(center_x, center_y, center_x, center_y - radius, fill="red", width=2)

def rotate_pointer(angle=0):
    if rotation_flag:
        angle_rad = math.radians(angle)
        x = center_x + radius * 0.9 * math.cos(angle_rad)
        y = center_y + radius * 0.9 * math.sin(angle_rad)
        canvas.coords(pointer, center_x, center_y, x, y)
        root.update()
        root.after(10, rotate_pointer, angle + rotation_speed)


# 创建开始旋转按钮
start_button = tk.Button(root, text="开始旋转", command=lambda: start_rotation())
start_button.pack(side="left", padx=40, pady=20)  # 设置anchor为"n"，垂直居中

# 创建停止按钮
stop_button = tk.Button(root, text="STOP", command=lambda: stop_rotation())
stop_button.pack(side="right", padx=40, pady=20)  # 设置anchor为"n"，垂直居中


def start_rotation():
    global rotation_flag
    rotation_flag = True
    rotate_pointer()


def stop_rotation():
    global rotation_flag
    rotation_flag = False


root.mainloop()
