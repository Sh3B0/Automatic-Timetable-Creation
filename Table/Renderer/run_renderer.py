from Table.Renderer.renderer import Renderer
from Table.Renderer.converter import convert
from Table.Renderer.make_sample_table.parser import parse

if __name__ == '__main__':
    # use parse to parse an existing table
    parse()

    # use convert to convert scheduler's output
    # convert()

    # vis renders the data
    vis = Renderer()