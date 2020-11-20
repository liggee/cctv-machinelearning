import numpy
import  os
import  cv2
import matplotlib.pyplot as plt
import pandas as pd


my_data = pd.read_csv('label/labels.csv')
df = pd.DataFrame(my_data)

def getImageName():
    image_name = []
    for dirname, _,filenames in os.walk('images/'):
        for filename in filenames:
            print(filename)

def getpath(image_name):
    image_path = 'images/'+image_name

    result = []
    item_list = df[df.filename == image_name]
    for item in item_list.index:
        data_class = item_list['class'][item]
        bnbox = [(int(item_list['xmin'][item]),int(item_list['ymin'][item])),
                 (int(item_list['xmax'][item]),int(item_list['ymax'][item]))]
        result.append((data_class,bnbox))

    size = [int(item_list['width'][item]),
            int(item_list['height'][item])]
    return image_path,result,size


def visualize_image(image_name,bnbox=True):
    image_path,result,size = getpath(image_name)
    image = cv2.imread(image_path)
    print(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if bnbox:
        thickness = int(sum(size) / 300.)
        # print(thickness)
        for item in result:
            data_class,bnbox = item
            if data_class == 'with_mask':
                cv2.rectangle(image, bnbox[0], bnbox[1], (0, 255, 0), thickness)
            elif data_class == 'without_mask':
                cv2.rectangle(image, bnbox[0], bnbox[1], (255, 0, 0), thickness)
            else:  # name == 'none'
                cv2.rectangle(image, bnbox[0], bnbox[1], (0, 0, 255), thickness)
            cv2.putText(image, data_class, bnbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 1)
    plt.figure(figsize=(20, 20))
    plt.subplot(1, 2, 1)
    plt.axis('off')
    plt.title(image_name)
    plt.imshow(image)
    plt.show()

# print(df[df.filename == 'maksssksksss754.png'])
# getImageName('train')
visualize_image('maksssksksss754.png')
# getpath('maksssksksss754.png')