import xlsxwriter as xw

N = int(1e3 + 10)
a = [[0 for _ in range(N)] for _ in range(N)]
n, m = 0, 0


def key_in():
    global n, m, a
    n, m = map(int, input().split())
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            a[i][j] = row[j]
    global col_num
    col_num = []
    for i in range(1, m + 1):
        col_num.append('第' + str(i) + '列')


def cout():
    global n, m
    global a
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()


def xw_toexcel(data, filename):
    workbook = xw.Workbook(filename)
    worksheet1 = workbook.add_worksheet('sheet1')
    worksheet1.activate()  # 表已经激活
    title = ['Generated Graph'] + col_num
    worksheet1.write_row('A1', title)  # 表示开始位置,,横向顺延
    i = 2
    for j in range(n):  # 这个参数放的是行
        row = 'A' + str(i)
        worksheet1.write_row(row, ['第' + str(i - 1) + '行'] + data[i - 2][:m])
        i += 1
    workbook.close()


def main():
    key_in()
    cout()
    xw_toexcel(a, '测试数据1-9(8)')


if __name__ == '__main__':
    main()
