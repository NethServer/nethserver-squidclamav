======================
nethserver-squidclamav
======================

If ``squidclamav[status]`` is set to ``enabled``,
Squid will load clamav libraries and signatures using E-CAP module.

Files bigger than 5MB are not scanned.

Please also note that the antivirus will not check HTTPS traffic
even if Transparent HTTPS proxy is enabled.
