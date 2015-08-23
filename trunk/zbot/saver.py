from env import Env
from zspy.filesys import makedirs
from os.path import dirname

def mako_render(template):
    def _mako_render(path,meta):
        makedirs(dirname(path))
        f=open(path,'w+')
        content=Env.get_template(template).render(**meta)
        f.write(content)
        try:
            print path
        except:
            pass
        f.close()
    return _mako_render


