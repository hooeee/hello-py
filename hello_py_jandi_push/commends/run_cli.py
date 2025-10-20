import subprocess

class RunCli:
    def __init__(self):
        pass

    def excute(self, cmd):
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ {cmd[1]} 실패: {result.stderr}")
        else:
            print(f"✅ {cmd[1]} 성공")