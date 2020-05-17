def massHTMLParse(baseDirectory, folderDepth, sections, baseURL, rename = False, test=False):

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

    print(len(files))

    errors = []
    for filename in files:
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        try:
            for section in sections:
                if type(section) == tuple:
                    print(type(section[0]))
                    if (type(section[0]) == int):
                        selectStart = section[0]
                    elif (type(section[0]) == str):
                        selectStart = 0
                        for line in original_html:
                            selectStart += 1
                            if re.search(section[0], line):
                                res = re.search(section[0], line)
                                print(f"{res.group(0)}")
                                break
                    if (type(section[1]) == int):
                        selectEnd = section[1]
                    elif (type(section[1]) == str):
                        selectEnd = 0
                        for line in original_html:
                            selectEnd += 1
                            if re.search(section[1], line):
                                res = re.search(section[1], line)
                                print(f"{res.group(0)}")
                                break
                    print(f"{selectStart}, {selectEnd}")
                    new_html.append(original_html[selectStart:selectEnd])
                else:
                    new_html.append(section)
        except ValueError:
            errors.append(filename)
            continue
        if rename == True:
            newname = filename.split("\\")
            nf = codecs.open(f"{newname[-2]}.html", "w", encoding='UTF-8')
            # print(f"newfile")
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
                # nf.write('\n')
            nf.close()
        elif rename == False:
            with codecs.open(filename, "w", encoding='UTF-8') as nf:
                for line in new_html:
                    if type(line) == list:
                        for line in line:
                            nf.write(line)
                    else:
                        nf.write(line)
                # nf.write('\n')
            nf.close()
        if test == True:
            break
    print(f"{len(errors)}")
    commands = []
    

    for error in errors:
        commands.append(f"wayback_machine_downloader {baseURL}{error[1:-10]} --exact-url --to {error[2:5]}{int(error[5]) + 1}")

    f = open("commands.txt", "w")
    for entry in commands:
        f.write(entry)
        f.write('\n')
    f.close()
    


def massHTMLScriptRemoval(baseDirectory, folderDepth, baseURL, test=False):

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
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        print(filename)
        middle_html = "".join(original_html)
        script = '<script(.*?)<\/script>'
        new_html = re.sub(script, "", middle_html, flags=re.DOTALL)
        # new_html = middle_html
        # for scripts in script_array:
        #     new_html = re.split(scripts, new_html)
        print(new_html)
        with codecs.open(filename, "w", encoding='UTF-8') as nf:
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
            # nf.write('\n')
        nf.close()
        if test == True:
            break


def massHTMLStylesheetReplace(baseDirectory, folderDepth, baseURL, test=False):

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
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        middle_html = "".join(original_html)
        stylesheet_old = 'rel="stylesheet"(.*?)\/>'
        if folderDepth == 1:
            stylesheet_new = f'rel="stylesheet" href="./styles.css" type="text/css" media="screen" />'
        else:
            stylesheet_new = f'rel="stylesheet" href="{"../" * (int(folderDepth))}styles.css" type="text/css" media="screen" />'
        new_html = re.sub(stylesheet_old, stylesheet_new, middle_html, flags=re.DOTALL)
        with codecs.open(filename, "w", encoding='UTF-8') as nf:
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
            # nf.write('\n')
        nf.close()
        if test == True:
            break
        
def massHTMLStyleRemoval(baseDirectory, folderDepth, baseURL, test=False):

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
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        middle_html = "".join(original_html)
        styles_block = '<style(.*?)<\/style>'
        styles_inline = 'style="(.*?);"'
        new_html = re.sub(styles_block, "", middle_html, flags=re.DOTALL)
        new_html = re.sub(styles_inline, "", new_html, flags=re.DOTALL)
        with codecs.open(filename, "w", encoding='UTF-8') as nf:
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
            # nf.write('\n')
        nf.close()
        if test == True:
            break


def massHTMLIMGLink(baseDirectory, folderDepth, baseURL, test=False):

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

    urls = []
        
    for filename in files:
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        middle_html = "".join(original_html)
        src = 'src="(.*?)"'
        new_html = re.findall(src, middle_html, flags=re.DOTALL)
        for entry in new_html:
            urls.append(entry)
        if test == True:
            break

    f = open("links.txt", "w")
    for entry in urls:
        f.write(entry)
        f.write('\n')
    f.close()

def massHTMLSRCupdate(baseDirectory, folderDepth, baseURL, test=False):

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
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        middle_html = "".join(original_html)
        src_old_one = 'src="(.*?)//'
        src_old_two = 'src=\'(.*?)//'
        if folderDepth == 1:
            src_new_one = f'src="./assets'
            src_new_two = f'src=\'./assets'
        else:
            src_new_one = f'src="{"../" * (int(folderDepth))}'
            src_new_two = f'src=\'{"../" * (int(folderDepth))}'
        middle_middle_html = re.sub(src_old_one, src_new_one, middle_html, flags=re.DOTALL)
        new_html = re.sub(src_old_two, src_new_two, middle_middle_html, flags=re.DOTALL)
        with codecs.open(filename, "w", encoding='UTF-8') as nf:
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
            # nf.write('\n')
        nf.close()
        if test == True:
            break

def massHTMLSelfRefrence(baseDirectory, folderDepth, baseURL, test=False):

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
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        middle_html = "".join(original_html)
        old_pointer_one = 'http://mybestofbothworlds.com/w'
        old_pointer_two = 'http://mybestofbothworlds.com/2'
        if folderDepth == 1:
            new_pointer_one = f'./mybestofbothworlds.com/w'
            new_pointer_two = f'./2'
        else:
            new_pointer_one = f'{"../" * (int(folderDepth))}mybestofbothworlds.com/w'
            new_pointer_two = f'{"../" * (int(folderDepth))}2'
        middle_middle_html = re.sub(old_pointer_one, new_pointer_one, middle_html, flags=re.DOTALL)
        new_html = re.sub(old_pointer_two, new_pointer_two, middle_middle_html, flags=re.DOTALL)
        with codecs.open(filename, "w", encoding='UTF-8') as nf:
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
            # nf.write('\n')
        nf.close()
        if test == True:
            break


def removeTags(baseDirectory, folderDepth, baseURL, test=False):
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
        original_html = []
        new_html = []
        with codecs.open(filename, "r", encoding='UTF-8', errors='ignore') as f:
            for line in f.readlines():
                original_html.append(line)
        f.close()
        middle_html = "".join(original_html)
        old_pointer_one = '<span class="tags">(.*?)<\/span>'
        new_pointer_one = ''
        new_html = re.sub(old_pointer_one, new_pointer_one, middle_html, flags=re.DOTALL)
        # new_html = re.sub(old_pointer_two, new_pointer_two, middle_middle_html, flags=re.DOTALL)
        with codecs.open(filename, "w", encoding='UTF-8') as nf:
            for line in new_html:
                if type(line) == list:
                    for line in line:
                        nf.write(line)
                else:
                    nf.write(line)
            # nf.write('\n')
        nf.close()
        if test == True:
            break

# delete styles
# delete style="\W\A[1]"
