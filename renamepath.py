import os

def filelist(thefolder):
    count = 0
    file_list = []
    for filename in os.listdir(thefolder):
        path = os.path.join(thefolder, filename)
        if path[-4:] == '.tif':
            count += 1
            file_list.append(path)
    #file_list.append(count)
    return count, file_list


def renamefile(folder):
    file_list_to_rename = filelist(folder)[1]
    for file in file_list_to_rename:
        if 'testtile1' in file:
            folderpath = file.split('/')
            items = folderpath[-1].split('_')
            stagenumber = int(items[3][5:]) - 1
            stagenumberformat = '0' + str(stagenumber)
            newname = items[1] + ' ' + items[2] + '--' + 'Stage' + stagenumberformat[-2:] + '--' + items[5][-7:-4] + '--' + 'C' + items[5][2:4] + '.tif'
            newpath = '/'.join(folderpath[:-1]) + '/' + newname
            os.rename(file, newpath)




if __name__ == '__main__':
    folder = '/home/hao/Desktop/try/try1try'
    renamefile(folder)
