#!/usr/bin/perl
#ImageSort.pl

use strict;
use warnings;
use Cwd;
use File::Copy;
#use Image::Size 'imgsize';

sub sizePNG{
	return unless $_[0];
	my ($width, $height);
	($width, $height) = unpack( "NN", $1) if $_[0] =~ /IHDR(........)/;
	return ($width, $height);
}

sub sizeGIF{
	return unless $_[0];
	my ($width, $height);
	($width, $height) = unpack ("SS", $1) if $_[0] =~ /^GIF8..(....)/;
	return ($width, $height);
}

sub sizeJPG{
	return unless $_[0];
	my ($width, $height);
	($width, $height) = unpack("nn", $1) if $_[0] =~ /\xFF\xC0...(....)/;
	return($width, $height);
}

sub main{
	#my $img_x = 0;
	#my $img_y = 0;
	my @images = ();
	my $imagePath = "";

	#access directory needing to be sorted
	my $newDirectory = $ARGV[0];
	chdir($newDirectory) or die "Can't change directory to $! .\n";
	my $currentDir = getcwd;
	print (getcwd, "\n");
	
	#create small/medium/large directories in sorted directory
	#unless (mkdir "Large_Images"){
	#	die "Unable to create Large_Images directory.\n";
	#}
	#unless (mkdir "Medium_Images"){
	#	die "Unable to create Medium_Images directory.\n";
	#}
	#unless (mkdir "Small_Images"){
	#	die "Unable to create Small_Images directory.\n";
	#}

	#search for all images in directory
	opendir(my $currentDirectory, $newDirectory) or die "Can't opendir $newDirectory: $!";
	@images = grep{/\.jpg$|\.gif$|\.bmp$|\.png$/} readdir($currentDirectory);
	closedir $currentDirectory;

	#access image sizes
	foreach(@images){
		
		my @imageSizes = ();
		#($img_x, $img_y) = imgsize($_);

		$imagePath = join('/', $currentDir, $_);
		print($imagePath, "\n");

		if ($imagePath =~ /\.png$/){
			@imageSizes = sizePNG($imagePath);
			print("@imageSizes\n");
		}
		elsif ($imagePath =~ /\.gif$/){
			@imageSizes = sizeGIF($imagePath);
			print("@imageSizes\n");
		}
		elsif ($imagePath =~ /\.jpg$/){
			@imageSizes = sizeJPG($imagePath);
			print("@imageSizes\n");
		}

		#determine if image is small/medium/large
		#place images in correct directories

		#if ($img_x >= 700 or $img_y >= 700){
		#	#is Large
		#	my $imageDir = join('/', $currentDir, "Large_Images");
		#	move($imagePath, $imageDir) or die "Move failed: $!";
		#}
		#elsif (($img_x >= 300 && $img_x < 700) or ($img_y >=300 && $img_y < 700){
		#	#is Medium
		#	my $imageDir = join('/', $currentDir, "Medium_Images");
		#	move($imagePath, $imageDir) or die "Move failed: $!";
		#}
		#elsif ($img_x < 300 or $img_y < 300){
		#	#is Small
		#	my $imageDir = join('/', $currentDir, "Small_Images");
		#	move($imagePath, $imageDir) or die "Move failed: $!";
		#}
	}
}

main()
