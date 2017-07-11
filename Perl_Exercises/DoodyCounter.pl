#!/usr/bin/perl
#DoodyCounter.pl

use strict;
use warnings;

sub main{

	my $counter = 0;
	my @wordArray = ();
	my @testArray = ();

	my $FILE = $ARGV[0];
	open(my $fh, "<$FILE");

	while(<$fh>){
		@wordArray = split /\s+/, $_;

		foreach(@wordArray){
			push @testArray, $_;
		}
	}

	foreach(@testArray){
		if ($_ =~ /duty|duties|doody|doodie|doodies|dudey/gi){
			$counter = $counter+1;
		}
	}
	print("Hehehe, you said doodie (or something that looks or sounds like doodie) ", $counter, " many times.\n");
	
}

main();
