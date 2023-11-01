

import winreg as reg
import ctypes

def add_to_registry():
    # 获取当前脚本的路径
    script_path = "C:\\path\\to\\your\\script.py"

    # 打开注册表项
    key_path = r"Directory\\Background\\shell\\YourCustomTool"
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)

    # 设置右键菜单显示的名称
    reg.SetValue(key, "", reg.REG_SZ, "Your Custom Tool")

    # 创建命令项
    command_key_path = key_path + "\\command"
    command_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key_path)

    # 设置命令项的默认值为脚本的路径
    reg.SetValue(command_key, "", reg.REG_SZ, f'pythonw.exe "{script_path}"')

    # 关闭注册表项
    reg.CloseKey(key)
    reg.CloseKey(command_key)

    # 刷新资源管理器
    ctypes.windll.shell32.SHChangeNotify(ctypes.c_ulong(0), ctypes.c_ulong(0), None, None, ctypes.c_ulong(0))

if __name__ == "__main__":
    add_to_registry()