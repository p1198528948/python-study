# 
# 代码解析：

# 1、通过np.linspace生成50个元素均匀的分布在[0,2pi]区间的数组，

# 2、plt.plot(x,y，"线的样式",label="标记")　　# 前两个参数时x,y的取值，第三个参数是线的样式，第四个参数是右上角的标记，和plt.legend()配套使用

# 3、plt.title("****)设置标题

# 4、plt.xlim()或plt.ylim()设置x坐标轴或者y坐标轴的范围

# 5、# 通过xticks或yticks来设置轴的刻度。

# 6、plt.xlabel("x")设置x轴的名称
# 

import matplotlib.pyplot as plt
import numpy as np

# 用np.linspace生成50个元素的数组，均匀的分布在（0,2*pi）区间上面
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)
# 把x;y函数画出来，用黄色的*-线
plt.plot(x, y, "y*-",label="y=sin(x)")
# 把x,y*2函数画出来，用品红的--线
plt.plot(x, y * 2, ":", label="y=2sin(x)")

z = np.cos(x)
plt.plot(x, z, "-.", label="y=cos(x)")
plt.plot(x, z * 2, "m--", label="y=2cos(x)")

plt.legend()
# plt.legend(loc="best")

plt.title("sin(x) & 2sin(x) & cos(x)")  # 设置标题

plt.xlim(0, 6)  # 设置x坐标轴的范围
plt.ylim(-3, 3)    # 设置y坐标轴的范围
# 通过xticks或yticks来设置轴的刻度。
plt.xticks((0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2))

plt.xlabel("x")    # 设置x轴的名称
plt.ylabel("y")    # 设置y轴的名称

# 展现
plt.show()