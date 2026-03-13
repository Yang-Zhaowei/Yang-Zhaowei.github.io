import json
import os

def generate_resume():
    # 1. 定义你的简历数据 (只需修改这里)
    resume_data = {
        "en": {
            "name": "Yang Zhaowei",
            "location": "Location: Anhui, China",
            "email": "Email: yangzw_@outlook.com",
            "phone": "Phone: +86 18101372898",
            "github": "GitHub: github.com/Yang-Zhaowei",
            "linkedin": "LinkedIn: None",
            "education": [
                {
                    "institution": "Beihang University",
                    "degree": "Master of Computer Technology",
                    "date": "2019 - 2022",
                    "description": "GPA: 3.72/4.0, Outstanding Graduate of Beijing in 2022;Graduation Thesis: Frequency Domain Analysis of Adversarial Signals for Deep Neural Network"
                },
                {
                    "institution": "Beijing University of Chemical Technology",
                    "degree": "Bachelor of Process Equipment and Control Engineering",
                    "date": "2015 - 2019",
                    "description": "GPA: 3.21/4.0, University Student Innovation: Vertical Multi-Row Bicycle Parking Device, Graduation Thesis: Research on Construction Methods of Safety Regulations and Case Knowledge Graph"
                },
                {
                    "institution": "No.1 High School of Luan Anhui",
                    "degree": "High School Diploma",
                    "date": "2012 - 2015",
                    "description": "Graduated with honors, Top 5% of class"
                }
            ],
            "experience": [
                {
                    "company": "China Computer Federation",
                    "position": "Software Developer Intern",
                    "date": "2021 - 2022",
                    "description": "Responsible for designing and improving the competition registration system, involved in the evaluation work of the National Olympiad in Informatics."
                },
                {
                    "company": "Zhongguang logistics Co., Ltd.",
                    "position": "Software Developer",
                    "date": "2023 - Now",
                    "description": "Responsible for the company's software development and participating in the company's intelligent logistics system transformation."
                }
            ]
        },
        "zh": {
            "name": "杨兆维",
            "location": "所在地：中国安徽省",
            "email": "邮箱：yangzw_@outlook.com",
            "phone": "电话：+86 18101372898",
            "github": "GitHub：github.com/Yang-Zhaowei",
            # "linkedin": "LinkedIn：linkedin.com/in/yangzhaowei",
            "linkedin": "LinkedIn：None",
            "education": [
                {
                    "institution": "北京航空航天大学",
                    "degree": "计算机技术硕士",
                    "date": "2019 - 2022",
                    "description": "GPA：3.72/4.0；计算机视觉方向；2022年北京市优秀毕业生；毕业论文：深度神经网络对抗信号的频域分析"
                },
                {
                    "institution": "北京化工大学",
                    "degree": "过程装备与控制工程学士",
                    "date": "2015 - 2019",
                    "description": "GPA: 3.21/4.0；大学生创新：立式多排自行车停放装置；毕业论文：安全法规与案例的知识图谱构建方法研究"
                },
                {
                    "institution": "安徽省六安第一中学",
                    "degree": "高中",
                    "date": "2012 - 2015",
                    "description": "班级前5%"
                }
            ],
            "experience": [
                {
                    "company": "中国计算机学会",
                    "position": "软件开发实习生",
                    "date": "2021-2022",
                    "description": "负责竞赛报名系统的设计和改进，参与全国青少年信息学奥赛的评测。"
                },
                {
                    "company": "中广物流有限公司",
                    "position": "软件开发",
                    "date": "2023 - 至今",
                    "description": "负责公司的软件开发，参与智能物流系统改造。"
                }
            ]
        }
    }

    # 2. 生成JSON文件
    with open('resume.json', 'w', encoding='utf-8') as f:
        json.dump(resume_data, f, ensure_ascii=False, indent=2)
    
    print("✅ Resume JSON generated successfully!")

if __name__ == "__main__":
    generate_resume()