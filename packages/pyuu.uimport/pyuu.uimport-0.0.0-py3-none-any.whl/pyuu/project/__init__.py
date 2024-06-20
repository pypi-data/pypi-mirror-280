from pyuu.path import Path

def get_proj_root(sub_path):
    """
    sub_path is inside the root project path
    find a uu project, which includes .uu/pm 
    """
    path = Path(sub_path)
    
    while True:
        prnt_path = path.prnt
        if prnt_path == path:
            return
        path = prnt_path
        if (path/'.uu').exists():
            return path
        
class ProjPath:
    assets:Path
    data:Path
    cache:Path
    tmp:Path
    out:Path
    export:Path

def make_project_path(root_path, name=''):
    root_path = Path(root_path)

    class PATH:
        root = root_path
        assets = root/'assets'/name
        data = root/'data'/name
        cache = root/'cache'/name
        tmp = root/'tmp'/name
        out = root/'out'/name

        messey = tmp/'messey'/name
        export = root/'export'/name
        test = root/'test'/name
        test_data = test/'data'

        uu = root/'.uu'             # .uu to indicate root
        pm = uu/'pm'/name           # app manager
        # proj_info = pm/'info.json'

        ALL_DIRS = [root, assets, data, cache, tmp, out, export, uu, pm]

    return PATH


# def make_mod_path(ProjPath:ProjPath, name:str, version:str=''):
#     class PATH:
#         root=ProjPath.data/'mod'/name/version
#         assets=root/'assets'
#         data=root/'data'
#         export=root/'export'
#         cache=ProjPath.cache/'mod'/name/version
#         tmp=ProjPath.tmp/'mod'/name/version
#         out=ProjPath.out/'mod'/name/version
#     return PATH


