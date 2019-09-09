"""此模块用于统计游戏信息"""
import json

class Gamestats():
    """统计游戏信息的类"""
    def __init__(self,ai_setting):
        """初始化统计信息"""
        self.ai_setting = ai_setting
        #在方法recet_stats中初始化大部分统计方法
        self.reset_stats()
        #游戏启动处于活跃状态
        self.game_active = False
        #在任何情况下都不应重置最高得分
        self.filename = 'high_score.json'
        self.high_score = self.load_high_score()
        
        
    
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_setting.ship_limt
        self.score = 0
        self.level = 1

    def dump_high_score(self):
        """将最高得分存储在文件里"""
        with open(self.filename,'w') as f_obj:
            json.dump(self.high_score,f_obj)

    def load_high_score(self):
        """读取最高得分"""
        try:
            with open(self.filename) as f_obj:
                high_score = json.load(f_obj)
                
        except FileNotFoundError:
            self.dump_high_score()

        return high_score

       
        

        

            
        
    
