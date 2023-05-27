class Config:
    def __init__(self, env):
        self.env = env
        self.load_config()

    def load_config(self):
        if self.env == "qa":
            # 讀取qa.toml並序列化為config物件
            with open("qa.toml", "r") as f:
                config_data = toml.load(f)
            # 執行設定檔初始化
            # ...

        elif self.env == "local":
            # 讀取local.toml並序列化為config物件
            with open("local.toml", "r") as f:
                config_data = toml.load(f)
            # 執行設定檔初始化
            # ...

        # 將config_data轉換為config物件
        self.config = ConfigObject(config_data)