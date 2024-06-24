def reverse_string(s):
    """
    Reverse the given string.
    从提供的PDF文件内容中，我将整理出所有的Python代码片段。以下是整理结果：

```python
# 创建一维数组
b = np.array([1, 2, 3, 4])
print(b)

# 创建二维数组
f = np.array([[1, 2], [3, 4], [5, 6]])
print(f)

# 引用 Numpy 库
import numpy as np
a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])
print(a)
print(b)
print(type(a))
print(type(b))

# 利用一维数组创建二维数组
a = np.arange(12).reshape(3, 4)
print(a)

# 创建随机整数的二维数组
a = np.random.randint(0, 10, (4, 4))
print(a)

# 引入 Pandas 库并创建 Series
import pandas as pd
s1 = pd.Series(['丁一', '王二', '张三'])
print(s1)

# 定位 Series 中的元素
print(s1[1])

# 通过列表创建 DataFrame
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])

# 自定义 DataFrame 的列索引和行索引名称
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])

# 通过字典创建 DataFrame
b = pd.DataFrame({'a': [1, 3, 5], 'b': [2, 4, 6]}, index=['x', 'y', 'z'])

# 读取 Excel 文件
data = pd.read_excel('表格名称.xlsx')
data.head()

# 绘制折线图
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y)
import pylab as pl
pl.xticks(rotation=45)
plt.show()

# 绘制柱状图
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
plt.bar(x, y)
plt.show()

# 绘制散点图
x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x, y)
plt.show()

# Tushare 库的使用
!pip install tushare
import tushare as ts
df = ts.get_k_data('000002', start='2009-01-01', end='2019-01-01')
df.head()
df.to_excel('在这里输入 Excel 表格名字.xlsx', index=False)
df.set_index('date', inplace=True)
df.head()
plt.rcParams['font.sans-serif'] = ['SimHei']
df['close'].plot(title='在这里输入需要加入的标题名称')

# 线性回归模型
df = pd.read_excel('IT 行业收入表.xlsx')
X = df[['自变量名称']]
Y = df['因变量名称']
plt.scatter(X, Y)
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(X, Y)
y = regr.predict([[1.5]])
print(y)
y = regr.predict([[1.5], [2.5], [4.5]])
print(y)
plt.scatter(X, Y)
plt.plot(X, regr.predict(X))
plt.show()
print('系数 a 为:' + str(regr.coef_[0]))
print('截距 b 为:' + str(regr.intercept_))
import statsmodels.api as sm
X2 = sm.add_constant(X)
est = sm.OLS(Y, X2).fit()
est.summary()

# 构建多元线性回归模型（省略部分代码）
X = df[['自变量 1', '自变量 2', '自变量 3', '自变量 4', '自变量 5']]
Y = df['客户价值']

# 逻辑回归模型
X = [[1, 0], [5, 1], [6, 4], [4, 2], [3, 2]]
y = [0, 1, 1, 0, 0]
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.predict([[2, 2]]))
print(model.predict([[1, 1], [2, 2], [5, 5]]))
X = df.drop(columns='特征变量名称')
y = df['目标变量']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
score
y_pred_proba = model.predict_proba(X_test)
a = pd.DataFrame(y_pred_proba, columns=['XXX 概率', 'XXX 概率'])
a.head()
model.coef_
model.intercept_
from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(y_test, y_pred)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:, 1])
a = pd.DataFrame()
a['阈值'] = list(thres)
a['假警报率'] = list(fpr)
a['命中率'] = list(tpr)
a.head()
plt.plot(fpr, tpr)
plt.title('ROC')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.show()
from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test, y_pred_proba[:, 1])
score
a = pd.DataFrame(matrix, columns=['预测不流失 0', '预测流失 1'],
                  index=['实际不流失 0', '实际流失 1'])
a

# 决策树模型
from sklearn.tree import DecisionTreeClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 0, 0, 1, 1]
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
print(model.predict([[5, 5]]))
from sklearn.tree import DecisionTreeRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = DecisionTreeRegressor(max_depth=2, random_state=0)
model.fit(X, y)
print(model.predict([[9, 9]]))
import pandas as pd
df = pd.read_excel('客户信息及违约表现.xlsx')
X = df.drop(columns='是否违约')
y = df['是否违约']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=3, random_state=123)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)
y_pred_proba = model.predict_proba(X_test)
b = pd.DataFrame(y_pred_proba, columns=['……', '……'])
b.head()
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:, 1])
a = pd.DataFrame()
a['阈值'] = list(thres)
a['假报警率'] = list(fpr)
a['命中率'] = list(tpr)
a.head()
plt.plot(fpr, tpr)
plt.show()
score = roc_auc_score(y_test, y_pred_proba[:, 1])
print(score)
model.feature_importances_
features = X.columns
importances = model.feature_importances_
importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)
print(importances_df.sort_values)
from sklearn.model_selection import GridSearchCV
parameters = {'max_depth': [5, 7, 9, 11, 13], 'criterion': ['gini', 'entropy'], 'min_samples_split': [5, 7, 9,11, 13, 15]}
modle = DecisionTreeClassifier()
grid_search = GridSearchCV(model, parameters, scoring='roc_auc', cv=5)
grid_search.fit(X_train, y_train)
grid_search.best_params_
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', max_depth=5, min_samples_split=7)
model.fit(X_train, y_train)
score = accuracy_score(y_pred, y_test)
print(score)

# 朴素贝叶斯模型
from sklearn.naive_bayes import GaussianNB
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = GaussianNB()
model.fit(X, y)
print(model.predict([[5, 5]]))
import pandas as pd
df = pd.read_excel('肿瘤数据.xlsx')
X = df.drop(columns='肿瘤性质')
y = df['肿瘤性质']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
from sklearn.naive_bayes import GaussianNB
nb_clf = GaussianNB()
nb_clf.fit(X_train, y_train)
y_pred = nb_clf.predict(X_test)
y_pred[:100]
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
print(a)
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)

# K 近邻算法
import pandas as pd
df = pd.read_excel('手写字体识别.xlsx')
Df.head()
X = df.drop(columns='对应数字')
y = df['对应数字']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
from sklearn.neighbors import KNeighborsClassifier as KNN
knn = KNN(n_neighbors=5)
knn.fit(X_train, y_train)
from PIL import Image
img = Image.open('测试图片.png')
img = img.resize((32, 32))
img = img.convert('L')
img_new = img.point(lambda x: 0 if x > 128 else 1)
arr = np.array(img_new)
arr_new = arr.reshape(1, -1)
arr_new.shape
y_pred = knn.predict(X_test)
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
print(a)
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
Score
from sklearn.model_selection import GridSearchCV
parameters = {'n_neighbors': [2, 3, 4, 5, 6, 7, 8], 'weights': ['distance']}
knn = KNN()
grid_search = GridSearchCV(knn, parameters, cv=5)
grid_search.fit(X_train, y_train)
grid_search.best_params_['n_neighbors']

# 随机森林模型
from sklearn.ensemble import RandomForestClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = RandomForestClassifier(n_estimators=10, random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
from sklearn.ensemble import RandomForestRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = RandomForestRegressor(n_estimators=10, random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
import pandas as pd
df = pd.read_excel('数据名称.xlsx')
df = df.set_index('trade_date')
df['close-open'] = (df['close'] - df['open']) / df['open']
df['high-low'] = (df['high'] - df['low']) / df['low']
df = df.sort_index()
df['MA5'] = df['close'].sort_index().rolling(5).mean()
df['MA10'] = df['close'].sort_index().rolling(10).mean()
df.dropna(inplace=True)
X = df[['close', 'pre_close', 'change', 'pct_chg', 'vol', 'amount', 'close-open', 'high-low', 'MA5', 'MA10']]
y = np.where(df['change'].shift(1) > 0, 1, -1)
X_length = X.shape[0]
split = int(X_length * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]
model = RandomForestClassifier(max_depth=3, n_estimators=10, min_samples_leaf=10, random_state=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators': [5, 10, 20], 'max_depth': [2, 3, 4, 5], 'min_samples_leaf': [5, 10, 20, 30]}
new_model = RandomForestClassifier(random_state=1)
grid_search = GridSearchCV(new_model, parameters, cv=6, scoring='accuracy')
grid_search.fit(X_train, y_train)
grid_search.best_params_
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()
score = accuracy_score(y_pred, y_test)
print(score)
features = X.columns
importances = model.feature_importances_
a = pd.DataFrame()
a['特征'] = features
a['特征重要性'] = importances
a = a.sort_values('特征重要性', ascending=False)
print(a)
warnings.filterwarnings("ignore")
X_test['prediction'] = model.predict(X_test)
X_test['p_change'] = (X_test['close'] - X_test['close'].shift(1)) / X_test['close'].shift(1)
X_test['origin'] = (X_test['p_change'] + 1).cumprod()
X_test['strategy'] = (X_test['prediction'].shift(1) * X_test['p_change'] + 1).cumprod()
X_test[['strategy', 'origin']].dropna().plot()
plt.gcf().autofmt_xdate()
plt.show()
X_test.index = pd.to_datetime(X_test.index, format='%Y%m%d')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(X_test.index, X_test['strategy'], label='Strategy')
ax.plot(X_test.index, X_test['origin'], label='Origin', linestyle='--')
ax.set_xlabel('Trade Date')
ax.set_ylabel('Value')
ax.legend()
plt.show()

# AdaBoost 与 GBDT 模型
import pandas as pd
df = pd.read_excel('信用卡精准营销模型.xlsx')
X = df.drop(columns='响应')
y = df['响应']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(random_state=123)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(y_pred)
from sklearn.ensemble import AdaBoostClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = AdaBoostClassifier(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
from sklearn.ensemble import AdaBoostRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = AdaBoostRegressor(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)
y_pred_proba = clf.predict_proba(X_test)
y_pred_proba[0:5]
fpr, tpr, thres = roc_curve(y_test.values, y_pred_proba[:, 1])
plt.plot(fpr, tpr)
plt.show()
from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test, y_pred_proba[:, 1])
print(score)
features = X.columns
importances = clf.feature_importances_
importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)

# 产品定价模型
import pandas as pd
df = pd.read_excel('产品定价模型.xlsx')
df.head()
from sklearn.ensemble import GradientBoostingClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = GradientBoostingClassifier(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
from sklearn.ensemble import GradientBoostingRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = GradientBoostingRegressor(random_state=123)
model.fit(X, y)
print(model.predict([[5, 5]]))
df['类别'].value_counts()
df['彩印'].value_counts()
df['纸张'].value_counts()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['类别'] = le.fit_transform(df['类别'])
df['类别'].value_counts()
X = df.drop(columns='价格')
y = df['价格']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(random_state=123)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred[0:50])
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()
model.score(X_test, y_test)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, model.predict(X_test))
print(r2)
features = X.columns
importances = model.feature_importances_
importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)

# 机器学习神器：XGBoost 与 LightGBM 模型
!pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xgboost
from xgboost import XGBRegressor
model = XGBRegressor(random_state=123)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred))
from sklearn.model_selection import GridSearchCV
parameters = {'max_depth': [1, 2, 3, 4, 5, 6, 7], 'n_estimators': [50, 100, 150, 200, 250, 300], 'learning_rate': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]}
model02 = XGBRegressor()
gs = GridSearchCV(model02, parameters, scoring='r2', cv=5)
gs.fit(X_train, y_train)
gs.best_params_
from xgboost import XGBRegressor
model = XGBRegressor(random_state=123, learning_rate=0.1, max_depth=2, n_estimators=50)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print('模型的平均绝对误差(MAE)为', mae)
print('模型的均方误差(MSE)为', mse)
print('可决系数 R2 为', r2)
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_pred.min(), y_pred.max()], 'r--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Diagonal Plot - Actual vs. Predicted')
plt.show()
residuals = y_test - y_pred
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

# LightGBM 算法
from lightgbm import LGBMClassifier
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 0, 1, 1]
model = LGBMClassifier()
model.fit(X, y)
print(model.predict([[5, 5]]))
from lightgbm import LGBMRegressor
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [1, 2, 3, 4, 5]
model = LGBMRegressor()
model.fit(X, y)
print(model.predict([[5, 5]]))
!pip install lightgbm -i https://pypi.tuna.tsinghua.edu.cn/simple
import pandas as pd
df = pd.read_excel('客户信息及违约表现.xlsx')
X = df.drop(columns='是否违约')
Y = df['是否违约']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=123)
from lightgbm import LGBMClassifier
model = LGBMClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
a = pd.DataFrame()
a['预测值'] = list(y_pred)
a['实际值'] = list(y_test)
a.head()
from sklearn.metrics import accuracy_score
score = accuracy_score(y_pred, y_test)
print(score)
y_pred_proba = model.predict_proba(X_test)
from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test.values, y_pred_proba[:, 1])
print(score)
y_pred_proba = model.predict_proba(X_test)
fpr, tpr, thres = roc_curve(y_test, y_pred_proba[:, 1])
plt.plot(fpr, tpr)
plt.show()
features = X.columns
importances = model.feature_importances_
importances_df = pd.DataFrame()
importances_df['特征名称'] = features
importances_df['特征重要性'] = importances
importances_df.sort_values('特征重要性', ascending=False)
from sklearn.model_selection import GridSearchCV
parameters = {'num_leaves': [10, 15, 31], 'n_estimators': [10, 20, 30], 'learning_rate': [0.05, 0.1, 0.2]}
model = LGBMClassifier()
grid_search = GridSearchCV(model, parameters, scoring='roc_auc', cv=5)
grid_search.fit(X_train, y_train)
grid_search.best_params_
model = LGBMClassifier(num_leaves=10, n_estimators=10, learning_rate=0.2)
model.fit(X_train, y_train)
y_pred_proba = model.predict_proba(X_test)
score = roc_auc_score(y_test, y_pred_proba[:, 1])
print(score)

# 特征工程之数据预处理
import pandas as pd
df = pd.DataFrame({'客户编号': [1, 2, 3], '性别': ['男', '女', '男']})
df
df = pd.get_dummies(df, columns=['性别'])
df
df = df.drop(columns='性别_女')
df
df = df.rename(columns={'性别_男': '性别'})
df
df = pd.DataFrame({'房屋编号': [1, 2, 3, 4, 5], '朝向': ['东', '南', '西', '北', '南']})
df
df = pd.get_dummies(df, columns=['朝向'])
df
df = df.drop(columns='朝向_西')
df
from sklearn.preprocessing import LabelEncoder
df = pd.DataFrame({'编号': [1, 2, 3, 4, 5], '城市': ['北京', '上海', '广州','深圳', '北京']})
df
le = LabelEncoder()
label = le.fit_transform(df['城市'])
df['城市'] = label
df
data = pd.DataFrame([[1, 2, 3], [1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])
data
data[data.duplicated()]
data.duplicated().sum()
data = data.drop_duplicates()
data
data = pd.DataFrame([[1, 2, 3], [1, 2, 3], [4, 5, 6]], columns=['c1', 'c2', 'c3'])
data = data.drop_duplicates('c1')
data
data = pd.DataFrame([[1, np.nan, 3], [np.nan, 2, np.nan], [1, np.nan, 0]], columns=['c1', 'c2', 'c3'])
data
data.isnull()
data['c1'].isnull()
data[data['c1'].isnull()]
a = data.dropna(thresh=2)
a
b = data.fillna(data.mean())
b
d = data.fillna(method='backfill')
e = data.fillna(method='bfill')
e
data = pd.DataFrame({'c1': [3, 10, 5, 7, 1, 9, 69], 'c2': [15, 16, 14, 100, 19, 11, 8], 'c3': [20, 15, 18, 21, 120, 27, 29]}, columns=['c1', 'c2', 'c3'])
data
a = pd.DataFrame()
for i in data.columns:
    z = (data[i] - data[i].mean()) / data[i].std()
    a[i] = abs(z) > 2
    """
    return s[::-1]