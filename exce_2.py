class Filehandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, 'w')   
        
    def write_data(self, data):
        return self.file.write(data)
    
    def __del__(self):
        closing = input(f"Are are sure you want to delet {self.file_name}? (y/n) ").lower()
        if closing == "y":
            self.file.close()
            print(f"{self.file_name} is closed")
        else:
            pass
        
file = Filehandler("index.txt")
file.write_data("Hello Word")
        
     
        
    
        