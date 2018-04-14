import os
import skimage.data
import numpy as np

def filelist(thefolder):
    count = 0
    file_list = []
    for filename in os.listdir(thefolder):
        path = os.path.join(inputfolder, filename)
        if path[-4:] == '.tif':
            count += 1
            file_list.append(path)
    #file_list.append(count)
    return count, file_list
#    print count

def outputfilelist(thefolder):
    thefilelist = filelist(thefolder)
    number = thefilelist[0]

    outputfile = '/home/hao/Desktop/track/filelistnumber_' + str(number) + '.txt'
    with open(outputfile,'w') as f:
        for item in thefilelist[-1]:
            file = item.split('/')[-1]
            f.write('%s' % file)
            f.write('\n')
        f.close()



#def outfile():


def stacktoimage(file, outputfolder):
    stack = skimage.data.imread(file)
    if len(stack.shape) == 4:
        stacktranspose = np.transpose(stack, (2,3,0,1))
        stacknumber = stacktranspose.shape[3]

        for i in range(stacknumber):
            filename = file.split('/')[-1]
            outputfiledest = outputfolder + '/' + filename[:-4] + 'Z0' + str(i) + '.tif'
            skimage.io.imsave(outputfiledest, stacktranspose[:,:,:,i])

def convert_execution(runfilelist, outputfolder):
    with open('/home/hao/Desktop/track/tracking.txt', 'w') as f:
        for item in runfilelist:
            stacktoimage(item, outputfolder)
            itemimage = item.split('/')[-1]
            f.write('%s' %itemimage)
            f.write('\n')
        f.close



if __name__ == '__main__':
    inputfolder = '/run/user/1000/gvfs/smb-share:server=130.229.49.177,share=codex'
    outputfilelist(inputfolder)
    runfilelist = filelist(inputfolder)[1]
    outputfolder = '/run/user/1000/gvfs/smb-share:server=storage.scilifelab.se,share=confocal/CELL_PROFILING/CODEX/hao-deconv'

    convert_execution(runfilelist, outputfolder)
