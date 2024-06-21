from json import dumps
from os.path import splitext, join
from email import message_from_file
from email.policy import HTTP, strict

from ruamel.yaml import YAML
from setuptools.command.egg_info import egg_info


def write_egg_files(cmd, basename, filename):
    yaml = YAML()

    with open('package_config.yaml') as file:
        value = yaml.load(file)

    argname = splitext(basename)[0]

    str_value = dumps(value, separators=(',', ':'), ensure_ascii=False)

    cmd.write_or_delete_file(argname, filename, str_value)


class AddRequiresExternal(egg_info):
    def run(self):
        result = super().run()
        if externals := getattr(self.distribution, 'requires_external', None):
            pkg_info_path = join(
                self.egg_base,
                self.egg_info,
                'PKG-INFO',
            )
            with open(pkg_info_path, mode='r+') as file:
                msg = message_from_file(file, policy=strict + HTTP)
                for ext in externals:
                    msg['Requires-External'] = ext

                file.truncate()
                file.seek(0)
                file.write(str(msg))

        return result
