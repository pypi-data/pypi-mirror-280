#!/bin/sh
(echo "#!/bin/sh"; echo "black ."; echo "python lint.py -p molecularprofiles/"; echo "git add -u")> .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
