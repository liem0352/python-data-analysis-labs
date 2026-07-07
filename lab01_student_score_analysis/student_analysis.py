import pandas as pd
import numpy as np
import random

class StudentDataProcessor:
    """
    学生数据处理类，负责学生数据的生成、存储、读取和筛选
    """
    
    # 更真实的中文姓名列表
    CHINESE_NAMES = [
        '张伟', '李娜', '王芳', '刘洋', '陈静',
        '王明', '李阳', '王强', '张丽', '李明'
    ]
    
    # 科目名称列表
    SUBJECTS = ['高等数学', '大学英语', '体育', '高级语言']
    
    def __init__(self, seed=42):
        """
        初始化处理器
        
        Args:
            seed: 随机种子，用于确保结果可复现
        """
        self.seed = seed
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_student_data(self, num_students=10):
        """
        生成学生数据
        
        Args:
            num_students: 学生数量
            
        Returns:
            pandas.DataFrame: 包含学生信息和成绩的DataFrame
        """
        # 随机选择学生姓名，确保不重复
        selected_names = random.sample(self.CHINESE_NAMES, min(num_students, len(self.CHINESE_NAMES)))
        
        # 生成各科成绩（60-100分之间的随机分数）
        data = {'学生姓名': selected_names}
        for subject in self.SUBJECTS:
            data[subject] = np.random.randint(60, 101, size=len(selected_names))
        
        # 创建并返回DataFrame
        return pd.DataFrame(data)
    
    def save_to_csv(self, df, filename='student_info.csv'):
        """
        保存数据到CSV文件
        
        Args:
            df: 要保存的DataFrame
            filename: 文件名
        """
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f" 数据已成功保存到 {filename}")
    
    def load_from_csv(self, filename='student_info.csv'):
        """
        从CSV文件加载数据
        
        Args:
            filename: 文件名
            
        Returns:
            pandas.DataFrame: 加载的DataFrame
        """
        return pd.read_csv(filename, encoding='utf-8-sig')
    
    def filter_excellent_students(self, df, threshold=80):
        """
        筛选各科成绩均达到指定分数线以上的学生
        
        Args:
            df: 包含学生数据的DataFrame
            threshold: 分数线，默认为80分
            
        Returns:
            pandas.DataFrame: 符合条件的学生数据
        """
        # 筛选出所有成绩列
        score_columns = [col for col in df.columns if col != '学生姓名']
        
        # 筛选各科成绩均≥threshold的学生
        mask = (df[score_columns] >= threshold).all(axis=1)
        return df[mask].reset_index(drop=True)
    
    def display_student_info(self, df, title="学生信息"):
        """
        美观地显示学生信息
        
        Args:
            df: 学生数据
            title: 显示标题
        """
        print(f"\n{'='*30}")
        print(f"{title:^30}")
        print(f"{'='*30}")
        print(df)
        print(f"{'='*30}\n")


def main():
    """
    主函数，展示学生数据处理流程
    """
    # 创建数据处理器实例
    processor = StudentDataProcessor(seed=42)
    
    # 1. 生成学生数据
    print(" 正在生成学生数据...")
    student_data = processor.generate_student_data(num_students=10)
    processor.display_student_info(student_data, "生成的学生数据")
    
    # 2. 保存数据到CSV
    csv_file = 'student_info.csv'
    processor.save_to_csv(student_data, csv_file)
    
    # 3. 从CSV读取数据
    print(f" 正在从 {csv_file} 读取数据...")
    loaded_data = processor.load_from_csv(csv_file)
    processor.display_student_info(loaded_data, "读取的学生数据")
    
    # 4. 筛选优秀学生
    threshold = 80
    print(f" 筛选各科成绩均在{threshold}分以上的学生...")
    excellent_students = processor.filter_excellent_students(loaded_data, threshold)
    
    if not excellent_students.empty:
        print(f" 找到 {len(excellent_students)} 名优秀学生！")
        
        # 显示优秀学生名单
        print("\n 优秀学生名单：")
        print(excellent_students[['学生姓名']])
        
        # 显示优秀学生详细成绩
        processor.display_student_info(excellent_students, "优秀学生详细成绩")
    else:
        print(f" 没有找到各科成绩均在{threshold}分以上的学生")


if __name__ == "__main__":
    main()