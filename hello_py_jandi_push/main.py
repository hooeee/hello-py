import random
from datetime import date, datetime

from argments import InputArgs
from commends import RunCli

if __name__ == '__main__':
    args = InputArgs().get_args()
    print(args.file_path, args.context)

    cli_executor = RunCli()

    for i in range(random.randint(1, 4)):
        with open(args.file_path, "a", encoding="utf-8") as f:
            f.write(f"\n {datetime.now().isoformat()}")

        cli_executor.excute(["git", "add", "."])
        cli_executor.excute(["git", "commit", "-m", "update : auto commit"])
        print("commit 완료")

    cli_executor.excute(["git", "push"])