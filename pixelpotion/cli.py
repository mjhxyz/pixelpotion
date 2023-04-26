import argparse

from pixelpotion import split_frames, convert


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    gif_parser = subparsers.add_parser('gif')
    gif_subparsers = gif_parser.add_subparsers(dest='gif_command')
    gif_split_parser = gif_subparsers.add_parser(
        'split', help='Split GIF animation into individual frames')

    gif_split_parser.add_argument(
        '-f', '--file', help='Input file path of GIF animation', required=True)
    gif_split_parser.add_argument(
        '-o', '--output', help='Output directory path for images', required=True)
    gif_split_parser.add_argument(
        '-p', '--prefix', help='Prefix for output images (default: frame)',
        default='frame', required=False)

    convert_parser = subparsers.add_parser('convert', help='Convert image')
    convert_parser.add_argument(
        '-f', '--file', help='Input file path of image', required=True)
    convert_parser.add_argument(
        '-o', '--output', help='Output file path of image', required=True)
    convert_parser.add_argument(
        '-t', '--type', help='Output image format (default: input image format)',
        default=None, required=False)
    convert_parser.add_argument(
        '-w', '--width', help='Output image width (default: original width)',
        type=int, required=False)
    convert_parser.add_argument(
        '-he', '--height', help='Output image height (default: original height)',
        type=int, required=False)
    convert_parser.add_argument(
        '-q', '--quality', help='Output image quality (default: 80)',
        type=int, required=False)
    convert_parser.add_argument(
        '-opt', '--optimize', help='Whether to optimize output image (default: True)',
        type=bool, required=False)

    args = parser.parse_args()
    if args.command == 'gif':
        if args.gif_command == 'split':
            split_frames.split_frames(args.file, args.output, args.prefix)
        else:
            gif_parser.print_help()
    elif args.command == 'convert':
        convert.convert(args.file, args.output, args.type, args.width,
                        args.height, args.quality, args.optimize)
    else:
        parser.print_help()
