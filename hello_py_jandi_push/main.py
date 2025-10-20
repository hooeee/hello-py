from argments import InputArgs

if __name__ == '__main__':
    args = InputArgs().get_args()
    print(args.file_path, args.context)