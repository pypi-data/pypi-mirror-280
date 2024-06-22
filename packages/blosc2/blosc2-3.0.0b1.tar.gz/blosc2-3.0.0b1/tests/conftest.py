#######################################################################
# Copyright (c) 2019-present, Blosc Development Team <blosc@blosc.org>
# All rights reserved.
#
# This source code is licensed under a BSD-style license (found in the
# LICENSE file in the root directory of this source tree)
#######################################################################
import pytest

import blosc2


# This still needs to pass the '-s' flag to pytest to see the output but anyways
@pytest.fixture(scope="session", autouse=True)
def setup_session():
    # This code will be executed before the test suite
    print()
    blosc2.print_versions()


@pytest.fixture(scope="session")
def c2sub_context():
    # You may use the URL and credentials for an already existing user
    # in a different Caterva2 subscriber.
    c2params = dict(urlbase="https://demo.caterva2.net/",
                    username=None, password=None)
    with blosc2.c2context(**c2params):
        yield c2params
