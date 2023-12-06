# -*- coding: utf-8 -*-

import pytest

import nebula


def pytest_addoption(parser):
    group = parser.getgroup("nebula")
    group.addoption(
        "--foo",
        action="store",
        dest="dest_foo",
        default="2023",
        help='Set the value for the fixture "bar".',
    )

    parser.addini("HELLO", "Dummy pytest.ini setting")


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo


@pytest.fixture
def xilinx_linux(request):
    # Get support files

    # Get No-OS

    # Check tools

    # Build project

    # Start monitoring

    # Load hardware




    # return request.config.option.xilinx_linux