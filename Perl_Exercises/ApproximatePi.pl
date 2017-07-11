#!/usr/bin/perl
#ApproximatePi.pl

use strict;
use warnings;

sub approximate{
	my $pi = 0;
	my $n = $_[0];
	print("=========================================\n");
	print("| value of k | approximation of pi at k |\n");
	print("=========================================\n");
	for (my $k=1; $k<=$n; $k++){
		$pi = ($pi + (((-1)**($k-1))/((2*$k)-1)));
		if($k == 1){
			print("|     ", $k, "      |     ", (4*$pi), "                    |\n");
			print("=========================================\n");
		}
		elsif($k>1 && $k<10){
			print("|     ", $k, "      |     ", (4*$pi), "     |\n");
			print("=========================================\n");
		}
		else{
			print("|     ", $k, "     |     ", (4*$pi), "      |\n");
			print("=========================================\n");
		}
	}
}

print("Please input a top delimiter - (1 to n):");
my $rangeVar = <STDIN>;
chomp($rangeVar);
approximate($rangeVar);
