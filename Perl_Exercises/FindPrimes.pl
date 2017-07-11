#!/usr/bin/perl
#FindPrimes.pl

use strict;
use warnings;

sub noArgsPrimeFinder{
	my $primeCounter = 1;
	my @primeArray = ();
	my @primeSquare = ();
	push @primeArray, 2;
	push @primeSquare, 4;
	my $i = 3;

	print("The following are the first 100 prime numbers.\n\t", $primeArray[0], "\n");

	#c = for (unsigned long i = 3; i<=ULONG_MAX && primeCounter<100; i++)
	while ($primeCounter < 100){
		my $isPrime = 1;
		my $j = 0;
		while ($j < $primeCounter){
			if ($i < $primeSquare[$j]){
				last;
			}
			elsif ($i%($primeArray[$j]) == 0){
				$isPrime = 0;
				last;
			}
		$j++;
		}
		if ($isPrime == 1){
			print("\t", $i, "\n");
			push @primeArray, $i;
			push @primeSquare, ($i*$i);
			$primeCounter++;
		}
	$i++;
	}
}

sub argsPrimeFinder{
	my $primeCounter = 1;
	my @primeArray = ();
	my @primeSquare = ();
	push @primeArray, 2;
	push @primeSquare, 4;
	my $i = 3;

	print("The following are the first ", $_[0], " prime numbers.\n\t", $primeArray[0], "\n");

	while ($primeCounter < $_[0]){
		my $isPrime = 1;
		my $j = 0;
		while ($j < $primeCounter){
			if ($i < $primeArray[$j]){
				last;
			}
			elsif ($i%($primeArray[$j]) == 0){
				$isPrime = 0;
				last;
			}
		$j++;
		}
		if ($isPrime == 1){
			print("\t", $i, "\n");
			push @primeArray, $i;
			push @primeSquare, ($i*$i);
			$primeCounter++;
		}
	$i++;
	}
}

sub main{
	print("Please type the number of prime numbers you would like to find: \n");
	my $numPrimes2Find = <STDIN>;
	chomp($numPrimes2Find);
	argsPrimeFinder($numPrimes2Find);
	noArgsPrimeFinder();
}

main();
