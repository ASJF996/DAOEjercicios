import json
from dao.carrera_dao_SQLserver import CarreraDAOSQLserver
from dao.carrera_dao_txt import CarreraDAOTxt
from dao.carrera_dao_xml import carreraDAOXML
from dao.carrera_dao_xlsx import CarreraDAOXLSX  # 👈 Importación agregada

def get_dao_from_config(config_path="config.json"):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    dao_type = config.get("dao_type", "").lower()

    if dao_type == "sqlserver":
        sql_conf = config.get("SQLserver", {})
        return CarreraDAOSQLserver(
            server=sql_conf.get("server"),
            username=sql_conf.get("name"),
            password=sql_conf.get("password"),
            database=sql_conf.get("database")
        )
   
    elif dao_type == "txt":
        return CarreraDAOTxt(config["txt"]["filepath"])

    elif dao_type == "xml":
        return carreraDAOXML(config["xml"]["filepath"])

    elif dao_type == "excel":  
        excel_conf = config.get("excel", {})
        return CarreraDAOXLSX(excel_conf.get("filepath"))

    else:
        raise ValueError(f"Tipo de DAO desconocido: {dao_type}")