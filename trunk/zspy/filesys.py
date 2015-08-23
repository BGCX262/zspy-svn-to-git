def filename(name,suffix=''):
    name=name.replace('<','(').replace('>',')')
    for i in '\/:*?"|':
        name=name.replace(i,'_')
    if suffix:
        suffix='.'+suffix
    name=name[:255-len(suffix)]+suffix
    return name

def makedirs(directory):
    from os.path import exists
    if exists(directory):
        return
    else:
        from os import makedirs
        makedirs(directory)

def merge(file_path,output,suffix="",delimiter="\n-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~\n\n"):
    from os.path import dirname
    makedirs(dirname(output))
    length=len(suffix)
    output=open(output,'w')
    for path in file_path:
        if length==0 or path[-length:]==suffix:
            input=open(path)
            output.write(input.read())
            input.close()
            output.write(delimiter)
    output.close()