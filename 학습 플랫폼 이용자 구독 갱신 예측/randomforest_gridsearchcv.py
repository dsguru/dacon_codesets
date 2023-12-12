import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, roc_auc_score, precision_score

# 데이터 불러오기
train = pd.read_csv('/data/train.csv')
test = pd.read_csv('/data/test.csv')

# train 데이터 분리
train_user_id = train['user_id']
x_train = train.drop(['user_id', 'target'], axis = 1)
y_train = train['target']

# test 데이터 분리
x_test = test.drop('user_id', axis = 1)
test_user_id = test['user_id']

# 데이터프레임 생성
x_train = pd.DataFrame(x_train)
y_train = pd.DataFrame(y_train)
x_test = pd.DataFrame(x_test)

# 원-핫 인코딩
x_train = pd.get_dummies(x_train)
x_test = pd.get_dummies(x_test)

# train 데이터 train, val 분리
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train['target'],
                                                  test_size = 0.2,
                                                  stratify = y_train['target'],
                                                  random_state = 2023)

# 파라미터
rf_params = {'n_estimators': [30, 70, 100],
             'max_depth': [6, 8, 10],
             'min_samples_leaf': [1, 2, 3],
             }

# 하이퍼파라미터 튜닝
rf = RandomForestClassifier(random_state = 2023)
grid_rf = GridSearchCV(rf, param_grid = rf_params, cv = 10)
grid_rf.fit(x_train, y_train)

print('최적 하이퍼파라미터:', grid_rf.best_params_)
print('Best 예측정확도:', grid_rf.best_score_)

# 모델 생성
model = RandomForestClassifier(n_estimators = 70,
                                 max_depth = 6,
                                 min_samples_leaf = 1,
                                 random_state = 2023)

# 모델 훈련
model.fit(x_train, y_train)

# 검증 데이터로 검증
y_pred = model.predict(x_val)

# 정확도, F1 Score, 재현율, 정밀도, ROC-AUC Curve
accuracy = accuracy_score(y_val, y_pred)
f1_score = f1_score(y_val, y_pred)
recall = recall_score(y_val, y_pred)
roc_auc = roc_auc_score(y_val, y_pred)
precision = precision_score(y_val, y_pred)

# 정확도
print(accuracy)

# F1 Score
print(f1_score)

# 재현율
print(recall)

# 정밀도
print(precision)

# ROC-AUC Curve
print(roc_auc)

# 대회용 Macro F1 Score
print(f1_score(y_val, y_pred, average = 'macro'))

# 제출용 예측 데이터 생성
pred = model.predict(x_test)

# 제출 파일 생성
submit = pd.DataFrame(
    {
        'user_id' : test_user_id,
        'target' : pred
    }
)

submit.to_csv('submisssion.csv', index=False)