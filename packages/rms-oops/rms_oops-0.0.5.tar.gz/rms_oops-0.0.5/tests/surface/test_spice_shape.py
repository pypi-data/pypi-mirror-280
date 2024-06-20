################################################################################
# tests/surface/test_spice_shape.py
################################################################################

import os
import unittest

import cspyce

from oops.frame.frame_        import Frame
from oops.frame.spiceframe    import SpiceFrame
from oops.path.path_          import Path
from oops.path.spicepath      import SpicePath
from oops.surface.spice_shape import spice_shape
from oops.unittester_support  import TESTDATA_PARENT_DIRECTORY
import oops.spice_support as spice


class Test_spice_shape(unittest.TestCase):

    def setUp(self):
        spice.initialize()
        cspyce.furnsh(os.path.join(TESTDATA_PARENT_DIRECTORY, "SPICE", "pck00010.tpc"))
        cspyce.furnsh(os.path.join(TESTDATA_PARENT_DIRECTORY, "SPICE", "de421.bsp"))

    def tearDown(self):
        pass

    def runTest(self):

        _ = SpicePath("VENUS", "SSB", "J2000", path_id="APHRODITE")
        _ = SpiceFrame("VENUS", "J2000", "SLOWSPINNER")

        body = spice_shape("VENUS")
        self.assertEqual(Path.as_path_id(body.origin), "APHRODITE")
        self.assertEqual(Frame.as_frame_id(body.frame),  "SLOWSPINNER")
        self.assertEqual(body.req, 6051.8)
        self.assertEqual(body.squash_z, 1.)

########################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
################################################################################
