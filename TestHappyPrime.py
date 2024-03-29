# Riley Vashtee: [reading from display] Find the next number in the sequence: 313, 331, 367...? What?
# Martha Jones: You said the crew knew all the answers!
# Riley Vashtee: The crew's changed since we set of questions.
# Martha Jones: You're joking!
# The Doctor: 379
# Martha Jones: What?
# The Doctor: It's a sequence of happy primes - 379
# Martha Jones: Happy what?
# The Doctor: Just enter it!
# Riley Vashtee: Are you sure? We only get one chance.
# The Doctor: Any number that reduces to one when you take the sum of the square of its digits and continue iterating it until it yields 1 is a happy number, any number that doesn't, isn't. A happy prime is both happy and prime. Now *type it in*!
# [aside]
# The Doctor: I dunno, talk about dumbing down. Don't they teach recreational mathematics anymore?
#

import unittest
import HappyPrime

class HappyPrimeTest(unittest.TestCase):
    """Test generating happy primes"""
    def test_getNextHappyPrime(self):
        happyprimes=[313,331,367,379]
        for c,n in zip(happyprimes[:-1],happyprimes[1:]):
            self.assert_(HappyPrime.getNextHappyPrime(c)==n,
        'getNextHappyPrime() thinks that next happy prime after %d is %d, not %d' % (c,HappyPrime.getNextHappyPrime(c),n))
        
class HappyTest(unittest.TestCase):
    """Test happiness"""
    def test_isHappy(self):
        self.assert_(HappyPrime.isHappy(HappyPrime.sumSquareDigits(313)), 'isHappy() thinks %d is not happy' % HappyPrime.sumSquareDigits(313))
        self.assert_(HappyPrime.isHappy(313), 'isHappy() thinks that 313 is not happy')

class PrimeTest(unittest.TestCase):
    """Test primeness"""
    def test_isPrime(self):
        self.assert_(HappyPrime.isPrime(313), 'isPrime() thinks 313 is not prime')
        # Some known primes (primes smaller than 20)
        for prime in [2,3,5,7,11,13,17,19]:
            self.assert_(HappyPrime.isPrime(prime), 'isPrime() thinks %d is not prime' % prime)
    def test_nextPrime(self):
        primes=[2,3,5,7,11,13,17,19]
        for c,n in zip(primes[:-1],primes[1:]):
            self.assert_(HappyPrime.nextPrime(c)==n, 'nextPrime() thinks that next prime after %d is not %d' % (c,n))

if __name__ == '__main__':
    unittest.main()