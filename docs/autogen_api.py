#!/usr/bin/env python
"""Script to auto-generate our API docs.
"""
# stdlib imports
import os
import sys

# local imports
sys.path.append(os.path.abspath('sphinxext'))
from apigen import ApiDocWriter

#*****************************************************************************
if __name__ == '__main__':
    pjoin = os.path.join
    package = 'menpo'
    outdir = pjoin('source', 'api', 'generated')
    docwriter = ApiDocWriter(package, rst_extension='.rst')

    # You have to escape the . here because . is a special char for regexps.
    # You must do make clean if you change this!
    # docwriter.package_skip_patterns += [r'\.external$']

    # The inputhook* modules often cause problems on import, such as trying to
    # load incompatible Qt bindings. It's easiest to leave them all out. The
    # main API is in the inputhook module, which is documented.
    # docwriter.module_skip_patterns += [ r'\.lib\.inputhook.+']
    
    # Now, generate the outputs
    docwriter.write_api_docs(outdir)
    # Write index with .txt extension - we can include it, but Sphinx won't try
    # to compile it
    docwriter.write_index(outdir, 'gen.txt',
                          relative_to=pjoin('menpo', 'api')
                          )
    print ('%d files written' % len(docwriter.written_modules))
