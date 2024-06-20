import os
import functools
import importlib.abc
import importlib.machinery
import importlib.util

from pyuu.path import Path


__all__ = [
    'DictMetaPathFinder'
]

class DictMetaPathFinder(importlib.abc.MetaPathFinder):
    """
    A custom Python module finder that uses a provided mapping
    to dynamically locate and load modules based on their full names.

    Args:
        module_path_map (dict): A dictionary that maps full module names to their file or directory paths.

    This custom module finder allows for dynamic module loading based on custom
    mappings, enabling the use of non-standard module locations or custom
    module resolution logic.

    Usage:
    1. Create an instance of DictMetaPathFinder by providing a module_path_map.
    2. Register the custom module finder using sys.meta_path.
    3. When an import statement is executed, this finder is invoked to locate and load modules.

    Note: This finder is designed for advanced use cases and may be used when you
    need to implement custom module loading behavior or support unconventional
    module locations.

    Demo:
    # Define a custom module path mapping, mapping module names to module file or directory paths
    module_path_map = {
        'my_module': '/path/to/my_module.py',
        'my_package.moduleA': '/path/to/my_package/moduleA.py',
        'my_package.moduleB': '/path/to/my_package/moduleB.py',
    }

    # Create and register the custom module finder
    from my_module import DictMetaPathFinder

    custom_finder = DictMetaPathFinder(module_path_map)
    sys.meta_path.append(custom_finder)

    # Now you can import modules, and the custom finder will be used to find and load them
    import my_module
    from my_package import moduleA, moduleB
    """

    def __init__(self, module_path_map:dict):
        """
        Initialize the custom module finder with the provided module_path_map.

        Args:
            module_path_map (dict): A dictionary that maps full module names to their file or directory paths.
        """
        self.module_path_map = module_path_map

    def find_spec(self, fullname, path, target=None):
        """
        Find and load a module's specification based on its full name.

        Args:
            fullname (str): The full name of the module being searched.
            path: Not used in this implementation, reserved for compatibility.
            target: An optional target for module search, reserved for compatibility.

        Returns:
            ModuleSpec or None: If a module specification is found, it returns a ModuleSpec object;
            otherwise, it returns None if the module is not found.

        This method dynamically locates and loads modules based on the provided
        module_path_map. It sets the 'origin' based on whether the module is a file
        or a package, and constructs a ModuleSpec accordingly.

        If the module is a package, it includes submodule search locations to support
        nested modules within the package.

        If the requested module is not in the module_path_map, it returns None.

        Raises:
            NotImplementedError: If the module is identified as a namespace package.
        """
        module_path = self.module_path_map.get(fullname)
        if not module_path:
            return
        module_path = Path(module_path)
        

        if module_path.is_file():
            origin=str(module_path)
        else:
            init_path = module_path/'__init__.py'
            if init_path.exists():
                origin= str(module_path/'__init__.py')
            else:
                raise NotImplementedError('namespace package')

        loader=importlib.machinery.SourceFileLoader(fullname, origin)

        if loader.is_package(fullname):   
            spec = importlib.util.spec_from_file_location(
                fullname,
                origin, 
                loader=loader,
                submodule_search_locations=[str(module_path)]
                )
        else:
            spec = importlib.util.spec_from_file_location(
                fullname,
                origin, 
                loader=loader
                )
        return spec


