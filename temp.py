import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

data1=pd.read_csv("round_data_1_100_1.csv")
data2=pd.read_csv("round_data_100_1000_10.csv")
data=pd.concat([data1,data2],ignore_index=True)

mean=data.groupby('n')['rounds'].mean().reset_index()
median=data.groupby('n')['rounds'].median().reset_index()
mode=data.groupby('n')['rounds'].apply(lambda x: x.mode().iloc[0]).reset_index()

xmean=mean['n'].values.reshape(-1,1)
ymean=mean['rounds'].values
modelmean=LinearRegression()
modelmean.fit(xmean,ymean)
plt.scatter(xmean,ymean,color='purple',s=3)
plt.plot(xmean, modelmean.predict(xmean), color='red')

xmedian=median['n'].values.reshape(-1,1)
ymedian=median['rounds'].values
modelmedian=LinearRegression()
modelmedian.fit(xmedian,ymedian)
plt.scatter(xmedian,ymedian,color='yellow',s=3)
plt.plot(xmedian, modelmedian.predict(xmedian), color='green')

xmode=mode['n'].values.reshape(-1,1)
ymode=mode['rounds'].values
modelmode=LinearRegression()
modelmode.fit(xmode,ymode)
plt.scatter(xmode,ymode,color='orange',s=3)
plt.plot(xmode, modelmode.predict(xmode), color='blue')

plt.xlabel('n')
plt.ylabel('rounds')
plt.show()

ymean_pred=modelmean.predict(xmean.reshape(-1,1))
ymedian_pred=modelmedian.predict(xmedian.reshape(-1,1))
ymode_pred=modelmode.predict(xmode.reshape(-1,1))
print(r2_score(ymean,ymean_pred))
print(r2_score(ymedian,ymedian_pred))
print(r2_score(ymode,ymode_pred))
