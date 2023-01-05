# coding = utf-8
if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt

    import spectrometer as spec

    # 定义测量数据目录路径
    dirPath = './absorption/New/Zns-XH.txt'
    # 定义原始数据文件路径
    filePath = './absorption/Zns.txt'
    # 定义波长范围
    wavelength = np.arange(200, 501, 1)
    # 实例化类
    u_matrix = spec.Spectrometer(wavelength)
    # 获得Ax=b中的各个矩阵
    u_matrix._get_matrix_a(dirPath)
    u_matrix._get_matrix_x(filePath)
    # u_matrix._get_matrix_b()

    # u_matrix._restoration("ALM")

    # 绘制图像
    fig = plt.figure(figsize=(12, 6), dpi=200)

    plt_type = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
    for plt_tmp in range(0, u_matrix.matrix_a_length):
        ax = fig.add_subplot(u_matrix.matrix_a_length,1,plt_tmp+1)
        # plt.scatter(wavelength, u_matrix.matrix_a[plt_tmp, :], marker='*', s=4, label = str(plt_tmp+1))
        plt.scatter(wavelength, u_matrix.matrix_a, marker='*', s=4, label='zns-xh')

    plt.xlabel("wavelength/nm", fontdict={'size': 12})
    plt.ylabel("Transmittance", fontdict={'size': 12})
    plt.title("ALL", fontdict={'size': 15})

    plt.legend(loc='best')
    # plt.savefig("test.svg")
    plt.show()
