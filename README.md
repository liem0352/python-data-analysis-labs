# Python数据分析实训合集

本项目包含4个Python数据分析实训，涵盖数据预处理、特征工程、机器学习模型和统计相关性分析。

## 实训目录

### Lab01 - 学生成绩数据分析
- **技术**：Pandas, NumPy
- **内容**：学生成绩数据生成、CSV读写、数据筛选
- **文件**：`lab01_student_score_analysis/`

### Lab02 - 特征工程
- **技术**：scikit-learn
- **内容**：缺失值处理、特征编码（Label/Ordinal/OneHot）、特征缩放、特征选择、特征离散化
- **文件**：`lab02_feature_engineering/`

### Lab03 - 机器学习：分类与回归
- **技术**：scikit-learn (KNN, LinearRegression)
- **内容**：
  - 基于iris数据集的KNN分类（准确率100%）
  - 基于wine数据集的线性回归（预测酒精含量）
- **文件**：`lab03_ml_classification_regression/`

### Lab04 - 身高体重相关性分析
- **技术**：SciPy, Pandas, Matplotlib, Seaborn
- **内容**：
  - Shapiro-Wilk正态性检验
  - Pearson相关分析
  - Spearman秩相关分析
  - 数据可视化
- **文件**：`lab04_height_weight_correlation/`

## 运行环境
```bash
pip install pandas numpy scikit-learn scipy matplotlib seaborn
```

## 目录结构
```
├── lab01_student_score_analysis/
│   ├── student_analysis.py
│   ├── student_info.csv
│   └── 实验报告.md
├── lab02_feature_engineering/
│   ├── missing_values.py
│   ├── 特征编码.py
│   ├── 特征缩放.py
│   ├── 特征选择.py
│   ├── 特征离散化.py
│   └── ...
├── lab03_ml_classification_regression/
│   ├── iris_knn_classification.py
│   ├── wine_linear_regression.py
│   └── 实验报告.md
└── lab04_height_weight_correlation/
    ├── height_weight_analysis.py
    ├── height_weight_scatter.png
    ├── 实验报告.md
    └── problem/
```

---
**作者**：liem
**语言**：Python 3.13
**库**：Pandas, scikit-learn, SciPy, Matplotlib
