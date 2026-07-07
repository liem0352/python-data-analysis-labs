import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def load_wine_data(target_feature_index=0):
    """
    加载wine数据集，将指定特征作为目标变量
    参数：
        target_feature_index: 作为目标变量的特征索引
    返回：
        X: 特征数据（不包含目标特征）
        y: 目标变量
        feature_names: 特征名称列表
    """
    wine = load_wine()
    
    # 选择一个特征作为目标变量（这里选择第一个特征：酒精含量）
    target_feature_name = wine.feature_names[target_feature_index]
    print(f"将 '{target_feature_name}' 作为目标变量进行回归预测")
    
    # 创建目标变量和特征数据
    y = wine.data[:, target_feature_index]
    X = np.delete(wine.data, target_feature_index, axis=1)
    
    # 更新特征名称列表（移除目标特征）
    feature_names = wine.feature_names.copy()
    del feature_names[target_feature_index]
    
    print(f"数据集加载完成，共有 {X.shape[0]} 个样本，{X.shape[1]} 个特征")
    return X, y, feature_names

def split_data(X, y, test_size=0.2, random_state=42):
    """
    划分训练集和测试集
    参数：
        X: 特征数据
        y: 目标变量
        test_size: 测试集比例
        random_state: 随机种子
    返回：
        X_train, X_test, y_train, y_test: 划分后的数据集
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"数据划分完成，训练集 {X_train.shape[0]} 个样本，测试集 {X_test.shape[0]} 个样本")
    return X_train, X_test, y_train, y_test

def train_linear_regression(X_train, y_train):
    """
    训练线性回归模型
    参数：
        X_train: 训练特征
        y_train: 训练目标
    返回：
        model: 训练好的线性回归模型
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("线性回归模型训练完成")
    
    # 输出模型系数
    print(f"截距: {model.intercept_:.4f}")
    print("特征系数:")
    for i, coef in enumerate(model.coef_):
        print(f"  特征{i+1}: {coef:.4f}")
    
    return model

def evaluate_model(model, X_test, y_test):
    """
    评估线性回归模型性能
    参数：
        model: 训练好的模型
        X_test: 测试特征
        y_test: 测试目标
    """
    # 预测
    y_pred = model.predict(X_test)
    
    # 计算评估指标
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n模型评估指标:")
    print(f"均方误差 (MSE): {mse:.4f}")
    print(f"均方根误差 (RMSE): {rmse:.4f}")
    print(f"平均绝对误差 (MAE): {mae:.4f}")
    print(f"R² 决定系数: {r2:.4f}")
    
    # 输出前5个预测值和真实值的对比
    print("\n前5个样本的预测值与真实值对比:")
    for i in range(5):
        print(f"  样本{i+1}: 预测值 = {y_pred[i]:.4f}, 真实值 = {y_test[i]:.4f}")

def main():
    """
    主函数：执行完整的线性回归模型训练和评估流程
    """
    print("=== 基于wine数据集的线性回归模型训练与评估 ===")
    
    # 加载数据（以酒精含量作为目标变量）
    X, y, feature_names = load_wine_data(target_feature_index=0)
    
    # 划分数据
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # 训练模型
    model = train_linear_regression(X_train, y_train)
    
    # 评估模型
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
