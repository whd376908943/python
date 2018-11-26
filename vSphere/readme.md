vm.py 包含在 vSphere 从模板克隆虚拟机 及 初始化虚拟机(设置ip、重启网络) 两个阶段

传参样例:
args = {
        'host': vip,                              # vSphere ip, or ESXI ip
        'user': user,                             # 用户名
        'password': password,                     # 密码
        'vm_name': vm_name,                       # 虚拟机名称
        'vm_user': vm_user,                       # 虚拟机用户名 ex: root
        'vm_pwd': vm_pwd,                         # 虚拟机密码
        'template': template,                     # 指定从该模板克隆虚拟机
        'resource_pool': resource_pool,           # 指定虚拟机建立在该资源池下
        'datastore_name': datastore_name,         # 指定虚拟机存储在该存储下
        'path_to_program': path_to_program,       # 指定在虚拟机上执行的程序
        'program_arguments': program_arguments    # 指定在虚拟机上执行程序时传入的参数     
    }


