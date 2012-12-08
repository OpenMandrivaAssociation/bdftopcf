Name: bdftopcf
Version: 1.0.3
Release: %mkrel 4
Summary: Convert X font from Bitmap Distribution Format to Portable Compiled Format
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxfont-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Bdftopcf converts X fonts from Bitmap Distribution Format
to Portable Compiled Format.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 663317
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 590570
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2010.1
+ Revision: 522191
- rebuilt for 2010.1

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 448649
- new release

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2010.0
+ Revision: 413164
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2009.0
+ Revision: 220479
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-4mdv2008.1
+ Revision: 166384
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-3mdv2008.1
+ Revision: 153800
- Update BuildRequires and resubmit package.

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-2mdv2008.1
+ Revision: 148918
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Apr 30 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.0.1-1mdv2008.0
+ Revision: 19468
- Updated to 1.0.1.


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 20:33:11 (27443)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

