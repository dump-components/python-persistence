from system.operation_system import OperationSystem

storage_path = OperationSystem().directory.storage.value

class PersistenceBinaryFiles:
    
    def __init__(self, binary_files: list) -> None:
        if isinstance(binary_files, list):
            self.__files = list(binary_files)
            self.persist_files()
        else:
            raise ValueError("PersistenceBinaryFiles aceita apenas uma lista de tuplas com (nome_do_arquivo, binario_do_arquivo)")
    
    def persist_files(self):
        for file in self.__files:
            name_file, binary_file = file
            self.__create_file(name_file, binary_file)
    
    def __create_file(self, name, binary):
        try:
            with open(storage_path + name, "wb") as file:
                file.write(binary)
        except Exception as err:
            raise err