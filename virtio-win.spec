%define virtio_win_dir /usr/share/virtio-win

Name:          virtio-win
Version:       0.0.1
Release:       1%{?dist}

Summary:       KVM virtio driver iso/vfd  
Group:         Documentation
License:       CC-BY-SA
URL:           http://www.github.com
Source0:       %{name}-0.1-74.iso
Source1:       %{name}-drivers-20120712-1.vfd
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:      

%description

This package contains the KVM virtio driver iso and 
vfd file

%prep
mkdir -p %{_builddir}/%{name}-%{version}/iso_tmp
mount -o loop %{SOURCE0} %{_builddir}/%{name}-%{version}/iso_tmp

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{virtio_win_dir}/
cp %{SOURCE0} $RPM_BUILD_ROOT/%{virtio_win_dir}/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{virtio_win_dir}/

mkdir -p %{buildroot}/%{virtio_win_dir}/drivers/amd64
mkdir -p %{buildroot}/%{virtio_win_dir}/drivers/i386
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/xp/amd64 %{buildroot}/%{virtio_win_dir}/drivers/amd64/Win2003
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/win7/amd64 %{buildroot}/%{virtio_win_dir}/drivers/amd64/Win2008
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/win7/amd64 %{buildroot}/%{virtio_win_dir}/drivers/amd64/Win7
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/xp/amd64 %{buildroot}/%{virtio_win_dir}/drivers/amd64/WinXP
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/xp/x86 %{buildroot}/%{virtio_win_dir}/drivers/i386/Win2003
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/win7/x86 %{buildroot}/%{virtio_win_dir}/drivers/i386/Win2008
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/win7/x86 %{buildroot}/%{virtio_win_dir}/drivers/i386/Win7
cp -r %{_builddir}/%{name}-%{version}/iso_tmp/xp/x86 %{buildroot}/%{virtio_win_dir}/drivers/i386/WinXP

umount %{_builddir}/%{name}-%{version}/iso_tmp
rm -rf %{_builddir}/%{name}-%{version}/iso_tmp

%clean
rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root,-)
%{virtio_win_dir}/*

%changelog
* Sun Apr 20 2014 Zhao Chao <chao.zhao@eayun.com> 0.0.1-1
- windows driver direcotry ready.

* Sat Apr 19 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1
- first

