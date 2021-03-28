import os


def summarize():
    sites = list()
    with open('README.md', 'w') as f:
        filenames = os.listdir('./')
        for filename in filenames:
            if filename == 'template':
                continue
            if os.path.isdir(filename):
                sites.append(filename)

            print(filename)
            print(os.path.isdir(filename))


if __name__ == '__main__':
    summarize()

    pass
