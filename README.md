## PNAServer_VXI11

通过 VXI11 协议实现 PNA 矢量网络分析仪的虚拟网络通信服务器，启动服务器后可以通过 VISA 的 Measurement 软件连接并进行部分指令的虚拟通信。



### 依赖

本项目在 [https://github.com/sonium0/pyvxi11server](https://github.com/sonium0/pyvxi11server) 的基础上开发，并把代码移植到 Python3

环境依赖：

- Linux 操作系统
- rpcbind 软件
- Python3



### 使用说明

#### 设置输出 debug 信息（可选）

打开 `logger.py` 文件，找到最上面的全局变量 `Debug`，修改赋值即可

#### 启动服务器

- 脚本启动

  直接运行

  ```bash
  bash startPNAServer.sh
  ```

  来启动服务器

- 分步启动

  1. 启动 rpcbind

     使用
     ```bash
     ps -aux | grep rpcbind
     ```
     查看 rpcbind 是否以 `rpcbind -i` 启动

     如果没有看到输出信息或者不是以 `-i` 的方式启动的，请使用 `kill` 命令杀掉进程（假如你有自己的 rpc 进程，请酌情操作）

     使用命令
     ```bash
     rpcbind -i
     ```
     启动 rpcbind

  2. 启动服务器

     使用命令
     ```bash
     python3 main.py
     ```
     启动服务器

#### 连接服务器并使用

接下来就可以使用你的 VISA 来连接服务器了（也可以使用 Measurement 软件连接使用）

连接后就可以使用 SCPI 指令与服务器进行交互了



### 结构说明

- vxi11server.py

  这个文件是在 [https://github.com/sonium0/pyvxi11server](https://github.com/sonium0/pyvxi11server) 项目的同名文件的基础上移植修改而来的，把原先的 python2 环境换成了 python3 环境

- logger.py

  这个是用来统一输出日志信息的文件，通过这个文件的全局变量 `logger` 即可统一输出日志信息

- algorithm.py

  这个文件包含了一些需要用到的算法

- PNAParser.py

  这个文件定义了一个 PNAParser 类，通过这个类的 `parse` 函数即可为特定的 SCPI 指令进行解析和执行，最后返回结果

  可以通过修改这个类的实现来输出个性化的内容

- PNAServer.py

  这个文件定义了一个 PNAServer 类，它实现了最基本的 PNA 矢量网络分析仪的服务器框架，通过 vxi11 协议与客户指令通信，通过 PNAParser 类进行指令的解析和反馈

  不建议修改这个文件

- main.py

  此文件是服务器的启动入口，请直接使用 `python3 main.py` 启动服务器

  可以修改此文件以实现个性化的使用