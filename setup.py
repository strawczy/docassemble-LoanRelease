import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LoanRelease',
      version='1.0a',
      description=('Creates a new release form'),
      long_description='** Change Log **\r\n\r\n# 1.0\r\n- Added loan releases\r\n\r\n# 0.3.8a\r\n- Amended the language on the exit screen\r\n\r\n# 0.3.8\r\n- Added options to specify payment due date or payment plan\r\n- Removed redundant and potentially erroneous reference in release to property -- customer might not be "of" the service address\r\n- Changed release version\r\n\r\n# 0.3.7\r\n- Removed the "new session" option from the waiting screen as it seemed you could click past it into an undefined signature state.\r\n\r\n# 0.3.6\r\n\r\n- Clarified the instructions for payment methods\r\n- Modified the logic for asking about waiving arrears\r\n\r\n# 0.3.5\r\n\r\n- Fix for the issue where uploaded modified releases were not used to generate signed copies\r\n\r\n# 0.3.4\r\n\r\n- Fix for https://github.com/strawczy/docassemble-Release/issues/5\r\n- Fix for https://github.com/strawczy/docassemble-Release/issues/6\r\n- Amended proposed class proceedings release to reflect only one class action is moving forward\r\n\r\n# 0.3.3\r\n\r\n- Changed the text of the release notification email\r\n\r\n# 0.3.2\r\n\r\n- Fixed the spacing issue in the property damage release\r\n\r\n# 0.3.2\r\n\r\n- Added language for Defendant\'s Claims to be dismissed\r\n- Fixed some spacing issues\r\n\r\n# 0.3.1\r\n\r\n- Fixed an issue with the margins on the release template docx\r\n\r\n# 0.3\r\n\r\n- Added Ecohome and ODFS to list of companies\r\n- Company address in release depends on which company is giving the release\r\n- Added class action release but accessible only to legal\r\n\r\n# 0.2.16\r\n- Added Thermostat to list of equipment\r\n\r\n# 0.2.16\r\n- Moved the code for multi_user=True which appears to fix an issue with the link not being clickable.\r\n\r\n# 0.2.15\r\n- Added EAC\r\n- Fixed (?) signature flow\r\n\r\n# 0.2.14\r\n- Added Utilebill\r\n  \r\n# 0.2.13\r\n- Added water treatment system and detergent-less laundry system options\r\n\r\n# 0.2.12\r\n- added HCSI Home Comfort Inc.\r\n- fixed a bug on the review screen\r\n\r\n*** 0.2.12 ***\r\n- added HCSI Home Comfort Inc.\r\n- fixed a bug on the review screen\r\n\r\n** 0.2 **\r\n*** 0.2.9 ***\r\n- added HRVs\r\n\r\n*** 0.2.9 ***\r\n- added subtitle so the release lists in "my interviews"\r\n\r\n*** 0.2.9 ***\r\n- fixed bug in signature flow\r\n\r\n*** 0.2.8 ***\r\n- changed the comments to an input type: area\r\n\r\n*** 0.2.7 ***\r\n- activated live chat\r\n- changed review screen to format currency\r\n\r\n*** 0.2.6 ***\r\n= improved review screen\r\n\r\n*** 0.2.4 ***\r\n\r\nThis version supports a few new functions in the template:\r\n- declare the manner in which the customer is to deliver payment\r\n- explicitly confirm we are deliverning a copy of the NOSI discharge\r\n- clear up the release for customers who are on assigned contracts\r\n\r\n*** 0.2.3, 0.2.4 ***\r\n\r\nCode cleanup to enable storing the business logic variables\r\n\r\n*** 0.2.2 ***\r\n\r\nNow handles preparation by the person who will sign without sending emails\r\n\r\n*** 0.2.1 ***\r\n\r\nFixed the language on the signatory screen.\r\n\r\n*** 0.2.0 ***\r\n\r\nA significant upgrade, this is now a multi-user interview.  Once the drafter completes the release, they choose someone to sign it.  The release is automagically emailed to the signatory and, when it\'s done, the signed version is emailed to the drafter.\r\n\r\n** 0.1 **\r\n\r\n*** 0.1.14 ***\r\n- Added a provision for waiving arrears\r\n\r\n*** 0.1.13 ***\r\n- Fixed spacing\r\n\r\n*** 0.1.12 ***\r\n- Fixed paragraph break at end of lawsuit paragraph\r\n\r\n*** 0.1.11 ***\r\n- Change of Address\r\n\r\n*** 0.1.10 ***\r\n- Added language for settlement of lawsuits\r\n- Added Crown Crest Capital Management Corp.\r\n\r\n*** 0.1.9 ***\r\n- Added language regarding removal of NOSI\r\n\r\n*** 0.1.8\r\n- It\'s a mystery\r\n\r\n*** 0.1.7 ***\r\n- Added Umta and Akm as signatories\r\n\r\n*** 0.1.7 ***\r\n- fixed grammatical error\r\n\r\n*** 0.1.6 ***\r\n- fixed release.docx to use proper currency values with cents\r\n\r\n*** 0.1.5 ***\r\n- added heat pump to the equipment type\r\n- fixed typos in release.docx template\r\n\r\n*** 0.1.4 ***\r\n- revised metadata\r\n\r\n*** 0.1.3 ***\r\n- re-enabled DOCX files\r\n- cleaned up question language\r\n\r\n*** 0.1.2 ***\r\nGrammar fixes to the release\r\n\r\n*** 0.1.1 ***\r\nIncorporated feedback from Fiona on questions\r\n\r\n*** 0.0.5 ***\r\nAdded a new simple (not mutual) release when there\'s water damage but contract continues.\r\n\r\n*** 0.0.4 ***\r\n- Added login requirement\r\n',
      long_description_content_type='text/markdown',
      author='Oscar Strawczynski',
      author_email='Oscar.strawczynski@mysimplygroup.com',
      license='All rights reserved',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LoanRelease/', package='docassemble.LoanRelease'),
     )

