Summary: NethServer squidclamav configuration
Name: nethserver-squidclamav
Version: 3.1.3
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-c-icap, nethserver-antivirus, nethserver-httpd, nethserver-squidguard
Requires: squidclamav
Obsoletes: ecap-clamav

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
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING


%changelog
* Thu Aug 31 2023 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.1.3-1
- Forse c-icap restart - Bug NethServer/dev#6762

* Thu Aug 24 2023 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.1.2-1
- c-icap service does not start - Bug NethServer/dev#6762

* Mon Sep 13 2021 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.1.1-1
- Squidclamav: Squid got an invalid ICAP OPTIONS - Bug NethServer/dev#6569

* Fri Aug 30 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.1.0-1
- Antivirus: improve memory usage - NethServer/dev#5803

* Fri Oct 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 3.0.0-1
- squid crashes when ecap-clamav is enabled - Bug NethServer/dev#5352

* Tue Jan 03 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.0-1
- Antivirus web: replace Squidclamav - NethServer/dev#5183

* Thu Aug 25 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.3.1-1
- nethserver-squidclamav: reload action not supported by c-icap - Bug NethServer/dev#5083

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.3.0-1
- First NS7 release

* Thu Feb 18 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Web filter antivirus whitelist - Enhancement #3354 [NethServer]

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


