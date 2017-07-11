#!/usr/bin/perl
#Collatz.pl

use strict;
use warnings;

sub collatzRecursive{
	my $original = $_[2];
	my $number = $_[0];
	my $bound = $_[1];

	if($_[0] == 1){
                print("It's true! ", $_[2], " can be made equal to one in ", $bound, " iterations!\n");
                return($bound);
        }
	elsif($_[1]>=1000){
                print("You have reached the upper bounds.  It's possible the Collatz Conjecture still works, but after 1000 iterations it has not.\n");
                return(-1);
        }
	elsif($_[0] != 1 && $_[1]<1000){
		if($_[0]%2 == 0){
			$number = ($_[0]/2);
		}
		elsif($_[0]%2 == 1){
			$number = (3*$_[0])+1;
		}
		$bound++;
		collatzRecursive($number, $bound, $original);
	}
	else{
		print("You broke it!");
		return;
	}
}

sub histogram{
	my $remainder1 = 0;
	my $remainder2 = 0;
	my $remainder3 = 0;

	my %hash = ($_[0], $_[1], $_[2], $_[3], $_[4], $_[5]);
	my @numbers = keys %hash;
	my @iterations = values %hash;

	my $stoppage1 = $hash{$numbers[0]};
	my $stoppage2 = $hash{$numbers[1]};
	my $stoppage3 = $hash{$numbers[2]};

	#gathering the necessary ASCII for first number

		my $underscore1 = $stoppage1/25;

		$stoppage1 = ($stoppage1 - ((int $underscore1)*25));
		
		my $hyphen1 = $stoppage1/14;		

		$stoppage1 = ($stoppage1 - ((int $hyphen1)*14));
		
		if($stoppage1 == 0){
			#no remainder
			$remainder1 = '|';
		}
		else{
			#remainder
			$remainder1 = ')';
		}

	#dealing with the second number

		my $underscore2 = $stoppage2/25;

		$stoppage2 = ($stoppage2 - ((int $underscore2)*25));

		my $hyphen2 = $stoppage2/14;

		$stoppage2 = ($stoppage2 - ((int $hyphen2)*14));

		if($stoppage2 == 0){
			#no remainder
			$remainder2 = '|';
		}
		else{
			#remainder
			$remainder2 = ')';
		}

	#dealing with the third number

		my $underscore3 = $stoppage3/25;

		my $stoppage3 = ($stoppage3 - ((int$underscore3)*25));

		my $hyphen3 = $stoppage3/14;

		$stoppage3 = ($stoppage3 - ((int $hyphen3)*14));

		if($stoppage3 == 0){
			#no remainder
			$remainder3 = '|';
		}
		else{
			#remainder
			$remainder3 = ')';
		}

	print("\nKEY:: _ (underscore) = 25, - (hyphen) = 14, ) (close parens) = remainder\n");
	print(" 			Iterations\n");
	print(" 0  50         250            500            750           1000\n");
	print("  __|__ __ __ __|__ __ __ __ __|__ __ __ __ __|__ __ __ __ __|\n");
	print(" |", "_"x$underscore1, "\n");
	print("N|", "_"x$underscore1, "-"x$hyphen1, $remainder1, "  ", $numbers[0], " ", $iterations[0], "\n");
	print("U|\n");
	print("M|", "_"x$underscore2, "\n");
	print("B|", "_"x$underscore2, "-"x$hyphen2, $remainder2, "  ", $numbers[1], " ", $iterations[1], "\n");
	print("E|\n");
	print("R|", "_"x$underscore3, "\n");
	print("S|", "_"x$underscore3, "-"x$hyphen3, $remainder3, "  ", $numbers[2], " ", $iterations[2], "\n");
	print(" |\n");
}

sub main{
	print("Please enter three numbers you would like to test the Collatz Conjecture with: \n");

	my $number1 = <STDIN>;
	my $number2 = <STDIN>;
	my $number3 = <STDIN>;
	my $bound = 0;
	chomp($number1);
	chomp($number2);
	chomp($number3);

	print("\nBe advised that if the number does not equal 1 after 1000 iterations, the function will cease.\n");

	my $stoppageTime1 = collatzRecursive($number1, $bound, $number1);
	my $stoppageTime2 = collatzRecursive($number2, $bound, $number2);
	my $stoppageTime3 = collatzRecursive($number3, $bound, $number3);

	histogram($number1, $stoppageTime1, $number2, $stoppageTime2, $number3, $stoppageTime3);	
}

main();
