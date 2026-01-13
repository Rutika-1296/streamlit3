import google.generativeai as genai

genai.configure(api_key="AIzaSyB0VfE3QTVcbYshaaSvhpIOLDiKM_9zlYg")

for m in genai.list_models():
    print(m.name)

