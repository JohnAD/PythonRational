# Rational\__init__.py
#
#   Rational wrapper for the python Fraction class of the "fractions" standard module.
#
#   This library that is a thin wrapper that uses the "fractions" module
#   in a different, and arguably better, manner.
#

from fractions import Fraction
from decimal import Decimal

class Rat(Fraction):

    def __init__(self, *args, **kwargs):
        Fraction.__init__(self, *args, **kwargs)
        return

    def __str__(self, *args, **kwargs):
        # the following would be WRONG because it converts to float first:
        #
        #     return str(Decimal(1.0*self.numerator/self.denominator))
        #
        #  example:
        #     >>> from Rational import Rat
        #     >>> str(Rat(11, 10))
        #     '1.100000000000000088817841970012523233890533447265625'
        #
        ## TODO: actually write a proper converter to decimal
        ##    make sure it handles both python2 and python3 int division diffs
        return str(Decimal(1.0*self.numerator/self.denominator))
