Summary:	USB Video Class grabber
Name:		luvcview
Version:	0.2.6
Release:	1
License:	GPL v2
Group:		Applications
# svn export http://svn.quickcamteam.net/svn/luvcview/tags/luvcview-0.2.6
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	154b8088c8126a313261c299fd2d68ca
Source1:	http://svn.berlios.de/svnroot/repos/linux-uvc/linux-uvc/trunk/uvcvideo.h
# Source1-md5:	84360f0925d68e95a24051b5bcce7db6
Source2:	http://svn.berlios.de/svnroot/repos/linux-uvc/linux-uvc/trunk/uvc_compat.h
# Source2-md5:	d01ff5ca0bc5b66abffbcea91c0b6508
Source3:	http://svn.quickcamteam.net/svn/qct/Linux/Common/include/dynctrl-logitech.h
# Source3-md5:	b1a1f4ee29f49cea6a2adbf623f86c18
Patch0:		%{name}-makefile.patch
URL:		http://www.quickcamteam.net/software/linux/v4l2-software/luvcview/
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
luvcview is a camera viewer for UVC based webcams. It includes an
mjpeg decoder and is able to save the video stream as an AVI file.

%prep
%setup -q
%patch0 -p1
cp -f %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
%{__make} \
	CC="%{__cc}" CPP=%{__cxx}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	BIN=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README ToDo
%attr(755,root,root) %{_bindir}/*
