import yaml

class DatabaseConfig:
    def __init__(self, user, password, host, port, dbname):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __repr__(self):
        return (f"DatabaseConfig(dbname={self.dbname}, user={self.user}, "
                f"password={self.password}, host={self.host}, port={self.port})")

class ServiceConfig:
    def __init__(self, logLevel, interval):
        self.logLevel = logLevel
        self.interval = interval

    def __repr__(self):
        return f"ServiceConfig(logLevel={self.logLevel}, interval={self.interval})"

class Config:
    def __init__(self, database_config, service_config):
        self.database = database_config
        self.service = service_config

    def __repr__(self):
        return f"Config(database={self.database}, service={self.service})"

# Функция для загрузки конфигурации из YAML файла и создания экземпляра класса Config
def LoadConfig(file_path):
    try:
        with open(file_path, 'r') as file:
            config_data = yaml.safe_load(file)

            # Создаем объекты конфигураций для базы данных и сервиса
            db_config = DatabaseConfig(**config_data['db'])
            service_config = ServiceConfig(**config_data['service'])
            print("Считали конфиг")
            # Возвращаем объект Config с двумя секциями
            return Config(db_config, service_config)
    except Exception as e:
        print(f"Ошибка при чтении конфигурации: {e}")
        return None


