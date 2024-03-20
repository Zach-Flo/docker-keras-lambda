import numpy as np
import tensorflow as tf
import json

def handler(event, context):
    
    model_dir = 'saved_model'

    # Define load options with experimental_io_device
    load_options = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')


    load_model = tf.keras.models.load_model(model_dir, options=load_options)

    sample_data = gen_input_data()
    load_model.predict(sample_data)
    list = sample_data.tolist()
    data = json.dumps(list)
    return {"statusCode": 200, "body": data}

def gen_input_data(shape1 = (1,5),shape2 = (1,24,77)):
    input1 = np.random.randint(low =0,high = 100,size = shape1)
    input2 = np.random.randint(low = 0,high = 100, size = shape2)
    inputs = [input1,input2]
    return inputs
    