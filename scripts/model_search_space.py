#!/usr/bin/env python3
# -*- coding: utf-8 -*-


model_search_space = {
    "svc": [
                {
                    'C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'kernel': ['linear']
                },
                {
                    'C': [0.001, 0.01, 0.1, 1, 10, 100],
                    'kernel': ['rbf'],# 'sigmoid'],
                    'gamma': ['auto', 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8]
                },
                # {
                #     'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                #     'kernel': ['poly'],
                #     'degree': [2, 3, 4],
                #     'gamma': ['auto']
                # }
    ],
    "lda": [
            {'solver': ['svd']}
    ],
    "qda": {'reg_param': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]},
    "logisticregression": [
            {
                'penalty': ['l2'],
                'solver': ['liblinear', 'lbfgs'],
                'C': [0.0001, 0.001, 0.01, 0.1, 1, 10, 100],
                'max_iter': [500],
                'class_weight': ['balanced', None]
            },
    ],
    "randomforest": {
        'n_estimators': [100],
        'max_depth': [4, 6, 8, 10],
        'min_samples_leaf': [2, 4, 6, 8, 10],
        'max_features': ['sqrt'],
        'class_weight': ['balanced'],
        'bootstrap': [True, False]
    },
    "gradientboosting": {
        'n_estimators': [100, 500, 1000, 5000],
        'learning_rate': [0.001, 0.01, 0.1, 1],
        'subsample': [0.3, 0.7, 1],
        'min_samples_split': [2, 3, 4]
    },
    "adaboost": {
        'n_estimators': [100, 500, 1000, 5000],
        'learning_rate': [0.001, 0.01, 0.1, 1]
    },
    "knn": {
        'n_neighbors': [2, 3, 5, 7],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto']
    },
    "xgboost": {
        'max_depth': [2, 3, 6, 8],
        'eta': [0.01, 0.1, 0.3, 1],
        'gamma': [0, 0.01, 0.1, 1, 10],
        'subsample': [0.2, 0.4, 0.6, 0.8, 1],
        'lambda': [0.1, 1, 10, 100],
        'colsample_bytree': [0.2, 0.4, 0.6, 0.8]
    }
}
