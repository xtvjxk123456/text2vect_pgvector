from text2vec import SentenceModel
import  json
sentences = ['苹果']
model = SentenceModel(r"D:\Code\text2vec-base-chinese")
embeddings = model.encode(sentences)
# print(json.dumps(embeddings.tolist()[0]))
print('dimension size of vector is: {}'.format(len(json.dumps(embeddings.tolist()[0]))))

# model.encode("如何更换花呗绑定银行卡")