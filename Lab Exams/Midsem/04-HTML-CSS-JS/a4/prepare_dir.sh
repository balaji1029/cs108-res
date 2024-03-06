# This script can be used to tacle.instrictor error, permission to shell files and tar direcrtories.
# To use this script copy it in the directory that contains labDirectory and evaluationScripts folder

rm -rf .evaluationScripts
cp -r evaluationScripts .evaluationScripts
sed -i s,../evaluationScripts,/home/.evaluationScripts, .evaluationScripts/evaluate.sh
chmod 777 -R .evaluationScripts
tar -cvzf clientEvaluationFiles.tgz .evaluationScripts
tar -cvzf lab.tgz labDirectory
