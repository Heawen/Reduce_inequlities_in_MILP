
# 输入由sagemath equality_generator 生成的不等式组，文件filename1
# 例如:'An inequality (-1, -1, -1, 3, -1, -1, 0, 0, 0, 0, 2) x + 2 >= 0 \n'
# 将其转换为'-1 -1 -1 3 -1 -1 0 0 0 0 2 2 ' 存入文件filename2中

if __name__ == '__main__':
    filename1 = 'inequalities_of_mod_add.txt'
    filename2 = 'inequalities.txt'
    readfile = open(filename1, "r")
    writefile = open(filename2,"w")
    for l in readfile:
        l = l.rstrip('= 0\n')
        l = l.strip('An inequality ')
        print(l)
        for i in l:
            if i not in ['(', ' ', ')', 'x', '>']:
                if i == ','or i == '+':
                    writefile.write(' ')
                else:
                    writefile.write(i)
        writefile.write('\n')
    readfile.close()
    writefile.close()

