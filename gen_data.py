import numpy as np
import json
# def gen_input_data(shape1 = (1,5),shape2 = (1,24,77)):
#     input1 = np.random.randint(low =0,high = 100,size = shape1)
#     input2 = np.random.randint(low = 0,high = 100, size = shape2)
#     inputs = [input1,input2]
#     return inputs
def gen_input_data(shape1 = (1,5),shape2 = (1,24,77)):
    input1 = np.random.randint(low =0,high = 100,size = shape1)
    input2 = np.random.randint(low = 0,high = 100, size = shape2)
    inputs = [input1.tolist(),input2.tolist()]
    return inputs[0],inputs[1]
input1,input2 = gen_input_data()
sample_data = {
    "signature_name": "serving_default",
    "instances": [
    {
      "input_11": input1,
      "input_12": input2
    }
  ]
}
with open("example_input.json","w") as f:
    json.dump(sample_data,f)
    