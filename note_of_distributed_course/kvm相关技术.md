---
name: kvm相关技术.md
date: 2017-04-02
update: 2017-04-02
keywords: kvm libvirt ubuntu 虚拟机 虚拟机技术
---


什么是KVM？
----

```
Kernel-based Virtual Machine的简称，是一个开源的系统虚拟化模块；
它可以在不改变linux镜像的情况下，同时运行多个虚拟机，把linux内核转换成一个虚拟机监视器(Hypervisor);
```
[维基百科](https://zh.wikipedia.org/wiki/%E5%9F%BA%E4%BA%8E%E5%86%85%E6%A0%B8%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA)

[kvm wiki](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine)

[kvm百科](http://baike.baidu.com/link?url=VBJtn9Sfnh5Diap_0HXYYEzhrMcLyewXF8oWLVS-7An6CqQGfvO-JaDrVSp7wzFK92EjCW7zD4QO1aUj9CM-uGizDHDoh2lPgZvTu_GJ7rndpGbe6js1H5Hm6HSlL5ra)

[Hypervisor](https://zh.wikipedia.org/wiki/Hypervisor)

安装KVM准备
----

- 确定机器有VT（virtualization Tech）

    ```
    $ grep vmx /proc/cpuinfo
    ```

- 确保BIOS开启了VT

- 确保内核版本较新(2.6.20以上)，支持KVM
    ```
    $ uname -a
    ```

Ubuntu安装KVM
----
* 安装必要的包

    这些必要的包是安装虚拟机服务器版本(没有图形界面)的必要的包
    ```
    $ sudo apt-get install kvm qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils
    ```
    说明一下
    ```
    1.libvirt-bin提供libvirtd，可以用来管理qemu和kvm实例
    2.qemu-kvm是kvm的后端服务
    3.ubuntu-vm-builder为构建虚拟机提供强大的命令行工具
    4.bridge-utils为虚拟机和网卡之间提供网桥
    ```

* 添加用户到用户组

    使用下面命令把你当前用户添加到libvirtd和kvm用户组：
    ```
    $ sudo adduser `id -un` kvm
    $ sudo adduser `id -un` libvirtd
    ```

* 重启后验证是否安装成功

    使用下面这个命令来检测安装是否成功
    ```
    $ virsh list --all
    Id Name         State
    --------------------------

    $
    ```

* 虚拟机管理

    1.列出正在运行的虚拟机
    ```
    $ virsh list
    ```
    2.启动一个虚拟机
    ```
    $ virsh start web_devel
    ```
    3.在启动时开始一个虚拟机
    ```
    $ virsh autostart web_devel
    ```
    4.重启一个虚拟机
    ```
    $ virsh reboot web_devel
    ```
    5.将虚拟机的状态保存到文件中，一旦保存虚拟机将不再运行
    ```
    $ virsh save web_devel-170408.state
    ```
    6.唤醒经过保存的虚拟机
    ```
    $ virsh restore web_devel-170408.state
    ```
    7.关闭虚拟机
    ```
    $ virsh shutdown web_devel
    ```
    8.把CDROM设备挂载到虚拟机上面
    ```
    $ virsh attach-disk web_devel /dev/cdrom /media/cdrom
    ```


* 虚拟机管理器

    如果想要使用桌面环境，那么需要先安装virt-manager，virt-manager包含有一组图形化的程序用以管理本地和远程的虚拟机，
    输入下面命令进行安装virt-manager:
    ```
    $ sudo apt-get install virt-manager
    ```
    链接到本地libvirt服务：
    ```
    $ virt-manager -c qemu:///system
    ```
    如果想要链接到另一台计算机上面的libvirt服务，可以使用下面的命令：
    ```
    $ virt-manager -c qemu+ssh://virtnode1.mydomain.com/system
    ```
    上面的命令是假设你已经设置好ssh管理和virtnode1.domain.com的连通，更多细节设置参看[OpenSSH服务器](https://help.ubuntu.com/lts/serverguide/openssh-server.html)


* 虚拟机查看器

    virt-viewer程序可以链接到虚拟机，运行virt-viewer需要虚拟机支持图形界面；
    安装virt-viewer命令：
    ```
    $ sudo apt-get install virt-viewer
    ```
    运行虚拟机后，使用下面命令到控制台：
    ```
    $ virt-viewer web_devel
    ```
    和virt-manager相似，virt-viewer也可以通过授权ssh远程链接到远方主机:
    ```
    $ virt-viewer -c qemu+ssh://virtnode1.mydomain.com/system web_devel
    ```

* 参考链接

    [KVM installation - ubuntu help](https://help.ubuntu.com/community/KVM/Installation)

    [libvirt - ubuntu help](https://help.ubuntu.com/lts/serverguide/libvirt.html)


了解QEMU
----
qemu是一个开源的hosted hypervisor,配合kvm一起使用，虚拟机的运行速度可以达到原生硬件的运行速度；
详细的可以查看相关的wiki链接：[qemu wiki](https://en.wikipedia.org/wiki/QEMU)

可看qemu相关网站：[qemu-project.org](http://wiki.qemu-project.org/Features/KVM)


vncviewer是什么？
----

```
Virtual Network Computing（VNC）是一个远程系统，允许你和网络上的另一台计算机的虚拟桌面进行交互；
使用VNC，你可以运行图形界面应用，并在你本地上面显示；VNC的客户端和服务端都支持多个操作系统；
```
下载网址[https://github.com/TigerVNC/tigervnc/releases](https://github.com/TigerVNC/tigervnc/releases)

