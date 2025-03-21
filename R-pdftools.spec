#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-pdftools
Version  : 3.5.0
Release  : 62
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/pdftools_3.5.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/pdftools_3.5.0.tar.gz
Summary  : Text Extraction, Rendering and Converting of PDF Documents
Group    : Development/Tools
License  : MIT
Requires: R-pdftools-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-qpdf
BuildRequires : R-Rcpp
BuildRequires : R-qpdf
BuildRequires : buildreq-R
BuildRequires : pkgconfig(poppler-cpp)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
text, fonts, attachments and metadata from a PDF file. Also supports high quality rendering
    of PDF documents into PNG, JPEG, TIFF format, or into raw bitmap vectors for further 
    processing in R.

%package lib
Summary: lib components for the R-pdftools package.
Group: Libraries

%description lib
lib components for the R-pdftools package.


%prep
%setup -q -n pdftools
pushd ..
cp -a pdftools buildavx2
popd
pushd ..
cp -a pdftools buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1741122841

%install
export SOURCE_DATE_EPOCH=1741122841
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pdftools/DESCRIPTION
/usr/lib64/R/library/pdftools/INDEX
/usr/lib64/R/library/pdftools/LICENSE
/usr/lib64/R/library/pdftools/Meta/Rd.rds
/usr/lib64/R/library/pdftools/Meta/features.rds
/usr/lib64/R/library/pdftools/Meta/hsearch.rds
/usr/lib64/R/library/pdftools/Meta/links.rds
/usr/lib64/R/library/pdftools/Meta/nsInfo.rds
/usr/lib64/R/library/pdftools/Meta/package.rds
/usr/lib64/R/library/pdftools/NAMESPACE
/usr/lib64/R/library/pdftools/NEWS
/usr/lib64/R/library/pdftools/R/pdftools
/usr/lib64/R/library/pdftools/R/pdftools.rdb
/usr/lib64/R/library/pdftools/R/pdftools.rdx
/usr/lib64/R/library/pdftools/help/AnIndex
/usr/lib64/R/library/pdftools/help/aliases.rds
/usr/lib64/R/library/pdftools/help/paths.rds
/usr/lib64/R/library/pdftools/help/pdftools.rdb
/usr/lib64/R/library/pdftools/help/pdftools.rdx
/usr/lib64/R/library/pdftools/html/00Index.html
/usr/lib64/R/library/pdftools/html/R.css
/usr/lib64/R/library/pdftools/tests/testthat.R
/usr/lib64/R/library/pdftools/tests/testthat/active-pdf-links.original.pdf
/usr/lib64/R/library/pdftools/tests/testthat/chinese.pdf
/usr/lib64/R/library/pdftools/tests/testthat/gangnam.pdf
/usr/lib64/R/library/pdftools/tests/testthat/hello.pdf
/usr/lib64/R/library/pdftools/tests/testthat/pdf-example-encryption.original.pdf
/usr/lib64/R/library/pdftools/tests/testthat/pdf-example-fonts.original.pdf
/usr/lib64/R/library/pdftools/tests/testthat/pdf-example-password.original.pdf
/usr/lib64/R/library/pdftools/tests/testthat/pdf-example-watermarks.original.pdf
/usr/lib64/R/library/pdftools/tests/testthat/test-chinese.R
/usr/lib64/R/library/pdftools/tests/testthat/test-encoding.R
/usr/lib64/R/library/pdftools/tests/testthat/test-reading.R
/usr/lib64/R/library/pdftools/tests/testthat/test-render.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/pdftools/libs/pdftools.so
/V4/usr/lib64/R/library/pdftools/libs/pdftools.so
/usr/lib64/R/library/pdftools/libs/pdftools.so
