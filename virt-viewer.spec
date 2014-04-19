%define virt_viewer_dir /usr/share/virt-viewer

Name:          virt-viewer
Version:       0.0.1
Release:        0%{?dist}

Summary:       spice client for windows
Group:         Documentation
License:       CC-BY-SA
URL:           http://www.github.com
Source:        %{name}-%{version}.tgz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:      

%description

This package contains both 32bit and amd64 spice client
--virt-viewer for windows.

%prep
%setup -q -c $RPM_BUILD_DIR

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{virt_viewer_dir}/
cp -rf virt-viewer $RPM_BUILD_ROOT/%{virt_viewer_dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root,-)
%{virt_viewer_dir}/*

%changelog
* Sat Apr 19 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1
- first

