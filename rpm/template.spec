%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-rsl
Version:        1.1.0
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS rsl package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       fmt-devel
Requires:       ros-jazzy-rclcpp
Requires:       ros-jazzy-tcb-span
Requires:       ros-jazzy-tl-expected
Requires:       ros-jazzy-ros-workspace
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  fmt-devel
BuildRequires:  ros-jazzy-rclcpp
BuildRequires:  ros-jazzy-tcb-span
BuildRequires:  ros-jazzy-tl-expected
BuildRequires:  ros-jazzy-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  clang-tools-extra
BuildRequires:  git
BuildRequires:  range-v3-devel
%endif

%description
ROS Support Library

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
    -DCATKIN_ENABLE_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%files
/opt/ros/jazzy

%changelog
* Mon Apr 22 2024 Tyler Weaver <maybe@tylerjw.dev> - 1.1.0-2
- Autogenerated by Bloom

* Mon Apr 22 2024 Tyler Weaver <maybe@tylerjw.dev> - 1.1.0-1
- Autogenerated by Bloom

