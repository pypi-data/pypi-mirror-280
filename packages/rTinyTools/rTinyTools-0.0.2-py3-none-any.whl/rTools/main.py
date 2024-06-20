import sys
import click
from .json_yaml.json_yaml_convert import JsonYamlConvert


@click.group()
def cli():
    """rfooox's tools."""
    pass


# Json 转化为 yaml
@cli.command(short_help='JSON or YAML convert.')
# @cli.command(short_help='test',)
# @click.argument('file_path', nargs=1, type=str)
@click.option('-j2y', '-j', 'convert_type', nargs=1, type=str, flag_value='j2y', help='JSON to YAML.')
@click.option('-y2j', '-y', 'convert_type', nargs=1, type=str, flag_value='y2j', help='YAML to JSON.')
@click.option('-del', '-d', 'is_del', is_flag=True, required=True, default=False, help='Flag to delete source file.')
@click.option('--path', '-p', 'path', type=click.Path(), required=True, help='Specify file path.')
@click.help_option('--help',)
# @click.argument('path', type=click.Path(exists=True))
# 1. 业务逻辑
def convert(convert_type, path, is_del):
    """
    Json Yaml Convert Tool

    You can convert JSON file to YAML file.
    """
    co = JsonYamlConvert()

    if convert_type == 'j2y':
        # JSON 转化为 YAML
        click.echo('test_J2Y')
        co.batch_json_to_yaml(path, is_del)

    elif convert_type == 'y2j':
        # YAML 转化为 JSON
        # yaml文件内容转换成json格式
        click.echo('test_Y2J')
        co.batch_yaml_to_json(path, is_del)

    else:
        # 无匹配项目
        pass


if __name__ == '__main__':
    # sys.argv = ['main.py', '--help']
    sys.argv = ['main.py', 'convert', '--help']
    # sys.argv = ['main.py', '-j2y', r'-p', r'D:\rfooox\rTools\testfile', '-del']
    # sys.argv = ['main.py', '-y2j', r'-p', r'D:\rfooox\rTools\testfile', '-del']
    # sys.argv = ['main.py', r'-j2y=D:\rfooox\rTools\testfile\test.json' ]
    # sys.argv = ['main.py', r'-j2y=D:\rfooox\rTools\testfile' ]
    # sys.argv = ['main.py', r'-y2j=D:\rfooox\rTools\testfile' ]
    # sys.argv = ['main.py', '-j2y']
    # convert()
    cli()
