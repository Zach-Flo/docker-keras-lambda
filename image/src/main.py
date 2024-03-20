import numpy as np
import tensorflow as tf
import os
import json
def handler(event, context):
    model_dir = './1'
    output = os.listdir(".")
    load_model = tf.keras.models.load_model(model_dir)

    sample_data = gen_input_data()
    test = load_model.predict(sample_data).tolist()
    output = json.dumps(test)
    return {"statusCode": 200, "body": output}

def gen_input_data(shape1 = (1,5),shape2 = (1,24,77)):
    input1 = np.random.randint(low =0,high = 100,size = shape1)
    input2 = np.random.randint(low = 0,high = 100, size = shape2)
    inputs = [input1,input2]
    return inputs
    
