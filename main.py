# coding = utf-8
if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib.ticker import MultipleLocator

    import ultraviloet as spec

    # 定义测量数据目录路径
    dirPath = './absorption/New/tmp.txt'
    # (此处为242峰)
    # dirPath = './absorption/New/Zns-LMY.txt'
    # dirPath = './absorption/Zns.txt'

    # 定义原始数据文件路径
    filePath = './absorption/CDS/0.txt'

    # 定义波长范围
    wavelength = np.arange(200, 351, 1)

    # 实例化类
    u_matrix = spec.ultraviloet(wavelength)

    # 获得Ax=b中的各个矩阵
    u_matrix._get_matrix_a(dirPath)
    u_matrix._panning(242)
    u_matrix._get_matrix_x(filePath)

    qiepian = np.arange(0,39,10)
    u_matrix.matrix_a = u_matrix.matrix_panning[qiepian,:]
    u_matrix._get_matrix_b()

    u_matrix._restoration("ALM")

    # 绘制图像
    fig = plt.figure(figsize=(12, 6), dpi=200)

    plt_type = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
    # for plt_tmp in range(0, u_matrix.matrix_a_length):
        # ax = fig.add_subplot(u_matrix.matrix_a_length,1,plt_tmp+1)
        # plt.scatter(wavelength, u_matrix.matrix_a[plt_tmp, :], marker='*', s=4, label = str(plt_tmp+1))
        # plt.scatter(wavelength, u_matrix.matrix_a, marker='*', s=4, label='zns-xh')

        # plt.plot(wavelength, u_matrix.matrix_panning[plt_tmp, :], label = str(plt_tmp+1))
        # plt.plot(wavelength, u_matrix.matrix_panning[plt_tmp, :])

        # plt.plot(wavelength, u_matrix.matrix_a, label='zns-xh')

    plt.plot(wavelength, u_matrix.matrix_x[0,:],label = 'original')
    plt.plot(wavelength, u_matrix.xil, label='10nm(175)')

    plt.xlabel("wavelength/nm", fontdict={'size': 12})
    plt.ylabel("Transmittance", fontdict={'size': 12})
    x_major_locator = MultipleLocator(10)  # 以每10显示
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    plt.title("Comparison", fontdict={'size': 15})
    plt.legend(loc='best')
    # plt.savefig("250-280.svg")
    plt.show()
