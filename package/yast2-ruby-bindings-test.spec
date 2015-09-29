#
# spec file for package yast2-ruby-bindings-test
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-ruby-bindings-test
Version:        3.1.38
Url:            https://github.com/yast/yast-ruby-bindings
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-ruby-bindings-%{version}.tar.bz2
Prefix:         /usr
BuildArch:      noarch

# Test the matching version of the main package
BuildRequires:  yast2-ruby-bindings = %{version}
# RSpec as the test harness
%if 0%{suse_version} == 1310
BuildRequires:  rubygem-rspec
%else
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
%endif

# The following buildrequires are the reason to split off this package

# The test suite includes a regression test (std_streams_spec.rb) for a
# libyui-ncurses bug fixed in 2.47.3
BuildRequires:  libyui-ncurses >= 2.47.3
# The mentioned test requires screen in order to be executed in headless systems
BuildRequires:  screen

Summary:        Integration tests for YaST Ruby bindings
License:        GPL-2.0
Group:          System/YaST

%description
The bindings allow YaST modules to be written using the Ruby language
and also Ruby scripts can use YaST agents, APIs and modules.

%prep
%setup -n yast2-ruby-bindings-%{version}
%build

%install

%check
mkdir -p build/src/binary/{plugin,yast} # test_helper expects that
tests/ruby/integration/run.rb

%files
# none, the success/failure of the build is what matters

%changelog
