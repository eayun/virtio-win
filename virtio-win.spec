%define virtio_dir /usr/share/virtio-win

Name:          virtio-win
Version:       0.0.1
Release:        0%{?dist}

Summary:       KVM virtio driver iso/vfd  
Group:         Documentation
License:       CC-BY-SA
URL:           http://www.github.com
Source:        %{name}-%{version}.tgz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:      

%description

This package contains the KVM virtio driver iso and 
vfd file

%prep
%setup -q -c $RPM_BUILD_DIR

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{virtio_dir}/
cp -rf virtio-win $RPM_BUILD_ROOT/%{virtio_dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root,-)
%{virtio-win}/*

%changelog
* Sat Apr 19 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1
- first

