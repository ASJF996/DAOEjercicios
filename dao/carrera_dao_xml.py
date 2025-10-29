import xml.etree.ElementTree as ET

class carreraDAOXML:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_all_users(self):
        users = []
        try:
            tree = ET.parse(self.filepath)
            root = tree.getroot()
            for user in root.findall("user"):
                user_id = user.find("id").text
                name = user.find("name").text
                users.append({"id": user_id, "name": name})
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.filepath}")
        except ET.ParseError:
            print(f"Error al parsear el XML: {self.filepath}")
        return users