%define _name folder_color

Name: folder-color
Version: 0.2.7
Release: 1
Summary: Folder Color
License: GPL-3.0+
Group: Productivity/File utilities
Source: https://launchpad.net/~costales/+archive/ubuntu/folder-color/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz
BuildRequires: fdupes
BuildRequires: hicolor-icon-theme
BuildRequires: intltool
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-distutils-extra
BuildArch: noarch
Requires: %{name}-common
Requires: nautilus
Requires: nautilus-python
%description
Folder Color allows one to choose the color or emblem of a folder in nautilus

%package common
Version: 0.1.3
Summary: Folder Color common files
Group: Productivity/File utilities
Source: https://launchpad.net/~costales/+archive/ubuntu/folder-color/+sourcefiles/%{name}-common/%{version}/%{name}-common_%{version}.tar.gz
Requires: gvfs
%description common
Folder Color common files

%prep
%setup -q -n nautilus
%setup -q -D -T -a 1 -n nautilus

%build
# nothing to build

%install
for dir in . common; do
    pushd $dir
    %{__python3} setup.py install --root=%{buildroot} --prefix=%{_prefix}
    popd
done
%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
#%doc /usr/share/doc/%{name}/
%{python3_sitelib}/%{_name}-*
%{_datadir}/nautilus-python/

%files common
%defattr(-,root,root)
%doc /usr/share/doc/%{name}-common/
%{python3_sitelib}/%{_name}_common-*
%{_datadir}/icons/hicolor/*/*/
%{_datadir}/locale/*/*/
