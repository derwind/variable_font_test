#! /bin/sh

# build the TTF version -- this requires a customized version of fontmake which
# is available at https://github.com/adobe-type-tools/fontmake
fontmake -m vuid_test.designspace -o variable --no-production-names
ttx -o vuid_test-Variable.ttf -m vuid_test-Variable.ttf GSUB_patch.ttx

# build the OTF version -- this requires an experimental build of the AFDKO which
# is available at http://www.adobe.com/devnet/opentype/afdko/AFDKO-Variable-Font-Support.html
buildMasterOTFs vuid_test.designspace
buildCFF2VF vuid_test.designspace vuid_test-Variable.otf
rm master_*/current.fpr

# replace the name, GPOS and GSUB tables in the OTF font by the ones from the TTF
sfntedit -x name=.tb_name,GSUB=.tb_GSUB vuid_test-Variable.ttf
sfntedit -a name=.tb_name,GSUB=.tb_GSUB vuid_test-Variable.otf

# delete temporary files
rm .tb_*
