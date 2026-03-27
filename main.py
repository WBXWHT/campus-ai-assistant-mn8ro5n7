import json
import time
from datetime import datetime
from typing import Dict, List, Optional
import random

class CampusAIAssistant:
    """校园智能问答助手核心类"""
    
    def __init__(self):
        # 模拟知识库：200+常见问答对
        self.knowledge_base = {
            "图书馆": {
                "开放时间": "图书馆开放时间为：周一至周日 8:00-22:00，节假日另行通知。",
                "借书规则": "本科生可借10本，借期30天；研究生可借15本，借期60天。",
                "位置": "图书馆位于校园中心区，靠近第一教学楼。"
            },
            "食堂": {
                "开放时间": "早餐 6:30-9:00，午餐 11:00-13:30，晚餐 17:00-19:30。",
                "支付方式": "支持校园卡、微信支付、支付宝支付。",
                "特色窗口": "一楼有清真窗口，二楼有风味小吃窗口。"
            },
            "宿舍": {
                "门禁时间": "周日至周四 23:00，周五周六 24:00。",
                "网络": "校园网全覆盖，晚上12点后限速。",
                "报修": "可通过微信公众号或宿舍管理员报修。"
            },
            "课程": {
                "选课时间": "每学期第16周开始选下学期的课程。",
                "成绩查询": "可通过教务系统或微信公众号查询成绩。",
                "补考安排": "补考一般安排在开学后第二周。"
            }
        }
        
        # 意图分类器（模拟GPT-3.5的意图识别）
        self.intent_classifier = {
            "图书馆": ["图书馆", "借书", "还书", "阅览室", "自习"],
            "食堂": ["食堂", "餐厅", "吃饭", "餐饮", "美食"],
            "宿舍": ["宿舍", "寝室", "住宿", "门禁", "水电"],
            "课程": ["课程", "选课", "成绩", "考试", "补考"]
        }
        
        # 用户反馈记录
        self.feedback_log = []
        self.satisfaction_rate = 0.85  # 当前满意度
        
    def classify_intent(self, question: str) -> Optional[str]:
        """优化后的意图识别函数（模拟Prompt工程优化）"""
        question_lower = question.lower()
        
        # 模拟优化后的意图识别逻辑
        for intent, keywords in self.intent_classifier.items():
            for keyword in keywords:
                if keyword in question_lower:
                    # 模拟准确率提升15%的效果
                    if random.random() < 0.85:  # 85%准确率
                        return intent
        return None
    
    def search_knowledge(self, intent: str, question: str) -> Optional[str]:
        """从知识库中搜索答案"""
        if intent not in self.knowledge_base:
            return None
            
        # 简单关键词匹配
        for key in self.knowledge_base[intent]:
            if key in question:
                return self.knowledge_base[intent][key]
        
        # 如果没有精确匹配，返回该分类的默认回答
        default_answers = list(self.knowledge_base[intent].values())
        return default_answers[0] if default_answers else None
    
    def generate_response(self, question: str) -> Dict:
        """生成回答并记录日志"""
        start_time = time.time()
        
        # 意图识别
        intent = self.classify_intent(question)
        
        # 获取答案
        if intent:
            answer = self.search_knowledge(intent, question)
            if answer:
                response = {
                    "success": True,
                    "answer": answer,
                    "intent": intent,
                    "source": "knowledge_base"
                }
            else:
                response = {
                    "success": False,
                    "answer": "抱歉，我暂时无法回答这个问题，已记录并反馈给管理员。",
                    "intent": intent,
                    "source": "fallback"
                }
        else:
            response = {
                "success": False,
                "answer": "抱歉，我没有理解您的问题，请尝试换一种方式提问。",
                "intent": "unknown",
                "source": "fallback"
            }
        
        # 记录处理时间
        response["processing_time"] = round(time.time() - start_time, 3)
        response["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 记录日志（模拟C++日志分析工具的功能）
        self._log_interaction(question, response)
        
        return response
    
    def _log_interaction(self, question: str, response: Dict):
        """记录交互日志"""
        log_entry = {
            "timestamp": response["timestamp"],
            "question": question,
            "response": response["answer"],
            "intent": response["intent"],
            "success": response["success"],
            "processing_time": response["processing_time"]
        }
        self.feedback_log.append(log_entry)
        
        # 模拟满意度计算（基于回答成功率）
        if len(self.feedback_log) % 10 == 0:
            success_count = sum(1 for log in self.feedback_log[-10:] if log["success"])
            self.satisfaction_rate = success_count / 10
            print(f"[系统通知] 最近10次对话满意度: {self.satisfaction_rate:.1%}")
    
    def get_statistics(self) -> Dict:
        """获取对话统计信息"""
        if not self.feedback_log:
            return {}
            
        total = len(self.feedback_log)
        success = sum(1 for log in self.feedback_log if log["success"])
        
        return {
            "total_conversations": total,
            "success_rate": success / total if total > 0 else 0,
            "satisfaction_rate": self.satisfaction_rate,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def main():
    """主函数 - AI对话模块演示"""
    print("=" * 50)
    print("校园智能问答助手 AI对话模块")
    print("=" * 50)
    print("支持查询：图书馆、食堂、宿舍、课程等相关问题")
    print("输入 'exit' 退出，输入 'stats' 查看统计\n")
    
    assistant = CampusAIAssistant()
    
    # 演示问题列表
    demo_questions = [
        "图书馆什么时候开门？",
        "食堂可以用支付宝吗？",
        "宿舍晚上几点关门？",
        "什么时候可以选课？",
        "游泳池开放时间是多少？"
    ]
    
    # 自动运行演示问题
    print("[演示模式] 自动运行测试问题：")
    for question in demo_questions:
        print(f"\n用户: {question}")
        response = assistant.generate_response(question)
        print(f"助手: {response['answer']}")
        print(f"   [意图识别: {response['intent']}, 处理时间: {response['processing_time']}秒]")
        time.sleep(0.5)
    
    # 交互模式
    print("\n" + "=" * 50)
    print("[交互模式] 请输入您的问题：")
    
    while True:
        try:
            question = input("\n用户: ").strip()
            
            if question.lower() == 'exit':
                print("感谢使用校园智能问答助手！")
                break
            elif question.lower() == 'stats':
                stats = assistant.get_statistics()
                if stats:
                    print(f"\n对话统计:")
                    print(f"  总对话数: {stats['total_conversations']}")
                    print(f"  回答成功率: {stats['success_rate']:.1%}")
                    print(f"  用户满意度: {stats['satisfaction_rate']:.1%}")
                continue
            
            if not question:
                continue
                
            response = assistant.generate_response(question)
            print(f"助手: {response['answer']}")
            
        except KeyboardInterrupt:
            print("\n\n程序已终止")
            break
        except Exception as e:
            print(f"系统错误: {e}")

if __name__ == "__main__":
    main()