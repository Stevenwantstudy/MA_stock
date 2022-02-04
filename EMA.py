import numpy as np
import xlrd
import matplotlib.pyplot as plt
from numpy import*

#定于指数移动平均的算法
def EMA(list,alpha):
    new_list = np.zeros(len(list))              #list是我们原始的数列，new_list是跟原数列数据一样的一组数列
    new_list[0] = list[0]                       #将原属list中的第一个值 赋值给新的list
    for i in range(1,len(list)):
        new_list[i] = alpha*list[i] + (1-alpha)*new_list[i-1]

    return new_list

#取到数列
def x_data(list1):
    X = []
    # 取第600行到最后的数据
    for i in range(len(list1)):
        X.append(i)

    return X


if __name__ == "__main__":
    #nums = 7
    alpha = 0.4
    data = xlrd.open_workbook("///Users/liuxiao/Desktop/else/stock/price.xls")
    #打开excel文件
    table = data.sheet_by_index(0)
    # 获取到第一个表单的数据
    list = table.col_values(2)
    #取列表中一部分数据
    list1 = list[600:]
    #直接取到600到最后一个数
    X1 = x_data(list1)



    del list[0]
    plt.plot(X1,list1,"g",label = "未处理的值",linewidth =1)
    plt.xlabel("time")
    plt.ylabel("lowest_price")


    plt.plot(X1,EMA(list1,alpha),"r",label= "EMA",linewidth =1,linestyle='--')
    plt.xticks(X1,X1)
    # plt.xlim(0,800)
    # plt.ylim(15,22)
    # plt.xticks(range(0,180,6))
    # plt.yticks(arange(15.6,19.2,0.2))
    # plt.title('alpha = 0.4')                #设置图形的标题
    # plt.savefig('filename.png', dpi=4000)   #设置图片的像素
    # plt.show()

    print





