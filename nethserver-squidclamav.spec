Summary: NethServer squidclamav configuration
Name: nethserver-squidclamav
Version: 1.1.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-c-icap, nethserver-antivirus, nethserver-httpd, nethserver-squidguard
Requires: squidclamav

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer squidclamav configuration

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Tue Sep 29 2015 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Make Italian language pack optional - Enhancement #3265 [NethServer]

* Tue Jan 20 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1.ns6
- squidGuard: support multiple profiles - Enhancement #2958 [NethServer]
- Enhance visual appearance of proxy block pages - Feature #2866 [NethServer]

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.4-1.ns6
- Enable logging to /var/log/c-icap/server.log - Enhancement #2289 [NethServer]

* Tue Jul 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
- Move antivirus proxy web ui from nethserver-antivirus package

* Mon Jul 29 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Fix typo for nethserver-httpd requires #1959
- Add nethserver-squid dependency #1959

* Fri Jul 26 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1.ns6
- Set default status to disabled #1959
- Add nethserver-httpd dependency  #1959

* Thu Jun 20 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1.ns6
- First release - Feature #1959


