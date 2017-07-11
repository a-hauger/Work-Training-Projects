#!/usr/bin/perl
#ImageSort.pl

use strict;
use warnings;
use Cwd;
use File::Copy;
use Image::Size 'imgsize';

sub main{
	my $img_x = 0;
	my $img_y = 0;
	my @images = ();
	my $imagePath = "";
	my $imageDir = "";

	#access directory needing to be sorted
	my $newDirectory = $ARGV[0];
	chdir($newDirectory) or die "Can't change directory to $! .\n";
	my $currentDir = getcwd;
	print (getcwd, "\n");
	
	#create small/medium/large directories in sorted directory
	unless (mkdir "Large_Images"){
		die "Unable to create Large_Images directory.\n";
	}
	unless (mkdir "Medium_Images"){
		die "Unable to create Medium_Images directory.\n";
	}
	unless (mkdir "Small_Images"){
		die "Unable to create Small_Images directory.\n";
	}

	#search for all images in directory
	opendir(my $currentDirectory, $newDirectory) or die "Can't opendir $newDirectory: $!";
	@images = grep{/\.jpg$|\.gif$|\.bmp$|\.png$/} readdir($currentDirectory);
	closedir $currentDirectory;

	#access image sizes
	foreach(@images){
			
		my @imageSizes = (0, 0);
		($img_x, $img_y) = imgsize($_);

		$imagePath = join('/', $currentDir, $_);
		print($imagePath, "\n");
		print ($img_x, " ", $img_y, "\n");

		#determine if image is small/medium/large
		#place images in correct directories

		if ($img_x >= 700 or $img_y >= 700){
			#is Large
			 $imageDir = join('/', $currentDir, "Large_Images");
			move($imagePath, $imageDir) or die "Move failed: $!";
		}
		elsif (($img_x >= 300 && $img_x < 700) or ($img_y >=300 && $img_y < 700)){
			#is Medium
			$imageDir = join('/', $currentDir, "Medium_Images");
			move($imagePath, $imageDir) or die "Move failed: $!";
		}
		elsif ($img_x < 300 or $img_y < 300){
			#is Small
			$imageDir = join('/', $currentDir, "Small_Images");
			move($imagePath, $imageDir) or die "Move failed: $!";
		}
	}
}

main()
