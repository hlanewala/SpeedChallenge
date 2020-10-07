from models.keras_models import *
from helper_functions import *
from image_preprocessing import *
import models.FlowNet_S as flownet_s
from optical_flow_pipeline import *
import generator


if __name__ == '__main__':
    model = flownet_s.FlowNet_S()
    model.build(input_shape=(None, 384, 512, 6))
    model.load_weights('../data/Local_Data/FlowNetS_Checkpoints/flownet-S2')
    model.compile()
    model.summary()

    # extract_frames = False
    # generate_pipeline = True
    image_directory = "..\data\Images"
    # if extract_frames:
    #     # renaming of files is done during extraction of frames
    #     frame_extractor()
    #
    # # this will generate the pipeline, we can use for training the keras model
    # if generate_pipeline:
    #     my_training_batch_generator, my_validation_batch_generator = generator.My_Custom_Generator(image_directory)
    #
    # optical_flow_pipeline_with_VGG_16(image_directory)
    # print('Done')
