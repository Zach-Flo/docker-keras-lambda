import numpy as np
import tensorflow as tf

def handler(event, context):
    
    model_dir = 'saved_model'
    load_model = tf.keras.models.load_model(model_dir)

    sample_data = gen_input_data()
    load_model.predict(sample_data)

    return {"statusCode": 200, "body": tf.__version__}

def gen_input_data(shape1 = (1,5),shape2 = (1,24,77)):
    input1 = np.random.randint(low =0,high = 100,size = shape1)
    input2 = np.random.randint(low = 0,high = 100, size = shape2)
    inputs = [input1,input2]
    return inputs
    