#!/usr/bin/perl
#Isocoles.c

use strict;
use warnings;

print("Please input the desired number of asterisks you would like as a base to the triangle:\n");
my $numAsterisks = <STDIN>;

for (my $i = 1; $i<=$numAsterisks; $i++){
	print("*"x$i, "\n");
}
