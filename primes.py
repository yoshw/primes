###############################################################################
#
# This module defines some simple functions for
# generating and working with prime numbers.
#
# AUTHOR
#
#    Yoshua Wakeham
#        email: yoshwakeham@gmail.com
#        www  : github.com/yoshw
#        tweet: @yoshw
#
# DATE CREATED
#
#    4 July 2014
#
# COPYING
#
#    This program is free software: you can redistribute it
#    and/or modify it under the terms of the GNU General Public
#    License as published by the Free Software Foundation, either
#    version 3 of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from math import sqrt


def prime_sieve(bound):
    '''
    An implementation of the Sieve of Eratosthenes:
    generates a list of all the prime numbers up to
    some bounding value.
    '''
    try:
        list = [1] * bound
    except:
        print("Error: upper bound is not an integer: {}".format(bound))

    # sieve even numbers greater than 2
    for i in range(3, bound, 2):
        list[i] = 0
    # sieve remaining composites
    for i in range(3, int(sqrt(bound))):
        if list[i-1]:
            for j in range(i**2, bound+1, 2*i):
                list[j-1] = 0
    return list


def is_sieved_prime(n, prime_list):
    '''
    Tests an integer for primality, assuming a list
    of primes has already been generated in which
    primes[n-1] evaluates to True if n is prime.
    '''
    try:
        test = prime_list[n-1]
    except TypeError:
        print("Error: invalid input to is_prime() function")

    return bool(test)

def is_naive_prime(n):
    '''
    Tests an integer for primality using the naive
    method, i.e. checking for divisibility by every
    odd integer from 3 to the square root of n.
    '''
    if n > 1:
        if n % 2 == 1:
            for i in range(3, int(sqrt(n))+1, 2):
                if n % i == 0:
                    return False
            return True
    return False
