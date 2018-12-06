# https://github.com/AudriusButkevicius/kcp-go
%global goipath github.com/AudriusButkevicius/kcp-go
%global commit  5d7d1a807aa5b7817d03f6edae42d602e98487f7
%global date    20171227

%gometa

Name:           golang-github-AudriusButkevicius-kcp-go
Version:        0
Release:        0.8%{?dist}
Summary:        Full-featured reliable UDP communication library
License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

# Upstream ships a test that's broken in fedora build environments.
# It exceeds the hard-coded limit of 1024 open files.
Patch0:         00-disable-broken-tests.patch

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/klauspost/reedsolomon)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/templexxx/xor)
BuildRequires:  golang(github.com/tjfoc/gmsm/sm4)
BuildRequires:  golang(golang.org/x/crypto/blowfish)
BuildRequires:  golang(golang.org/x/crypto/cast5)
BuildRequires:  golang(golang.org/x/crypto/pbkdf2)
BuildRequires:  golang(golang.org/x/crypto/salsa20)
BuildRequires:  golang(golang.org/x/crypto/tea)
BuildRequires:  golang(golang.org/x/crypto/twofish)
BuildRequires:  golang(golang.org/x/crypto/xtea)
BuildRequires:  golang(golang.org/x/net/ipv4)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup
%patch0 -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20171227git5d7d1a8
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.20171227git5d7d1a8
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20171227git5d7d1a8
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20171227.git5d7d1a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20171227.git5d7d1a8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.3.20171227.git5d7d1a8
- Bump to commit 5d7d1a8.

* Wed Oct 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.2.20171025.git8ae5f52
- Bump to commit 8ae5f52.

* Sat Sep 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20180902.gitd17218b
- First package for Fedora

