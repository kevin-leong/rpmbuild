#
# spec file for package folder-color
#

%define _name   folder_color
Name:           folder-color
Version:        0.0.91
Release:        0

%define version_common  0.0.93

Summary:	    Folder Color
License:        GPL-3.0+
Group:          Productivity/File utilities
Url:            https://launchpad.net/folder-color
Source0:        https://launchpad.net/~costales/+archive/ubuntu/folder-color/+sourcefiles/%{name}-common/%{version_common}/%{name}-common_%{version_common}.tar.gz
Source1:        https://launchpad.net/~costales/+archive/ubuntu/folder-color/+sourcefiles/%{name}/%{version}/%{name}_%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildArch:      noarch

%description
Allows one to choose the color or emblem of a folder

%package common
Summary:        Common files for Folder Color
Group:          Productivity/File utilities
Requires:       gvfs

%description common
Common files for Folder Color

%package -n %{name}-nautilus
Summary:        Nautilus extension for Folder Color
Group:          Productivity/File utilities
Requires:       %{name}-common = %{version}
Requires:       nautilus
Requires:       nautilus-python

%description -n %{name}-nautilus
Nautilus extension for Folder Color

%prep
#%setup -q -n %{name}-common
#%setup -q -D -T -a 1 -n %{name}-common
%setup -q -n common
%setup -q -D -T -a 1 -n common
mv -f nautilus %{name}-nautilus

#chmod a-x COPYING
chmod a-x COPYING.GPL3
sed -i '/name/s/%{name}/%{name}-nautilus/' %{name}-nautilus/setup.py

%build
# Nothing to build.

%install
for dir in . %{name}-nautilus; do
    pushd $dir
    %{__python3} setup.py install --root=%{buildroot} --prefix=%{_prefix}
    popd
done
%fdupes %{buildroot}%{_datadir}

%files common
%defattr(-,root,root)
#%doc COPYING
%doc COPYING.GPL3
%{python3_sitelib}/%{_name}_common-*
%{_datadir}/icons/hicolor/*/*/
%{_datadir}/locale/*/*/

%files -n %{name}-nautilus
%defattr(-,root,root)
#%doc COPYING
%doc COPYING.GPL3
%{python3_sitelib}/%{_name}_nautilus-*
%{_datadir}/nautilus-python/
