import pandas as pd

data = {
    '학번' : range(2000,2010)
    ,'성적':[85,95,75,70,100,100,95,85,80,85]
}

print(pd.DataFrame(data))
print(pd.DataFrame(data, columns= ['성적','학번']))
print(pd.DataFrame(data, columns= ['성적','학번'],index=['a','b','c','d','e','f','g','h','i','j']))
