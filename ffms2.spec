Name:           ffms2
Version:        2.23
Release:        10%{?dist}
License:        MIT
Summary:        Wrapper library around libffmpeg
URL:            https://github.com/FFMS/ffms2
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  zlib-devel

%description
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
FFmpegSource (usually known as FFMS or FFMS2) is a cross-platform wrapper
library around libffmpeg, plus some additional components to deal with file
formats libavformat has (or used to have) problems with.

%prep
%autosetup
sed -i 's/\r$//' COPYING

%build
autoreconf -vfi
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
rm -rf %{buildroot}%{_docdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/ffmsindex
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/*
%{_libdir}/lib%{name}.so
%{_includedir}/ffms*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.23-9
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.23-7
- Rebuilt for ffmpeg-3.5 git

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.23-6
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.23-3
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.23-1
- Update to 2.23

* Tue Aug 30 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.22-3
- Couple of trivial fixes

* Tue Jun 14 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 2.2-2
- rebuilt against new ffmpeg

* Wed Nov 04 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.22-1
- Update to 2.22

* Sun Jun 28 2015 Ivan Epifanov <isage.dna@gmail.com> - 2.21-1
- Update to 2.21

* Mon Jan  5 2015 Ivan Epifanov <isage.dna@gmail.com> - 2.20-1
- Update to 2.20

* Fri Mar 28 2014 Ivan Epifanov <isage.dna@gmail.com> - 2.19-1
- Initial spec for Fedora
