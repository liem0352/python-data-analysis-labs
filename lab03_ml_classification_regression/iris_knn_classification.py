import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_iris_data():
    """
    加载iris数据集
    返回：
        X: 特征数据
        y: 目标标签
    """
    iris = load_iris()
    X = iris.data
    y = iris.target
    print(f"数据集加载完成，共有 {X.shape[0]} 个样本，{X.shape[1]} 个特征")
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    划分训练集和测试集
    参数：
        X: 特征数据
        y: 目标标签
        test_size: 测试集比例
        random_state: 随机种子
    返回：
        X_train, X_test, y_train, y_test: 划分后的数据集
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"数据划分完成，训练集 {X_train.shape[0]} 个样本，测试集 {X_test.shape[0]} 个样本")
    return X_train, X_test, y_train, y_test

def train_knn_model(X_train, y_train, n_neighbors=3):
    """
    训练KNN分类器
    参数：
        X_train: 训练特征
        y_train: 训练标签
        n_neighbors: K值
    返回：
        model: 训练好的KNN模型
    """
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    print(f"KNN模型训练完成，K值 = {n_neighbors}")
    return model

def evaluate_model(model, X_test, y_test):
    """
    评估模型性能
    参数：
        model: 训练好的模型
        X_test: 测试特征
        y_test: 测试标签
    """
    # 预测
    y_pred = model.predict(X_test)
    
    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"模型准确率: {accuracy:.4f}")
    
    # 分类报告
    print("\n分类报告:")
    print(classification_report(y_test, y_pred, target_names=['setosa', 'versicolor', 'virginica']))
    
    # 混淆矩阵
    print("\n混淆矩阵:")
    print(confusion_matrix(y_test, y_pred))

def main():
    """
    主函数：执行完整的KNN分类模型训练和评估流程
    """
    print("=== 基于iris数据集的KNN分类模型训练与评估 ===")
    
    # 加载数据
    X, y = load_iris_data()
    
    # 划分数据
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # 训练模型
    model = train_knn_model(X_train, y_train)
    
    # 评估模型
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
