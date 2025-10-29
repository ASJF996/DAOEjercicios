import json
from dao.estudiante_dao_SQLserver import EstudianteDAOSQLserver 

def get_daos_from_config(config_path="config.json"):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    dao_type = config.get("dao_type", "").lower()

    if dao_type == "sqlserver":
        sql_conf = config.get("SQLserver", {})
        return EstudianteDAOSQLserver(
            server=sql_conf.get("server"),
            username=sql_conf.get("name"),
            password=sql_conf.get("password"),
            database=sql_conf.get("database")
        )
   
    else:
        raise ValueError(f"Tipo de DAO desconocido: {dao_type}")