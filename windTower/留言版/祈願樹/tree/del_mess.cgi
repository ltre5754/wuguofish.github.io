&error("�K�X���~") if ($T{username} ne $password);
my @file = &readfile('mess.txt');

open FILE,'>mess.txt';
for (@file) {
	print FILE $_ unless ($_ =~ /^$T{x_point}��(.*)/);
}
close FILE;
print "<META HTTP-EQUIV=REFRESH CONTENT='0;URL=$cgi_url'>";
exit;