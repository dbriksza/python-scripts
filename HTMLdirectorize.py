def massHTMLDirectorize(baseDirectory, folderDepth, newDirectories, test=False):

    import os
    import re
    import codecs

    files = []

    for dirname, dirnames, filenames in os.walk(baseDirectory):
        #specify how many directories deep to get files
        if (dirname[len(baseDirectory):].count(os.sep) > folderDepth - 1) & (dirname[len(baseDirectory):].count(os.sep) < folderDepth + 1):

            for filename in filenames:
                if ".git" not in dirname:
                    files.append(os.path.join(dirname, filename))

    for filename in files:
        directory = []
        original_html = []
        with codecs.open(filename, "r", encoding='UTF-8') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        for newDirectory in newDirectories:
            if type(newDirectory) == tuple:
                # print(type(newDirectory[0]))
                if (type(newDirectory[0]) == int):
                    selectLine = newDirectory[0]
                elif (type(newDirectory[0]) == str):
                    selectLine = 0
                    for line in original_html:
                        selectLine += 1
                        if line.find(newDirectory[0]) != -1:
                            # print(line)
                            break
                    selectStart = original_html[selectLine - 1].find(newDirectory[0]) + len(newDirectory[0]) + newDirectory[1]
                    selectEnd = original_html[selectLine - 1].find(newDirectory[0]) + len(newDirectory[0]) + newDirectory[2]
                    directory.append(str(original_html[selectLine - 1])[selectStart:selectEnd])
            else:
                directory.append(newDirectory)
        name_of_file = filename.split('\\')[-1]
        file_no_extension = name_of_file.split('.')[0]
        file_file = os.path.join('.', *directory, file_no_extension, 'index.html')
        file_path = os.path.join('.', *directory, file_no_extension)
        print(file_path)
        print(file_path)
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        with codecs.open(file_file, "w", encoding='UTF-8') as file:
            for line in original_html:
                if type(line) == list:
                    for line in line:
                        if re.match(r'^\s*$', line):
                            continue
                        file.write(line)
                else:
                    if re.match(r'^\s*$', line):
                        continue
                    file.write(line)
            # nf.write('\n')
        file.close()
        if test == True:
            break
