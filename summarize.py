import os


def summarize():
    sites = ['samsung', 'ctci', 'etc', 'leetcode', 'programmers']

    with open('README.md', 'w') as f:
        f.write('# Algorithm Practice\n')
        for site in sites:
            f.write(f'## {site}\n')
            path = os.walk(f"./{site}")
            for root, directories, files in path:
                print('directories', directories)
                print('files', files)
                for filename in files:
                    ext = os.path.splitext(filename)[-1]
                    if ext == '.py':
                        print(root, filename)

                        f.write(f'[{filename}]({root})\n\n')
        # for directory in directories:
        #     print(directory)
        #     if directory in dir_exception:
        #         continue
        # for file in files:
        #     print(file)


if __name__ == '__main__':
    summarize()

    pass
