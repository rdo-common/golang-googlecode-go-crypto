%global debug_package   %{nil}
%global provider        google
%global provider_sub    code
%global provider_tld    com
%global project         p
%global repo            crypto
%global import_path     %{provider_sub}.%{provider}.%{provider_tld}/%{project}/go.%{repo}
%global rev             69e2a90ed92d03812364aeb947b7068dc42e561e
%global shortrev        %(r=%{rev}; echo ${r:0:12})

%global x_provider      golang
%global x_provider_tld  org
%global x_repo          crypto
%global x_import_path   %{x_provider}.%{x_provider_tld}/x/%{x_repo}
%global x_name          golang-%{x_provider}%{x_provider_tld}-%{repo}

Name:           golang-%{provider}%{provider_sub}-go-%{repo}
Version:        0
Release:        0.1.hg%{shortrev}%{?dist}
Summary:        Supplementary Go cryptography libraries
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{repo}.go%{provider}%{provider_sub}.%{provider_tld}/archive/%{rev}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{import_path}/bcrypt) = %{version}-%{release}
Provides:       golang(%{import_path}/blowfish) = %{version}-%{release}
Provides:       golang(%{import_path}/bn256) = %{version}-%{release}
Provides:       golang(%{import_path}/cast5) = %{version}-%{release}
Provides:       golang(%{import_path}/curve25519) = %{version}-%{release}
Provides:       golang(%{import_path}/hkdf) = %{version}-%{release}
Provides:       golang(%{import_path}/md4) = %{version}-%{release}
Provides:       golang(%{import_path}/nacl/box) = %{version}-%{release}
Provides:       golang(%{import_path}/nacl/secretbox) = %{version}-%{release}
Provides:       golang(%{import_path}/ocsp) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp/armor) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp/clearsign) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp/elgamal) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp/errors) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp/packet) = %{version}-%{release}
Provides:       golang(%{import_path}/openpgp/s2k) = %{version}-%{release}
Provides:       golang(%{import_path}/otr) = %{version}-%{release}
Provides:       golang(%{import_path}/pbkdf2) = %{version}-%{release}
Provides:       golang(%{import_path}/poly1305) = %{version}-%{release}
Provides:       golang(%{import_path}/ripemd160) = %{version}-%{release}
Provides:       golang(%{import_path}/salsa20) = %{version}-%{release}
Provides:       golang(%{import_path}/salsa20/salsa) = %{version}-%{release}
Provides:       golang(%{import_path}/scrypt) = %{version}-%{release}
Provides:       golang(%{import_path}/sha3) = %{version}-%{release}
Provides:       golang(%{import_path}/ssh) = %{version}-%{release}
Provides:       golang(%{import_path}/ssh/agent) = %{version}-%{release}
Provides:       golang(%{import_path}/ssh/terminal) = %{version}-%{release}
Provides:       golang(%{import_path}/ssh/test) = %{version}-%{release}
Provides:       golang(%{import_path}/ssh/testdata) = %{version}-%{release}
Provides:       golang(%{import_path}/twofish) = %{version}-%{release}
Provides:       golang(%{import_path}/xtea) = %{version}-%{release}
Provides:       golang(%{import_path}/xts) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go crypto libraries with code.google.com/p/ imports.

%package -n %{x_name}-devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        %{summary}
Provides:       golang(%{x_import_path}/bcrypt) = %{version}-%{release}
Provides:       golang(%{x_import_path}/blowfish) = %{version}-%{release}
Provides:       golang(%{x_import_path}/bn256) = %{version}-%{release}
Provides:       golang(%{x_import_path}/cast5) = %{version}-%{release}
Provides:       golang(%{x_import_path}/curve25519) = %{version}-%{release}
Provides:       golang(%{x_import_path}/hkdf) = %{version}-%{release}
Provides:       golang(%{x_import_path}/md4) = %{version}-%{release}
Provides:       golang(%{x_import_path}/nacl/box) = %{version}-%{release}
Provides:       golang(%{x_import_path}/nacl/secretbox) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ocsp) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp/armor) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp/clearsign) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp/elgamal) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp/errors) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp/packet) = %{version}-%{release}
Provides:       golang(%{x_import_path}/openpgp/s2k) = %{version}-%{release}
Provides:       golang(%{x_import_path}/otr) = %{version}-%{release}
Provides:       golang(%{x_import_path}/pbkdf2) = %{version}-%{release}
Provides:       golang(%{x_import_path}/poly1305) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ripemd160) = %{version}-%{release}
Provides:       golang(%{x_import_path}/salsa20) = %{version}-%{release}
Provides:       golang(%{x_import_path}/salsa20/salsa) = %{version}-%{release}
Provides:       golang(%{x_import_path}/scrypt) = %{version}-%{release}
Provides:       golang(%{x_import_path}/sha3) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ssh) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ssh/agent) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ssh/terminal) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ssh/test) = %{version}-%{release}
Provides:       golang(%{x_import_path}/ssh/testdata) = %{version}-%{release}
Provides:       golang(%{x_import_path}/twofish) = %{version}-%{release}
Provides:       golang(%{x_import_path}/xtea) = %{version}-%{release}
Provides:       golang(%{x_import_path}/xts) = %{version}-%{release}


%description -n %{x_name}-devel
%{summary}

This package contains library source intended for building other packages
which use the supplementary Go crypto libraries with golang.org/x/ imports.

%prep
%setup -q -n %{repo}.go-%{shortrev}

%build

%install
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
install -d -p %{buildroot}/%{gopath}/src/%{x_import_path}/
cp -rpav xts %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav xtea %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav twofish %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ssh %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav sha3 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav scrypt %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav salsa20 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ripemd160 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav poly1305 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav pbkdf2 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav otr %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav openpgp %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav ocsp %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav nacl %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav md4 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav hkdf %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav curve25519 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav cast5 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav bn256 %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav blowfish %{buildroot}/%{gopath}/src/%{import_path}/
cp -rpav bcrypt %{buildroot}/%{gopath}/src/%{import_path}/

cp -r %{buildroot}/%{gopath}/src/%{import_path}/ %{buildroot}/%{gopath}/src/%{x_import_path}/

cd %{buildroot}/%{gopath}/src/%{import_path}/
# from https://groups.google.com/forum/#!topic/golang-nuts/eD8dh3T9yyA, first post
sed -i 's/"golang\.org\/x\//"code\.google\.com\/p\/go\./g' \
        $(find . -name '*.go')

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/xts
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/xtea
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/twofish
# fails on ssh/keys_test.go:55: undefined: elliptic.P224 
#GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ssh
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ssh/test
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ssh/terminal
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ssh/agent
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/sha3
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/scrypt
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/salsa20
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/salsa20/salsa
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ripemd160
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/poly1305
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/pbkdf2
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/otr
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/openpgp
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/openpgp/s2k
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/openpgp/packet
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/openpgp/elgamal
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/openpgp/clearsign
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/openpgp/armor
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/ocsp
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/nacl/secretbox
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/nacl/box
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/md4
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/hkdf
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/curve25519
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/cast5
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/bn256
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/blowfish
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}/bcrypt

%files devel
%doc LICENSE README
%{gopath}/src/%{import_path}/

%files -n %{x_name}-devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%{gopath}/src/%{x_import_path}

%changelog
* Thu Dec 04 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.hg69e2a90ed92d
- First package for Fedora
  resolves: #1148704

