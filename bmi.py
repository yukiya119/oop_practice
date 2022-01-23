"""
class BMI*:
    関連する属性:
        - 身長(m)
        - 体重(kg)
        - BMIという値そのもの
    ルール:
        - BMIは22が適正 10以上40以下の範囲 <-常識的な範囲
        - 表示する時は小数点第2位まで
            - eg: 23.689 => 23.69
            - eg: 23.681 => 23.68
    できること:
        - BMIの計算
"""


class BMI:
    def __init__(self, height_m, weight_kg):
        self.value = weight_kg / height_m ** 2
        if not (10 <= self.value <= 40):
            raise ValueError(f"BMIが正常範囲を外れていますぜ!!!{self.value}")

    def __str__(self):
        return f"{self.value:.2f}"  # 小数点第2位まで表示（第3位以下を四捨五入)


# BMIクラスのインスタンス化
yukiya = BMI(height_m=1.73, weight_kg=73)
print(yukiya)
