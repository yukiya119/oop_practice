"""
データ型の宣言: UserName
    属性:
        実際のユーザー名:
    ルール:
        ユーザー名は4文字以上20文字以内である
    できること:
        ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        # nameのチェック処理
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}はルール違反です')
        self.name = name  # インスタンス化したことで、「名前」が必須項目化されたらしい

    # 大文字にする処理
    def battle_name(self):
        return self.name.upper()


bob = UserName(name='Bob Smith')
print(bob.name)
print(bob.battle_name())
