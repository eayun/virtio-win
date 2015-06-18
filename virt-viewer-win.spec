%define virt_viewer_win_dir /usr/share/virt-viewer-win
%define virt_viewer_win_httpconf /etc/httpd/conf.d/virt_viewer_win.conf

Name:          virt-viewer-win
Version:       0.0.1
Release:       4%{?dist}

Summary:       spice client for windows
Group:         Documentation
License:       CC-BY-SA
URL:           http://www.github.com
Source:        %{name}-%{version}.tgz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:      
Requires(post): policycoreutils-python
Requires(postun): policycoreutils-python

%description

This package contains both 32bit and amd64 spice client
--virt-viewer for windows.

%prep
%setup -q -c $RPM_BUILD_DIR

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{virt_viewer_win_dir}/
cp -rf virt-viewer-win/* $RPM_BUILD_ROOT/%{virt_viewer_win_dir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
semanage fcontext -a -t httpd_sys_content_t '%{virt_viewer_win_dir}(/.*)?' 2>/dev/null || :
restorecon -R %{virt_viewer_win_dir} || :
cat > %{virt_viewer_win_httpconf} <<EOF
Alias /eayunVirt "%{virt_viewer_win_dir}"
<Directory "%{virt_viewer_win_dir}">
Options -Indexes
Order allow,deny
Allow from all
Require all granted
AddType application/octet-stream .msi
</Directory>
EOF

echo "Apache need to be restarted ..."
service httpd restart

%postun
if [ $1 -eq 0 ] ; then  # final removal
semanage fcontext -d -t httpd_sys_content_t '%{virt_viewer_win_dir}(/.*)?' 2>/dev/null || :
fi

if [ -e %{virt_viewer_win_httpconf} ]; then
rm -f %{virt_viewer_win_httpconf} || :
fi

%files
%defattr(-,root,root,-)
%{virt_viewer_win_dir}/*

%changelog
* Thu May 28 2014 Zhao Chao <chao.zhao@eayun.com> 0.0.1-4
- fix x64 client href url.
- fix mime type settings for msi files downloading.

* Thu May 28 2014 Zhao Chao <chao.zhao@eayun.com> 0.0.1-3
- add downloading webpage.

* Sun Apr 20 2014 Zhao Chao <chao.zhao@eayun.com> 0.0.1-2
- add SELinux support;
- add apache configure file.

* Sat Apr 19 2014 Li jiansheng <lijiangsheng1@gmail.com> 0.0.1
- first
