#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pdftools
Version  : 2.3
Release  : 18
URL      : https://cran.r-project.org/src/contrib/pdftools_2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pdftools_2.3.tar.gz
Summary  : Text Extraction, Rendering and Converting of PDF Documents
Group    : Development/Tools
License  : MIT
Requires: R-pdftools-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-qpdf
Requires: R-tesseract
BuildRequires : R-Rcpp
BuildRequires : R-qpdf
BuildRequires : R-tesseract
BuildRequires : buildreq-R
BuildRequires : pkgconfig(poppler-cpp)

%description
metadata from a PDF file. Also supports high quality rendering of PDF documents into
    PNG, JPEG, TIFF format, or into raw bitmap vectors for further processing in R.

%package lib
Summary: lib components for the R-pdftools package.
Group: Libraries

%description lib
lib components for the R-pdftools package.


%prep
%setup -q -c -n pdftools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574317154

%install
export SOURCE_DATE_EPOCH=1574317154
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdftools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdftools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdftools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pdftools || :


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
/usr/lib64/R/library/pdftools/libs/pdftools.so
