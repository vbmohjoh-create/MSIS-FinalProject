from datasets import load_dataset
import pandas as df

#load dataset
MyDataset=load_dataset("KFUPM-JRCAI/arabic-generated-abstracts");


dfby_polishing=df.DataFrame(MyDataset["by_polishing"]);
dffrom_title=df.DataFrame(MyDataset["from_title"]);
dffrom_title=df.DataFrame(MyDataset["from_title_and_content"]);


featrures = [
    "original_abstract",
    "allam_generated_abstract",
    "jais_generated_abstract",
    "llama_generated_abstract",
    "openai_generated_abstract"
]



def checkShortText(df,DatasetName):
    print("Dataset Name : ",DatasetName)
    for feature in featrures:
        print(df[feature].info)




def hello():
    print("Hi")