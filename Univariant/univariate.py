import pandas as pd
import numpy as nm

class univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columname in dataset.columns:
            if (dataset[columname].dtype=='O'):
                qual.append(columname)
            else:
                quan.append(columname)
        return quan,qual
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                                    "Q3:75%","99%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive.loc["Mean", columnName] = dataset[columnName].mean()
            descriptive.loc["Median", columnName] = dataset[columnName].median()
            descriptive.loc["Mode", columnName] = dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%", columnName] = dataset.describe()[columnName]["25%"]
            descriptive.loc["Q2:50%", columnName] = dataset.describe()[columnName]["50%"]
            descriptive.loc["Q3:75%", columnName] = dataset.describe()[columnName]["75%"]
            descriptive.loc["99%", columnName] = nm.percentile(dataset[columnName],99)
            descriptive.loc["Q4:100%", columnName] = dataset.describe()[columnName]["max"]
            descriptive.loc["IQR", columnName] = descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive.loc["1.5rule", columnName] = 1.5*descriptive[columnName]["IQR"]
            descriptive.loc["Lesser", columnName] = descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive.loc["Greater", columnName] =descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive.loc["Min", columnName] = dataset[columnName].min()
            descriptive.loc["Max", columnName] = dataset[columnName].max()
        return descriptive
