from __future__ import print_function

import sys
import argparse

import pyarrow.parquet as pq


def get_metadata(parquet_file):
    r = pq.ParquetFile(parquet_file)
    return r.metadata


def get_schema(parquet_file):
    r = pq.ParquetFile(parquet_file)
    return r.schema


def write_data(parquet_file):

    try:
        r = pq.ParquetFile(parquet_file)
        write_header = True
        for i in range(r.num_row_groups):
            data = r.read_row_group(i)
            sys.stdout.write(data.to_pandas().to_csv(header=write_header, index=False))
            write_header = False
    except (BrokenPipeError, IOError):
        # Broken pipe
        pass
    sys.stderr.close()


def main(cmd_args=sys.argv, skip=False):
    if not skip:
        cmd_args = init_args()

    if cmd_args.schema:
        print("\n # Schema \n", get_schema(cmd_args.file))
    if cmd_args.metadata:
        print("\n # Metadata \n", get_metadata(cmd_args.file))
    else:
        write_data(cmd_args.file)


def init_args():
    parser = argparse.ArgumentParser(
        description="Command line tool to convert Apache Parquet files to CSV",
        usage="usage: parq2csv file [--schema | --metadata]"
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-s",
                       "--schema",
                       nargs="?",
                       type=bool,
                       const=True,
                       help="get schema information",
                       )

    group.add_argument("-m",
                       "--metadata",
                       nargs="?",
                       type=bool,
                       const=True,
                       help="get metadata information",
                       )

    parser.add_argument("file",
                        type=argparse.FileType('rb'),
                        help='Parquet file')

    cmd_args = parser.parse_args()

    return cmd_args


if __name__ == '__main__':
    args = init_args()
    main(args, skip=True)

