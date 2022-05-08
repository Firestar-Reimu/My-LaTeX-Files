def permutations(a, arr, pos, end):  # 获取列表的全排列
    if pos == end:  # 递归结束
        arr = arr[:]
        a.append(arr)
    else:
        for index in range(pos, end):
            arr[index], arr[pos] = arr[pos], arr[index]  # 交换相邻两个元素
            permutations(a, arr, pos+1, end)  # 列表长度-1
            arr[index], arr[pos] = arr[pos], arr[index]  # 交换相邻两个元素
    return a