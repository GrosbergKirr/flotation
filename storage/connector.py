import pandas as pd
from sqlalchemy import create_engine


def connectToDb(cfg, log):
    engine = create_engine(f"postgresql+psycopg2://{cfg.user}:{cfg.password}@{cfg.host}:{cfg.port}/{cfg.dbname}")

    try:
        with engine.connect():
            log.info("Connected to database successfully")
    except Exception as e:
        log.error(f"Failed to connect to database: {str(e)}")

    return engine


def fetch_all_to_dataframe(engine, table_name, log):
    try:
        # Используем Pandas для выполнения SQL-запроса и получения данных
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, engine)
        log.info("read data successfully")
        return df
    except Exception as e:
        log.error("Failed to connect to database: ", e)
        return None
