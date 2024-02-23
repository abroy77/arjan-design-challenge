from importlib.util import spec_from_file_location, module_from_spec
import os


class PluginInterface:
    @staticmethod
    def initialize() -> None:
        ...


def load_plugins():
    loader_path = __file__
    plugins_path = os.path.join(os.path.dirname(loader_path), "plugins")
    plugin_filenames = [filename for filename in os.listdir(plugins_path) if filename.endswith('.py')]
    for plugin_filename in plugin_filenames:
        module_name = os.path.splitext(plugin_filename)[0]
        plugin_filepath = os.path.join(plugins_path, plugin_filename)
        spec = spec_from_file_location(module_name, location=plugin_filepath)
        if spec:
            module: PluginInterface = module_from_spec(spec)  # type: ignore
            spec.loader.exec_module(module)  # type: ignore
            module.initialize()
