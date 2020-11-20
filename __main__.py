from Train import  Train
import pandas as pd


if __name__ == '__main__':
    image_dir = 'images/'
    my_data = pd.read_csv('label/labels.csv')
    df = pd.DataFrame(my_data)
    train = Train(df,image_dir)
    train.getImageName()

    # train.visualize_image('maksssksksss754.png')
