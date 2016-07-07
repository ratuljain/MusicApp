import graphlab
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base, 'musicapp','personalized_model')

loaded_model = graphlab.load_model(model_path)

def recomToDict(recomList):
    res = []
    for i in recomList:
        res.append(i.split('-'))
    return res
