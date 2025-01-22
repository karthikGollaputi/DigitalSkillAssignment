class FileUtils:


    @staticmethod
    def read_file(filepath, filemode):
        with open(filepath, filemode) as f:
            data = f.readlines()
        return data

