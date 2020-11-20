import numpy
import  os
import  cv2
import matplotlib.pyplot as plt

class Train:
    def __init__(self,df,image_dir):
        self.df = df
        self.image_dir = image_dir

    def getImageName(self):
        image_name = []
        for dirname, _, filenames in os.walk(self.image_dir):
            for filename in filenames:
                if filename.endswith(".png"):
                    image_name.append(filename)
        return image_name

    def getpath(self,image_name):
        image_path = self.image_dir + image_name

        result = []
        item_list = self.df[self.df.filename == image_name]
        for item in item_list.index:
            data_class = item_list['class'][item]
            bnbox = [(int(item_list['xmin'][item]), int(item_list['ymin'][item])),
                     (int(item_list['xmax'][item]), int(item_list['ymax'][item]))]
            result.append((data_class, bnbox))

        size = [int(item_list['width'][item]),
                int(item_list['height'][item])]
        return image_path, result, size

    def visualize_image(self,image_name, bnbox=True):
        image_path, result, size = self.getpath(image_name)
        image = cv2.imread(image_path)
        print(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if bnbox:
            thickness = int(sum(size) / 300.)
            # print(thickness)
            for item in result:
                data_class, bnbox = item
                if data_class == 'with_mask':
                    cv2.rectangle(image, bnbox[0], bnbox[1], (0, 255, 0), thickness)
                elif data_class == 'without_mask':
                    cv2.rectangle(image, bnbox[0], bnbox[1], (255, 0, 0), thickness)
                else:  # name == 'none'
                    cv2.rectangle(image, bnbox[0], bnbox[1], (0, 0, 255), thickness)
                cv2.putText(image, data_class, bnbox[0], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 1)
        plt.figure(figsize=(20, 20))
        plt.subplot(1, 2, 1)
        plt.axis('off')
        plt.title(image_name)
        plt.imshow(image)
        plt.show()

