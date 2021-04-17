import os


def summarize():
    sites = ['acmicpc', 'ctci', 'etc', 'leetcode', 'programmers', 'projecteuler']

    with open('README.md', 'w') as f:
        f.write('# Algorithm Practice\n')
        for site in sites:
            f.write(f'## {site}\n')
            if site == 'projecteuler':
                num_problem = 755  # 2021/04/18 update
                ps = [i for i in range(1, num_problem + 1)]
                ps = [' | '.join(map(str, ps[i * 10:i * 10 + 10])) for i in range(num_problem // 10 + 1)]
                f.write("""| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
""")
                for p in ps:
                    f.write(f'| {p} |\n')
                # print('\n'.join(ps))

            path = os.walk(f"./{site}")
            for root, directories, files in path:
                print('directories', directories)
                print('files', files)
                for filename in sorted(files,
                                       key=lambda x: int(x.split('.')[0]) if x.count('.') > 1 else 0):
                    ext = os.path.splitext(filename)[-1]
                    if ext == '.py':
                        print(root, filename)

                        f.write(f'[{filename[:-3]}]({root}/{filename})\n\n')
        # for directory in directories:
        #     print(directory)
        #     if directory in dir_exception:
        #         continue
        # for file in files:
        #     print(file)


if __name__ == '__main__':
    summarize()

    pass
