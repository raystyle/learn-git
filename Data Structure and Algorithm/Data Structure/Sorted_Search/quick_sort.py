"""
https://www.geeksforgeeks.org/quick-sort/   

快速排序:单向扫描  https://blog.csdn.net/k_koris/article/details/80585979  单 两 三路
快速排序:双向扫描  本文

优化：

1 Pick a random element as pivot

2 快速排序:三路快排 LeetCode75
  在使用有序或者近乎有序的数组测试时，算法的执行时间大大增加，经过分析发现：
  原来该算法O(nlogn)的复杂度会退化成为O(n^2)，这显然是和快排这个名称不想符的，
  于是笔者又经过分析与查阅资料了解到了所谓三路快排，该算法应用更加广泛，
  甚至Java将三路快排作为系统库中默认的排序算法
"""

class Quick():
    def __init__(self):
        pass

    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)

    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)
            print(splitpoint)

            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:
            # 左指针 右移
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            # 右指针 左移
            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            # 指针交叉 找到了分裂点
            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        # 找到分裂点后 将枢轴点 与rightmark 交换
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

    def quick_sort_bizhan(self, alist, first, last):
        if first >= last:
            return
        mid_value = alist[first]
        low = first
        high = last
        while low < high:
            # high 左移
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]

            # low 右移
            while low < high and alist[low] < mid_value:
                low += 1
            alist[high] = alist[low]

        # 循环退出时 low==high
        alist[low] = mid_value

        # 对low左边的列表执行快速排序
        self.quick_sort_bizhan(alist, first, low - 1)

        # 对low右边的列表执行快速排序
        self.quick_sort_bizhan(alist, low + 1, last)


if __name__ == "__main__":
    # 第一种
    q = Quick()
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # alist = [26,20]
    # alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    q.quickSort(alist)
    print(alist)
    # [31, 26, 20, 17, 44, 54, 77, 55, 93]
    # 5
    # [17, 26, 20, 31, 44, 54, 77, 55, 93]
    # 3
    # [17, 26, 20, 31, 44, 54, 77, 55, 93]
    # 0
    # [17, 20, 26, 31, 44, 54, 77, 55, 93]
    # 2
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # 7
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]

    # 第一种
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    q.quick_sort_bizhan(alist2, 0, len(alist2) - 1)
    print(alist2)
