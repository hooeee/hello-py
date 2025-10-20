from datetime import date, datetime

from argments import InputArgs
from commends import RunCli

if __name__ == '__main__':
    args = InputArgs().get_args()
    print(args.file_path, args.context)


    with open(args.file_path, "a", encoding="utf-8") as f:
        f.write(f"\n {datetime.now().isoformat()}")


    cli_executor = RunCli()
    cli_executor.excute(["git", "add", "."])
    cli_executor.excute(["git", "commit", "-m", "update : auto commit"])
    # cli_executor.excute(["git", "push"])
    #
    # # git 명령 실행 함수
    # def run_git(cmd):
    #     result = subprocess.run(cmd, capture_output=True, text=True)
    #     if result.returncode != 0:
    #         print(f"❌ {cmd[1]} 실패: {result.stderr}")
    #     else:
    #         print(f"✅ {cmd[1]} 성공")
    #
    #
    # # git add, commit, push
    # run_git(["git", "add", args.filename])
    # run_git(["git", "commit", "-m", f"update: {args.filename}"])
    # run_git(["git", "push"])