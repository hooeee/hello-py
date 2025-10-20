import argparse


class InputArgsResult:
    def __init__(self, file_path: str, context: str):
        self.file_path = file_path
        self.context = context

class InputArgs:
    def __init__(self, ):
        pass

    def get_args(self) -> InputArgsResult:
        parser = argparse.ArgumentParser(description="git Jandi Commit CLI Tool")

        parser.add_argument("file_path", help="파일 경로")
        parser.add_argument("context", help="커밋 컨텍스트")
        args = parser.parse_args()
        return InputArgsResult(args.file_path, args.context)
