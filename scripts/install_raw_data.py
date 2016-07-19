#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from jsk_data import download_data


def main():
    PKG = 'hrp2_apc'

    download_data(
        pkg_name=PKG,
        path='raw_data/2016-07-19-16-46-05-hrp2_rosbag_apc_look_around.bag',
        url='https://drive.google.com/uc?id=0B9P1L--7Wd2vYmdYdjFmSHV4dkU',
        md5='d344dc71d4f545012fa7cdfa9dea4b15',
    )


if __name__ == '__main__':
    main()