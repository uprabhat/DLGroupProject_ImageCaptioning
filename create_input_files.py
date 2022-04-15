from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    # create_input_files(dataset='coco',
    #                    karpathy_json_path='../caption data/dataset_coco.json',
    #                    image_folder='/media/ssd/caption data/',
    #                    captions_per_image=5,
    #                    min_word_freq=5,
    #                    output_folder='/media/ssd/caption data/',
    #                    max_len=50)

    create_input_files(dataset='flickr8k',
                       karpathy_json_path='../captions_datasets/dataset_flickr8k.json',
                       image_folder='D:/OMSCS/DL/Project/ImageCaptioning/flickr8k/Images',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='D:/OMSCS/DL/Project/ImageCaptioning/flickr8k/out',
                       max_len=50)
