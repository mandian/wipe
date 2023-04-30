Summary:        A UNIX tool for secure deletion
Name:           wipe
Version:        0.24
Release:        1
License:        GPLv2+
Group:          File tools
URL:            http://lambda-diode.com/software/wipe
Source0:	https://github.com/berke/wipe/archive/v%{version}/%{name}-%{version}.tar.gz
#Source0:        http://lambda-diode.com/resources/wipe/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.24-Makefile.patch

%files
%license GPL
%doc README CHANGES BUGS
%doc examples
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/tr/man1/%{name}.1.*

#---------------------------------------------------------------------------

%description
Wipe is a short, nice tool for securely wiping out files from magnetic media.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build linux CC_LINUX=cc

%install
install -dm 0755 %{buildroot}%{_bindir}/
install -pm 0755 %{name} %{buildroot}%{_bindir}/

# manpages
install -dm 0755 %{buildroot}%{_mandir}/man1/
install -pm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/

install -dm 755 %{buildroot}%{_mandir}/tr/man1/
install -pm 644 %{name}.tr.1 %{buildroot}%{_mandir}/tr/man1/%{name}.1

