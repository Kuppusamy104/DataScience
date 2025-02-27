class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            #ptint (columnname)
            if(dataset[columnName].dtype == 'O'):
                qual.append(columnName)
            else:
                 quan.append(columnName)
        return quan,qual