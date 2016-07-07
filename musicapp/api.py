import graphlab

loaded_model = graphlab.load_model('/Users/lol/Desktop/Machine Learning/personalized_model')

def recomToDict(recomList):
    res = []
    for i in recomList:
        res.append(i.split('-'))
    return res
